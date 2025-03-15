import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def bend_euler(
    radius: float = 100, 
    angle: float = 90, 
    p: float = 0.5, 
    width: float = 1, 
    buffer: float = 3
) -> gf.Component:
    """Regular degree euler bend.

    Args:
        radius: in um. Defaults to cross_section_radius.
        angle: total angle of the curve.
        p: Proportion of the curve that is an Euler curve.
        width: width to use. Defaults to cross_section.width.
        buffer: buffer width for positive tone resist (um)
    """
    return Utils.pos_neg_seperate(gf.components.bend_euler(radius=radius, angle=angle, with_arc_floorplan=False, p=p, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def bend_euler_s(
    radius: float = 100, 
    angle: float = 30, 
    p: float = 0.5, 
    width: float = 1, 
    buffer: float = 3
) -> gf.Component:
    r"""Sbend made of 2 euler bends.

    Args:
        radius: in um. Defaults to cross_section_radius.
        angle: total angle of the curve
        p: Proportion of the curve that is an Euler curve.
        width: width to use. Defaults to cross_section.width.
        buffer: buffer width for positive tone resist (um)


    .. code::

                        _____ o2
                       /
                      /
                     /
                    /
                    |
                   /
                  /
                 /
         o1_____/

    """
    c = gf.Component()
    b = bend_euler(radius=radius, angle=angle, p=p, width=width, buffer=buffer)
    bend_1 = c << b
    bend_2 = c << b
    bend_1.center = (0, 0)
    bend_2.connect("o2", bend_1.ports["o2"])
    c.add_port("o1", port=bend_1.ports["o1"])
    c.add_port("o2", port=bend_2.ports["o1"])
    c.flatten()
    return c

if __name__ == "__main__":
    # c = bend_euler(radius=100, angle=30)
    c = bend_euler_s(radius=100, angle=30)
    c.draw_ports()
    c.show()