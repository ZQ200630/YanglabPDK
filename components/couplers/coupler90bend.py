import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def coupler90bend(
    radius: float = 100.0,
    gap: float = 0.2,
    width_outter: float = 1,
    width_inner: float = 1,
    buffer: float = 3
) -> gf.Component:
    r"""Returns 2 coupled bends.

    Args:
        radius: um.
        gap: um.
        bend: for bend.
        width_outter: outter bend width um.
        width_inner: inner bend width um.
        buffer: buffer width for positive tone resist (um)


    .. code::

            r   3 4
            |   | |
            |  / /
            | / /
        2____/ /
        1_____/

    """
    return Utils.pos_neg_seperate(
        gf.components.coupler90bend(
            radius=radius,
            gap=gap,
            cross_section_inner=Sections.pos_neg_resist(width=width_inner, buffer=buffer),
            cross_section_outer=Sections.pos_neg_resist(width=width_outter, buffer=buffer)
        )
    )

if __name__ == "__main__":
    c = coupler90bend(radius=100.0, gap=0.2, width_inner=1, width_outter=2, buffer=3)
    c.show()