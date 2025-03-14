import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.YanglabLayerStack import LAYER


@gf.cell
def spiral_double(
    min_bend_radius: float | None = None,
    separation: float = 2.0,
    number_of_loops: float = 3,
    npoints: int = 1000,
    width = 1,
    buffer = 3):
    return Utils.pos_neg_seperate(gf.components.spiral_double(min_bend_radius=min_bend_radius, separation=separation, number_of_loops=number_of_loops, npoints=npoints, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))