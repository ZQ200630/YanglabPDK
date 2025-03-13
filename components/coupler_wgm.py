import gdsfactory as gf
from yanglab_pdk.components.bend import bend_coupler
from yanglab_pdk.components.basic import straight
from yanglab_pdk.YanglabUtils import pos_neg_seperate

@gf.cell
def coupler_ring_bend(
    radius: float = 100,
    coupler_gap: float = 0.2,
    coupling_angle_coverage: float = 90.0,
    length_x: float = 0.0,
    width_inner: float = 1,
    width_outer: float = 1,
    buffer: float = 3
) -> gf.Component:
    r"""Two back-to-back coupler_bend.

    Args:
        radius: um.
        gap: um.
        angle_inner: of the inner bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
        angle_outer: of the outer bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
        bend: for bend.
        length_x: horizontal straight length.
        cross_section: cross_section.
        cross_section_inner: spec inner bend.
        cross_section_outer: spec outer bend.
        kwargs:
    """
    c = gf.Component()
    cp = bend_coupler(radius=radius, coupler_gap=coupler_gap, coupling_angle_coverage=coupling_angle_coverage, width_inner=width_inner, width_outer=width_outer, buffer=3)

    sin = straight(length=length_x, width=width_inner, buffer=buffer)

    sout = straight(length=length_x, width=width_outer, buffer=buffer)

    coupler_right = c << cp
    coupler_left = c << cp.mirror()
    straight_inner = c << sin
    straight_inner.movex(-length_x / 2)
    straight_outer = c << sout
    straight_outer.movex(-length_x / 2)

    coupler_left.connect("o1", straight_outer.ports["o1"])
    straight_inner.connect("o1", coupler_left.ports["o2"])
    coupler_right.connect("o2", straight_inner.ports["o2"])
    straight_outer.connect("o2", coupler_right.ports["o1"])

    c.absorb(coupler_right)
    c.absorb(coupler_left)
    c.absorb(straight_inner)
    c.absorb(straight_outer)

    c.add_port("o1", port=coupler_left.ports["o3"])
    c.add_port("o2", port=coupler_left.ports["o4"])
    c.add_port("o4", port=coupler_right.ports["o3"])
    c.add_port("o3", port=coupler_right.ports["o4"])
    return pos_neg_seperate(c)