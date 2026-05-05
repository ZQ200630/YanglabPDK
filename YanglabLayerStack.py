"""Layer definitions used across YanglabPDK.

`YanglabLayerMap` is the canonical place for lab layer numbers.  Component
generators should import `YanglabPDK.LAYER` and refer to these symbolic names
instead of repeating raw `(layer, datatype)` tuples.
"""

from gdsfactory.typings import Layer
from gdsfactory.technology import (
    LayerMap,
)


class YanglabLayerMap(LayerMap):
    """Lab-specific GDS layer map.

    The attribute names are short by design because they appear frequently in
    layout scripts.  Keep new names stable once they are used in generated
    masks or shared design files.
    """

    # Field Layer
    FD: Layer = (0, 0)
    # Waveguide Layer
    WG: Layer = (1, 0)
    # Metal Layer(Gold)
    MT1: Layer = (2, 0)
    # Second Metal Layer
    MT2: Layer = (21, 0)
    # Text Layer
    TX: Layer = (3, 0)
    # Assisted Layer, As Frame of Slabs
    AS: Layer = (5, 0)
    # Mark Layer
    MK: Layer = (7, 0)
    # Version Layer
    VT: Layer = (8, 0)
    # Anchor Point Layer, help beamer locate the fields
    AC: Layer = (9, 0)
    # Hidden Layer, show parameters
    HD: Layer = (10, 0)
    # Silica Substrate
    SL: Layer = (99, 0)
    # Cladding Layer
    CL: Layer = (55, 0)
    # Positive Photoresist Layer
    PR: Layer = (60, 0)
    # Negative Photoresist Layer
    NR: Layer = (61, 0)
    # Deep Trench Layer
    DT: Layer = (33, 0)
    # Die Layer
    DIE: Layer = (100, 0)
    # Cutting Layer
    CUT: Layer = (101, 0)
    # All
    ALL: Layer = (255, 0)
    # Keep Out Layer
    KO: Layer = (121, 0)
    # Grid Layer
    GRID: Layer = (122, 0)
    # Grid Text Layer
    GRID_TX: Layer = (123, 0)
    # Litho Ruler Layer
    RULER: Layer = (124, 0)
    # Marker Expose Layer
    EX: Layer = (125, 0)
