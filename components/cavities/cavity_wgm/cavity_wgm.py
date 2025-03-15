import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.components import bend as Bend
from yanglab_pdk.components import coupler_wgm as Coupler_WGM
from yanglab_pdk.components import basic as Basic
from functools import partial


# Bend can be bend_euler or bend_circular
@gf.cell
def coupler_ring(gap=0.2, radius=5, length_x=4, bend='bend_euler', length_extension=3, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler_ring(gap = gap, radius=radius, length_x=length_x, bend=bend, length_extension=length_extension, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def ring_single(gap=0.2, radius=5, length_x=4, length_y=4, bend=gf.components.bend_euler, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.ring_single(gap=gap, radius=radius, length_x=length_x, length_y=length_y, bend=bend, bend_coupler=bend, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

ring_circle = partial(ring_single, radius=100, gap=0.5, length_x=0, length_y=0, bend=gf.components.bend_circular)

@gf.cell
def ring_single_pulley(
    radius: float = 100,
    gap: float = 0.2,
    coupling_angle_coverage: float = 180.0,
    length_x: float = 0.6,
    length_y: float = 0.6,
    width_inner: float = 1,
    width_outer: float = 1,
    buffer: float = 3
) -> gf.Component:
    r"""Returns ring with curved coupler.

    TODO: enable euler bends.

    Args:
        radius: um.
        gap: um.
        angle_inner: of the inner bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
        angle_outer: of the outer bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
        bend: for bend.
        length_x: horizontal straight length.
        length_y: vertical straight length.
        cross_section: cross_section.
        cross_section_inner: spec inner bend.
        cross_section_outer: spec outer bend.
        kwargs: cross_section settings.
    """
    c = gf.Component()

    cb = c << Coupler_WGM.coupler_ring_bend(radius=radius, coupler_gap=gap, coupling_angle_coverage=coupling_angle_coverage, length_x=length_x, width_inner=width_inner, width_outer=width_outer, buffer=buffer)

    sx = Basic.straight(length=length_x, width=width_inner, buffer=buffer)
    sy = Basic.straight(length=length_y, width=width_inner, buffer=buffer)

    b = Bend.bend_circular(radius=radius, width=width_inner, buffer=buffer)
    sl = c << sy
    sr = c << sy
    bl = c << b
    br = c << b
    st = c << sx

    sl.connect(port="o1", destination=cb.ports["o2"])
    bl.connect(port="o2", destination=sl.ports["o2"])
    st.connect(port="o2", destination=bl.ports["o1"])
    br.connect(port="o2", destination=st.ports["o1"])
    sr.connect(port="o1", destination=br.ports["o1"])
    sr.connect(port="o2", destination=cb.ports["o3"])

    c.add_port("o2", port=cb.ports["o4"])
    c.add_port("o1", port=cb.ports["o1"])
    return Utils.pos_neg_seperate(c)

ring_circle_pulley = partial(ring_single_pulley, radius=100, gap=0.5, length_x=0, length_y=0, width_inner=1, width_outer=1, buffer=3)