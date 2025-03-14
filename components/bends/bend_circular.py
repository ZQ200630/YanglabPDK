import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def bend_circular(radius=100, angle=90, width=1, buffer=3) -> gf.Component:
    """Returns a radial arc.

    Args:
        radius: in um. Defaults to cross_section_radius.
        angle: angle of arc (degrees).
        width: width to use. Defaults to cross_section.width.
        buffer: buffer width for positive tone resist (um)
    """
    c = Utils.pos_neg_seperate(gf.components.bend_circular(radius=radius, angle=angle, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))
    # print(c.ports)
    return c

if __name__ == "__main__":
    c = bend_circular(radius=100)
    c.show()