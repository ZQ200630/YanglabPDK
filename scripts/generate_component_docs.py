"""Generate Markdown API pages and best-effort previews for YanglabPDK cells."""

from __future__ import annotations

import ast
import importlib
import inspect
import os
import re
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_PARENT = ROOT.parent
PACKAGE_NAME = ROOT.name
COMPONENTS_DIR = ROOT / "components"
DOCS_DIR = ROOT / "docs"
GENERATED_DIR = DOCS_DIR / "generated"
PREVIEW_DIR = DOCS_DIR / "_static" / "component_previews"


@dataclass(frozen=True)
class ParameterEntry:
    """Function parameter metadata for generated API pages."""

    name: str
    annotation: str
    default: str
    description: str


@dataclass(frozen=True)
class ComponentEntry:
    """Metadata extracted for a public component function."""

    group: str
    function_name: str
    module_name: str
    source_path: Path
    source_line: int
    signature: str
    docstring: str
    summary: str
    parameters: tuple[ParameterEntry, ...]
    returns: str
    return_type: str
    has_required_args: bool
    discovered_by: str

    @property
    def qualified_name(self) -> str:
        return f"{self.module_name}.{self.function_name}"

    @property
    def preview_filename(self) -> str:
        safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", self.qualified_name)
        return f"{safe_name}.png"


@dataclass
class PreviewResult:
    """Preview generation result for one component."""

    status: str
    detail: str


def read_ast(path: Path) -> ast.Module | None:
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except UnicodeDecodeError:
        return ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
    except SyntaxError:
        return None


def decorator_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = decorator_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    if isinstance(node, ast.Call):
        return decorator_name(node.func)
    return ""


def is_gf_cell(function: ast.FunctionDef) -> bool:
    return any(decorator_name(decorator) in {"gf.cell", "cell"} for decorator in function.decorator_list)


def parse_all_names(module: ast.Module) -> set[str]:
    names: set[str] = set()
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "__all__" for target in node.targets):
            continue
        try:
            value = ast.literal_eval(node.value)
        except Exception:
            continue
        if isinstance(value, (list, tuple, set)):
            names.update(item for item in value if isinstance(item, str))
    return names


def parse_imported_exports(init_path: Path) -> dict[str, str]:
    module = read_ast(init_path)
    if module is None:
        return {}

    exported_names = parse_all_names(module)
    mapping: dict[str, str] = {}
    for node in module.body:
        if not isinstance(node, ast.ImportFrom) or node.module is None:
            continue
        for alias in node.names:
            public_name = alias.asname or alias.name
            if public_name in exported_names:
                mapping[alias.name] = public_name
    return mapping


def module_name_from_path(path: Path) -> str:
    relative = path.relative_to(ROOT).with_suffix("")
    return ".".join([PACKAGE_NAME, *relative.parts])


def group_from_path(path: Path) -> str:
    relative = path.relative_to(COMPONENTS_DIR)
    return relative.parts[0] if len(relative.parts) > 1 else "components"


def function_signature(function: ast.FunctionDef) -> str:
    args = ast.unparse(function.args)
    returns = f" -> {ast.unparse(function.returns)}" if function.returns else ""
    return f"{function.name}({args}){returns}"


def function_parameters(function: ast.FunctionDef, descriptions: dict[str, str]) -> tuple[ParameterEntry, ...]:
    entries: list[ParameterEntry] = []
    args = [*function.args.posonlyargs, *function.args.args]
    defaults: list[ast.expr | None] = [None] * (len(args) - len(function.args.defaults)) + list(function.args.defaults)

    for arg, default in zip(args, defaults):
        if arg.arg in {"self", "cls"}:
            continue
        annotation = ast.unparse(arg.annotation) if arg.annotation else "Any"
        default_text = ast.unparse(default) if default is not None else ""
        entries.append(
            ParameterEntry(
                name=arg.arg,
                annotation=annotation,
                default=default_text,
                description=descriptions.get(arg.arg, "No description available."),
            )
        )

    for arg, default in zip(function.args.kwonlyargs, function.args.kw_defaults):
        annotation = ast.unparse(arg.annotation) if arg.annotation else "Any"
        default_text = ast.unparse(default) if default is not None else ""
        entries.append(
            ParameterEntry(
                name=arg.arg,
                annotation=annotation,
                default=default_text,
                description=descriptions.get(arg.arg, "No description available."),
            )
        )

    return tuple(entries)


def has_required_positional_args(function: ast.FunctionDef) -> bool:
    positional = [*function.args.posonlyargs, *function.args.args]
    required_count = len(positional) - len(function.args.defaults)
    return required_count > 0


