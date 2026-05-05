"""Build the local YanglabPDK documentation site."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
HTML_DIR = DOCS_DIR / "_build" / "html"


def run(command: list[str]) -> int:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = str(ROOT.parent) + os.pathsep + env.get("PYTHONPATH", "")
    completed = subprocess.run(command, cwd=ROOT, env=env)
    return completed.returncode


def main() -> int:
    generator_status = run([sys.executable, str(ROOT / "scripts" / "generate_component_docs.py")])
    if generator_status != 0:
        return generator_status

    sphinx_status = run([sys.executable, "-m", "sphinx", "-b", "html", str(DOCS_DIR), str(HTML_DIR)])
    if sphinx_status != 0:
        print("")
        print("Sphinx build failed. Install documentation dependencies with:")
        print("  python -m pip install -r requirements-docs.txt")
        return sphinx_status

    print("")
    print(f"Documentation built at: {HTML_DIR / 'index.html'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

