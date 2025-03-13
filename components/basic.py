import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.YanglabLayerStack import LAYER
from functools import partial

@gf.cell
def straight(length=10, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.straight(length=length, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))


@gf.cell
def straight_heater_metal_undercut(length=320.0, length_undercut_spacing=6, length_undercut=30.0, length_straight_input=15, with_undercut=True, heater_taper_length=5.0, heater_width=2, undercut_width=3, undercut_gap=3, width=1, buffer=3):
    cross_section = Sections.pos_neg_resist(width=1, buffer=buffer)
    # cross_section = partial(gf.cross_section.strip, width=width, layer=LAYER.WG)
    # cross_section="xs_sc"
    cross_section_heater = partial(gf.cross_section.heater_metal, width=heater_width, layer=LAYER.MT2)
    cross_section_waveguide_heater = partial(gf.cross_section.strip_heater_metal, width=width, layer=LAYER.NR, layer_heater=LAYER.MT2, heater_width=heater_width, sections=Sections.pos_neg_Section_Tuple(width=width, buffer=buffer))
    cross_section_heater_undercut = partial(gf.cross_section.strip_heater_metal_undercut, layer=LAYER.NR, width=width, heater_width=heater_width, trench_gap=undercut_gap, layer_heater=LAYER.MT2, layer_trench=LAYER.DT, trench_width=undercut_width, sections=Sections.pos_neg_Section_Tuple(width=width, buffer=buffer+undercut_gap))
    vs = gf.components.via_stack(size=[11.0, 11.0], layers=[LAYER.MT2, LAYER.MT1], correct_size=True, slot_horizontal=False, slot_vertical=False, vias=[None, None])
    return gf.components.straight_heater_metal_undercut(length=length, length_undercut_spacing=length_undercut_spacing, cross_section=cross_section, cross_section_heater=cross_section_heater, cross_section_waveguide_heater=cross_section_waveguide_heater, cross_section_heater_undercut=cross_section_heater_undercut, length_undercut=length_undercut, length_straight_input=length_straight_input, with_undercut=with_undercut, heater_taper_length=heater_taper_length, via_stack=vs)

