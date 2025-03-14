import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def straight(length=10, width=1, buffer=3) -> gf.Component:
    """Returns a Straight waveguide.

    Args:
        length: straight length (um).
        width: width of the waveguide. 
        buffer: buffer width for positive tone resist (um)
    .. code::
        --------------------
        o1 -------------- o2
        --------------------
                length
    """
    return Utils.pos_neg_seperate(gf.components.straight(length=length, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

if __name__ == "__main__":
    c = straight()
    c.show()