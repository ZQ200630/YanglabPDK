import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections


@gf.cell
def coupler_straight(
    length: float = 10.0, 
    gap: float = 0.27, 
    width: float = 1, 
    buffer: float = 3
) -> gf.Component:
    """Coupler_straight with two parallel straights.

    Args:
        length: of straight.
        gap: between straights.
        width: of the straights.
        buffer: buffer.

    .. code::

        o2──────▲─────────o3
                │gap
        o1──────▼─────────o4
    """
    c = gf.components.coupler_straight(length=length, gap=gap, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer))
    c.locked = False
    c.flatten()
    return Utils.pos_neg_seperate(c)

@gf.cell
def coupler(
    gap: float = 0.236, 
    length: float = 20.0, 
    dy: float = 4.0, 
    dx: float = 10.0, 
    width: float = 1, 
    buffer: float = 3
) -> gf.Component:
    r"""Symmetric coupler.

    Args:
        gap: between straights in um.
        length: of coupling region in um.
        dy: port to port vertical spacing in um.
        dx: length of bend in x direction in um.
        cross_section: spec (CrossSection, string or dict).
        allow_min_radius_violation: if True does not check for min bend radius.
        bend: input and output sbend components.

    .. code::

               dx                                 dx
            |------|                           |------|
         o2 ________                           ______o3
                    \                         /           |
                     \        length         /            |
                      ======================= gap         | dy
                     /                       \            |
            ________/                         \_______    |
         o1                                          o4

                        coupler_straight  coupler_symmetric
    """
    c = gf.components.coupler(gap=gap, length=length, dy=dy, dx=dx, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer))
    c.locked = False
    c.flatten()
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    # c = coupler_straight()
    c = coupler()
    c.show()