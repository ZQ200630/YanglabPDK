import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def spiral_double(
    min_bend_radius: float | None = None,
    separation: float = 2.0,
    number_of_loops: float = 3,
    npoints: int = 1000,
    width: float = 1,
    buffer: float = 3):
    """Returns a spiral double (spiral in, and then out).

    Args:
        min_bend_radius: inner radius of the spiral.
        separation: separation between the loops.
        number_of_loops: number of loops per spiral.
        npoints: points for the spiral.
        width: waveguide width in um.
        buffer: buffer.
    """
    return Utils.pos_neg_seperate(gf.components.spiral_double(min_bend_radius=min_bend_radius, separation=separation, number_of_loops=number_of_loops, npoints=npoints, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

if __name__ == "__main__":
    c = spiral_double(min_bend_radius=10, separation=2.0, number_of_loops=3, npoints=1000, width=1, buffer=3)
    c.show()