def function_returns_component(function: ast.FunctionDef) -> bool:
    if function.returns is not None and "Component" in ast.unparse(function.returns):
        return True

    for node in ast.walk(function):
        if isinstance(node, ast.Return):
            value = node.value
            if isinstance(value, ast.Name) and value.id in {"c", "component", "comp", "all_comp"}:
                return True
            if isinstance(value, ast.Call):
                call_text = ast.unparse(value)
                if "pos_neg_seperate" in call_text or "gf.Component" in call_text:
                    return True
    return False


def parse_docstring(docstring: str, fallback_name: str) -> tuple[str, dict[str, str], str]:
    if not docstring:
        return f"Return the `{fallback_name}` component.", {}, "Generated gdsfactory component."

    lines = inspect.cleandoc(docstring).splitlines()
    summary_lines: list[str] = []
    parameter_descriptions: dict[str, str] = {}
    returns_lines: list[str] = []
    section: str | None = None
    current_param: str | None = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue

        lower = line.lower().rstrip(":")
        if lower in {"args", "arguments", "parameters"}:
            section = "parameters"
            current_param = None
            continue
        if lower in {"returns", "return"}:
            section = "returns"
            current_param = None
            continue
        if line.startswith(".. code::"):
            section = "code"
            current_param = None
            continue

        if section is None:
            summary_lines.append(line)
        elif section == "parameters":
            match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\s*\([^)]*\))?\s*:\s*(.*)$", line)
            if match:
                current_param = match.group(1)
                parameter_descriptions[current_param] = match.group(2).strip() or "No description available."
            elif current_param:
                parameter_descriptions[current_param] += " " + line
        elif section == "returns":
            returns_lines.append(line)

    summary = " ".join(summary_lines).strip() or f"Return the `{fallback_name}` component."
    returns = " ".join(returns_lines).strip() or "Generated gdsfactory component."
    return summary, parameter_descriptions, returns


def discover_components() -> list[ComponentEntry]:
    entries: dict[str, ComponentEntry] = {}

    all_exports_by_module: dict[Path, set[str]] = {}
    export_aliases_by_module: dict[Path, dict[str, str]] = {}
    for init_path in COMPONENTS_DIR.rglob("__init__.py"):
        module = read_ast(init_path)
        if module is not None:
            all_exports_by_module[init_path.parent] = parse_all_names(module)
            export_aliases_by_module[init_path.parent] = parse_imported_exports(init_path)

    for path in sorted(COMPONENTS_DIR.rglob("*.py")):
        if "__pycache__" in path.parts or path.name == "__init__.py":
            continue
        module = read_ast(path)
        if module is None:
            continue

        exported_names = all_exports_by_module.get(path.parent, set())
        export_aliases = export_aliases_by_module.get(path.parent, {})
        for node in module.body:
            if not isinstance(node, ast.FunctionDef):
                continue

            by_cell = is_gf_cell(node)
            by_export = node.name in exported_names or node.name in export_aliases
            by_component_shape = function_returns_component(node)
            if not by_cell and not by_export and not by_component_shape:
                continue

            module_name = module_name_from_path(path)
            key = f"{module_name}.{node.name}"
            docstring = inspect.cleandoc(ast.get_docstring(node) or "")
            summary, parameter_descriptions, returns = parse_docstring(docstring, node.name)
            return_type = ast.unparse(node.returns) if node.returns else "gf.Component"
            entries[key] = ComponentEntry(
                group=group_from_path(path),
                function_name=node.name,
                module_name=module_name,
                source_path=path,
                source_line=node.lineno,
                signature=function_signature(node),
                docstring=docstring,
                summary=summary,
                parameters=function_parameters(node, parameter_descriptions),
                returns=returns,
                return_type=return_type,
                has_required_args=has_required_positional_args(node),
                discovered_by="gf.cell + __all__" if by_cell and by_export else "gf.cell" if by_cell else "__all__" if by_export else "component return",
            )

    return sorted(entries.values(), key=lambda entry: (entry.group, entry.module_name, entry.function_name))


def prepare_gdsfactory_runtime() -> PreviewResult | None:
    try:
        import gdsfactory as gf
    except Exception as exc:
        return PreviewResult("unavailable", f"gdsfactory import failed: {type(exc).__name__}: {exc}")

    try:
        gf.get_active_pdk()
    except Exception:
        try:
            gf.gpdk.get_generic_pdk().activate()
        except Exception as exc:
            return PreviewResult("unavailable", f"could not activate generic PDK: {type(exc).__name__}: {exc}")

    return None


def import_function(entry: ComponentEntry) -> Any:
    if str(PACKAGE_PARENT) not in sys.path:
        sys.path.insert(0, str(PACKAGE_PARENT))
    module = importlib.import_module(entry.module_name)
    return getattr(module, entry.function_name)


def has_required_parameters(function: Any) -> bool:
    signature = inspect.signature(function)
    for parameter in signature.parameters.values():
        if parameter.kind in {parameter.VAR_POSITIONAL, parameter.VAR_KEYWORD}:
            continue
        if parameter.default is inspect.Parameter.empty:
            return True
    return False


