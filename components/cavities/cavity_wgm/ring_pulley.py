import gdsfactory as gf

import YanglabPDK.YanglabUtils as Utils

from YanglabPDK.components.bends.bend_circular import bend_circular
from YanglabPDK.components.couplers.coupler_ring import coupler_halfring_pulley
from YanglabPDK.components.waveguides.straight import straight

@gf.cell
def ring_single_pulley(
    radius: float = 100,
    gap: float = 0.2,
    coupling_angle_coverage: float = 90,
    length_x: float = 0.6,
    length_y: float = 0.6,
    width_inner: float = 1,
    width_outer: float = 1,
    buffer: float = 3,
    length_extension_left: float = 500,
    length_extension_right: float = 500
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

    cb = c << coupler_halfring_pulley(
        gap=gap,
        radius=radius,
        covered_angle=coupling_angle_coverage,
        length_x=length_x,
        width_wg=width_inner,
        width_bend=width_outer,
        buffer=buffer,
        length_extension_left=length_extension_left,
        length_extension_right=length_extension_right
    )

    sx = straight(length=length_x, width=width_inner, buffer=buffer)
    sy = straight(length=length_y, width=width_inner, buffer=buffer)

    b = bend_circular(radius=radius, width=width_inner, buffer=buffer)
    sl = c << sy
    sr = c << sy
    bl = c << b
    br = c << b
    st = c << sx

    sl.connect(port="o1", other=cb.ports["o2"])
    bl.connect(port="o2", other=sl.ports["o2"])
    st.connect(port="o2", other=bl.ports["o1"])
    br.connect(port="o2", other=st.ports["o1"])
    sr.connect(port="o1", other=br.ports["o1"])
    sr.connect(port="o2", other=cb.ports["o3"])

    c.add_port("o2", port=cb.ports["o4"])
    c.add_port("o1", port=cb.ports["o1"])
    return Utils.pos_neg_seperate(c)

ring_pulley = ring_single_pulley(length_x=0, length_y=0)

if __name__ == "__main__":
    c = ring_pulley(radius=100, length_x=50, length_y=50)
    c.show()