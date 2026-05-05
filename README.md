# YanglabPDK

YanglabPDK is a lightweight photonic layout package used by Prof. Lan Yang's
Lab as a local middle layer on top of
[gdsfactory](https://gdsfactory.github.io/gdsfactory/).  It keeps lab-specific
layers, cross sections, utility geometry operations, and reusable components in
one place so design scripts do not need to call raw gdsfactory primitives for
every layout.

The package is intentionally close to the gdsfactory programming model:
components return `gf.Component`, reusable cells are decorated with `@gf.cell`,
and cross sections are built with `gf.CrossSection` / `gf.Section`.

## What Is In This Package

- `YanglabLayerStack.py`: lab layer map constants such as waveguide, metal,
  marker, positive resist, and negative resist layers.
- `YanglabSections.py`: common cross sections, especially the positive/negative
  resist patterns used by the lab process.
- `YanglabUtils.py`: geometry post-processing helpers for layer remapping,
  layer copying/removal, resist separation, and coordinate rounding.
- `components/`: reusable photonic and layout building blocks grouped by device
  family.

Common component families include:

- `components.waveguides`: straight waveguides and heater-integrated straights.
- `components.bends`: circular, Euler, S-bend, and Bezier bends.
- `components.couplers`: directional, asymmetric, adiabatic, ring, and 90-degree
  couplers.
- `components.cavities`: ring and Fabry-Perot style cavities.
- `components.mmis`, `components.mzis`, `components.spirals`,
  `components.filters`, `components.metals`, `components.utils`: higher-level
  building blocks and layout utilities.

## Requirements

- Python 3.10 or newer is recommended.
- gdsfactory 9.1 or newer.
- numpy for selected generated components.

The package currently assumes it is importable as `YanglabPDK`.

## Installation For Local Lab Use

The current lab workflow uses a `.pth` file rather than a published package.

1. Clone this repository.
2. Create a file named `module_yanglabpdk.pth` in your Python environment's
   `Lib/site-packages` directory.
3. Put the parent directory of `YanglabPDK` into that `.pth` file.
4. Restart Python and verify the import:

```python
import YanglabPDK as ypdk
print(ypdk.LAYER.WG)
```

## Quick Start

```python
import gdsfactory as gf
from YanglabPDK.components.waveguides import straight
from YanglabPDK.components.bends import bend_circular

c = gf.Component("demo")
wg = c << straight(length=100, width=1, buffer=3)
bend = c << bend_circular(radius=30, width=1, buffer=3)
bend.connect("o1", wg.ports["o2"])

c.show()
```

## Design Conventions

- Lengths and widths are in microns, following gdsfactory conventions.
- Components should return a `gf.Component` and expose meaningful ports.
- New reusable cells should use `@gf.cell` unless there is a strong reason not
  to cache them.
- Layout generators should prefer the layer constants from `YanglabPDK.LAYER`
  instead of hard-coded `(layer, datatype)` tuples.
- Positive/negative resist waveguide components should usually use
  `YanglabSections.pos_neg_resist()` and then run
  `YanglabUtils.pos_neg_seperate()` before returning the final component.

## Adding A New Component

1. Add the component file under the most relevant folder in `components/`.
2. Implement a function that returns `gf.Component`.
3. Add a short docstring explaining the device, important parameters, units, and
   returned ports.
4. Export the function from that folder's `__init__.py`.
5. Add a small `if __name__ == "__main__":` preview block only when it helps
   manual layout inspection.

Example structure:

```python
import gdsfactory as gf


@gf.cell
def my_component(length: float = 10.0) -> gf.Component:
    """Return a lab-specific component.

    Args:
        length: Component length in microns.

    Returns:
        Component with optical ports `o1` and `o2`.
    """
    c = gf.Component()
    ...
    return c
```

## Building API Documentation

Install the documentation dependencies once:

```powershell
python -m pip install -r requirements-docs.txt
```

Then regenerate the component catalog and local HTML site with:

```powershell
python scripts/build_docs.py
```

The HTML entry point is written to:

```text
docs/_build/html/index.html
```

The component catalog is generated from the source tree and should not be edited
by hand. Preview images are best-effort: components that cannot be imported or
instantiated with default parameters are recorded in
`docs/generated/component_report.md`.

## Current Notes

- Generated layout files under `build/gds/` are outputs, not source files.
- Python cache folders such as `__pycache__/` are not part of the source API.
- Some older component docstrings may still contain encoding artifacts from
  copied diagrams. Prefer plain ASCII diagrams or clear text descriptions when
  updating them.
