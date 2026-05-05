# YanglabPDK Documentation

YanglabPDK is a lab-specific middle layer on top of gdsfactory.  It collects
the layer map, cross sections, geometry utilities, and reusable photonic
components used by Prof. Lan Yang's Lab.

This documentation is generated from the source tree so it can stay close to
the code.  After adding or editing components, rebuild the docs with:

```powershell
python scripts/build_docs.py
```

The generated HTML site is written to:

```text
docs/_build/html/index.html
```

```{toctree}
:maxdepth: 2
:caption: Guides

project_structure
component_authoring
components/index
api
generated/component_report
```

