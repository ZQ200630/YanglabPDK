import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def bend_bezier(control_points=[[0.0, 0.0], [5.0, 0.0], [50, 5], [100.0, 20]], npoints=201, with_manhattan_facing_angles=True, start_angle=0, end_angle=0, width=1, buffer=3) -> gf.Component:
    """Returns Bezier bend.

    Args:
        control_points: list of points.
        npoints: number of points varying between 0 and 1.
        with_manhattan_facing_angles: bool.
        start_angle: optional start angle in deg.
        end_angle: optional end angle in deg.
        width: width to use. Defaults to cross_section.width.
        buffer: buffer width for positive tone resist (um)
    """
    return Utils.pos_neg_seperate(gf.components.bezier(control_points=control_points, npoints=npoints, with_manhattan_facing_angles=with_manhattan_facing_angles,start_angle=start_angle, end_angle=end_angle, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

if __name__ == "__main__":
    c = bend_bezier()
    c.show()