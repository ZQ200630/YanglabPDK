import gdsfactory as gf
from functools import partial

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections
from YanglabPDK import LAYER as LAYER

@gf.cell
def straight_heater_metal_undercut(length=320.0, length_undercut_spacing=6, length_undercut=30.0, length_straight_input=15, with_undercut=True, heater_taper_length=5.0, heater_width=2, undercut_width=3, undercut_gap=3, width=1, buffer=3) -> gf.Component:
    """Returns a thermal phase shifter.

    dimensions from https://doi.org/10.1364/OE.27.010456

    Args:
        length: of the waveguide.
        length_undercut_spacing: from undercut regions.
        length_undercut: length of each undercut section.
        length_straight_input: from input port to where trenches start.
        with_undercut: isolation trenches for higher efficiency.
        heater_taper_length: minimizes current concentrations from heater to via_stack.
        heater_width: width of the heater.
        undercut_width: width of the undercut.
        undercut_gap: gap between the undercut and the waveguide.
        width: width of the waveguide.
        buffer: buffer width for positive tone resist.
    """
    cross_section = Sections.pos_neg_resist(width=1, buffer=buffer)
    cross_section_heater = partial(gf.cross_section.heater_metal, width=heater_width, layer=LAYER.MT2)
    cross_section_waveguide_heater = partial(gf.cross_section.strip_heater_metal, width=width, layer=LAYER.NR, layer_heater=LAYER.MT2, heater_width=heater_width, sections=Sections.pos_neg_Section_Tuple(width=width, buffer=buffer))
    cross_section_heater_undercut = partial(gf.cross_section.strip_heater_metal_undercut, layer=LAYER.NR, width=width, heater_width=heater_width, trench_gap=undercut_gap, layer_heater=LAYER.MT2, layer_trench=LAYER.DT, trench_width=undercut_width, sections=Sections.pos_neg_Section_Tuple(width=width, buffer=buffer+undercut_gap))
    vs = gf.components.via_stack(size=[11.0, 11.0], layers=[LAYER.MT2, LAYER.MT1], correct_size=True, slot_horizontal=False, slot_vertical=False, vias=[None, None])
    return gf.components.straight_heater_metal_undercut(length=length, length_undercut_spacing=length_undercut_spacing, cross_section=cross_section, cross_section_heater=cross_section_heater, cross_section_waveguide_heater=cross_section_waveguide_heater, cross_section_heater_undercut=cross_section_heater_undercut, length_undercut=length_undercut, length_straight_input=length_straight_input, with_undercut=with_undercut, heater_taper_length=heater_taper_length, via_stack=vs)

if __name__ == "__main__":
    c = straight_heater_metal_undercut()
    # c.draw_ports()
    c.show()