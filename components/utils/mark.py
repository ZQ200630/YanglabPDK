import gdsfactory as gf

from gdsfactory.typings import Layer
from YanglabPDK import LAYER
from functools import partial

@gf.cell
def cross(
    outter_length: float = 200,
    outter_width: float = 5,
    inner_width: float = 1,
    layer: Layer = LAYER.MK,
    text: str = '1'
) -> gf.Component:
    c = gf.Component()
    # Larger Cross
    l_cross = c << gf.components.cross(length=outter_length, width=outter_width, layer=layer)
    # Smaller Cross
    s_cross = c << gf.components.cross(length=outter_width, width=inner_width, layer=layer)
    l_cross.center = (0, 0)
    s_cross.center = (0, 0)
    # Boolean, subtraction
    comp = gf.Component()
    cross = comp << gf.boolean(l_cross, s_cross, operation='A-B', layer=LAYER.MK, layer1=LAYER.MK, layer2=LAYER.MK)
    text = comp << gf.components.text(text=text, size=10, layer=layer)
    cross.center = (0, 0)
    text.center = (15, 15)
    return comp


if __name__ == "__main__":
    c = cross()
    c.show()