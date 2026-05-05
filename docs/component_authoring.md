# Component Authoring Guide

This guide records the conventions used by YanglabPDK component generators.
Keeping new cells consistent makes the package easier to reuse in experiment
scripts and easier to debug when a generated GDS looks wrong.

## Basic Pattern

```python
import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections


@gf.cell
def example(length: float = 10.0, width: float = 1.0, buffer: float = 3.0) -> gf.Component:
    """Return an example positive/negative resist waveguide.

    Args:
        length: Waveguide length in microns.
        width: Negative-resist core width in microns.
        buffer: Positive-resist buffer width on each side in microns.

    Returns:
        Component with optical ports `o1` and `o2`.
    """
    c = gf.components.straight(
        length=length,
        cross_section=Sections.pos_neg_resist(width=width, buffer=buffer),
    )
    return Utils.pos_neg_seperate(c)
```

## Recommended Docstring Content

Each public component should explain:

- What physical/layout structure it returns.
- Units for non-obvious parameters.
- The meaning of key geometry parameters such as `gap`, `radius`, `length_x`,
  `length_y`, `width`, and `buffer`.
- Returned optical or electrical port names.
- Any geometry restrictions that raise `ValueError`.

Keep ASCII diagrams optional.  A clear sentence is better than a diagram that
breaks under a different terminal encoding.

## Layer Rules

- Import `LAYER` from `YanglabPDK` or use `YanglabPDK.LAYER`.
- Avoid hard-coded layer tuples in component files unless a temporary debug
  layer is being created.
- Use `YanglabUtils.remap_layers()` when copying gdsfactory primitives from one
  layer to another.
- Use `YanglabUtils.pos_neg_seperate()` for cells that combine `LAYER.PR` and
  `LAYER.NR`.

## Port Rules

- Optical waveguide ports should normally use `o1`, `o2`, `o3`, ...
- Electrical ports should use names that communicate the pad or direction, such
  as `e1_0`, `e1_180`, or `heater_left`.
- Prefer copying ports from the underlying gdsfactory component when the
  geometry is only post-processed.

## Manual Preview Blocks

Preview blocks are useful, but they should stay small:

```python
if __name__ == "__main__":
    c = example()
    c.show()
```

Avoid writing generated files from preview blocks unless the file path is
intentional and documented.
