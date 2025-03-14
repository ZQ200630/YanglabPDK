import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def bend_s(size=[10, 10], width=1, buffer=3) -> gf.Component:
    """Return S bend with bezier curve.

    stores min_bend_radius property in self.info['min_bend_radius']
    min_bend_radius depends on height and length

    Args:
        size: in x and y direction.
        width: width to use. Defaults to cross_section.width.
        buffer: buffer width for positive tone resist (um)

    """
    c = Utils.pos_neg_seperate(gf.components.bend_s(size=size, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))
    return c

if __name__ == "__main__":
    c = bend_s()
    c.show()