def render_preview(component: Any, output_path: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plot_result = component.plot()
    figure = None
    if hasattr(plot_result, "savefig"):
        figure = plot_result
    elif isinstance(plot_result, (tuple, list)):
        for item in plot_result:
            if hasattr(item, "savefig"):
                figure = item
                break
            if hasattr(item, "figure"):
                figure = item.figure
                break

    if figure is None:
        figure = plt.gcf()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)


def generate_preview(entry: ComponentEntry) -> PreviewResult:
    if entry.has_required_args:
        return PreviewResult("skipped", "function has required arguments without defaults")

    runtime_error = prepare_gdsfactory_runtime()
    if runtime_error is not None:
        return runtime_error

    try:
        function = import_function(entry)
        if has_required_parameters(function):
            return PreviewResult("skipped", "runtime signature has required arguments without defaults")
        component = function()
        render_preview(component, PREVIEW_DIR / entry.preview_filename)
    except Exception as exc:
        detail = f"{type(exc).__name__}: {exc}"
        return PreviewResult("failed", detail)

    return PreviewResult("generated", f"_static/component_previews/{entry.preview_filename}")


def markdown_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("|", "\\|")


def format_signature(entry: ComponentEntry) -> str:
    return f"{entry.module_name}.{entry.signature}"


def write_components_markdown(entries: list[ComponentEntry], previews: dict[str, PreviewResult]) -> None:
    lines = [
        "# Generated Component Reference",
        "",
        "This page is generated from the `components/` source tree.  Do not edit it by hand.",
        "",
    ]

    groups = sorted({entry.group for entry in entries})
    lines.extend(["## Contents", ""])
    for group in groups:
        lines.append(f"- <a href=\"#{group}\">{group}</a>")
    lines.append("")

    for group in groups:
        lines.extend([f"## {group}", ""])
        group_entries = [entry for entry in entries if entry.group == group]
        for entry in group_entries:
            preview = previews[entry.qualified_name]
            lines.extend(
                [
                    f"### `{entry.module_name}.{entry.function_name}`",
                    "",
                    "```python",
                    format_signature(entry),
                    "```",
                    "",
                    f"[source: `{entry.source_path.relative_to(ROOT).as_posix()}:{entry.source_line}`]",
                    "",
                ]
            )

            if preview.status == "generated":
                lines.extend([f"![{entry.function_name} preview](../_static/component_previews/{entry.preview_filename})", ""])
            else:
                lines.extend([f"**Preview:** {preview.status} - {preview.detail}", ""])

            lines.extend([entry.summary, "", "**Parameters:**", ""])
            if entry.parameters:
                for parameter in entry.parameters:
                    type_text = f" ({parameter.annotation})" if parameter.annotation else ""
                    default_text = f" Defaults to `{parameter.default}`." if parameter.default else ""
                    lines.append(
                        f"- **{parameter.name}**{type_text} - {parameter.description}{default_text}"
                    )
                lines.append("")
            else:
                lines.extend(["This component does not expose public parameters.", ""])

            lines.extend(
                [
                    "**Returns:**",
                    "",
                    entry.returns,
                    "",
                    "**Return type:**",
                    "",
                    f"`{entry.return_type}`",
                    "",
                    f"**Discovered by:** `{entry.discovered_by}`",
                    "",
                ]
            )

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    (GENERATED_DIR / "components.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_report(entries: list[ComponentEntry], previews: dict[str, PreviewResult]) -> None:
    counts: dict[str, int] = {}
    for result in previews.values():
        counts[result.status] = counts.get(result.status, 0) + 1

    lines = [
        "# Component Generation Report",
        "",
        "This report is generated by `scripts/generate_component_docs.py`.",
        "",
        "## Summary",
        "",
        f"- Components discovered: {len(entries)}",
    ]
    for status in sorted(counts):
        lines.append(f"- {status}: {counts[status]}")

    lines.extend(
        [
            "",
            "## Details",
            "",
            "| Component | Group | Preview status | Detail |",
            "| --- | --- | --- | --- |",
        ]
    )

    for entry in entries:
        result = previews[entry.qualified_name]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{markdown_escape(entry.qualified_name)}`",
                    markdown_escape(entry.group),
                    markdown_escape(result.status),
                    markdown_escape(result.detail),
                ]
            )
            + " |"
        )

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    (GENERATED_DIR / "component_report.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    entries = discover_components()
    previews: dict[str, PreviewResult] = {}

    for entry in entries:
        try:
            previews[entry.qualified_name] = generate_preview(entry)
        except Exception:
            previews[entry.qualified_name] = PreviewResult("failed", traceback.format_exc(limit=1).strip())

    write_components_markdown(entries, previews)
    write_report(entries, previews)

    print(f"Discovered {len(entries)} components.")
    print(f"Wrote {GENERATED_DIR / 'components.md'}")
    print(f"Wrote {GENERATED_DIR / 'component_report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
