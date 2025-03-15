import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK.components.bends.bend_circular import bend_circular
from YanglabPDK.components.bends.bend_euler import bend_euler

@gf.cell
def bend_coupler(
    radius: float = 100,
    coupler_gap: float = 0.2,
    coupling_angle_coverage: float = 120.0,
    width_inner: float = 1,
    width_outer: float = 1,
    buffer: float = 3
) -> gf.Component:
    r"""Compact curved coupler with bezier escape.

    TODO: fix for euler bends.

    Args:
        radius: um.
        gap: um.
        angle_inner: of the inner bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
        angle_outer: of the outer bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
        bend: for bend.
        cross_section: cross_section.
        cross_section_inner: spec inner bend.
        cross_section_outer: spec outer bend.

    .. code::

            r   4
            |   |
            |  / ___3
            | / /
        2____/ /
        1_____/
    """
    c = gf.Component(name='bend_coupler')

    angle_inner = 90
    angle_outer = coupling_angle_coverage / 2
    gap = coupler_gap

    width = width_outer / 2 + width_inner / 2
    spacing = gap + width

    bend90_inner_right = bend_circular(radius=radius, angle=angle_inner, width=width_inner, buffer=buffer)
    bend_outer_right = bend_circular(radius=radius + spacing, angle=angle_outer, width=width_outer, buffer=buffer)

    bend_inner_ref = c << bend90_inner_right
    bend_outer_ref = c << bend_outer_right

    output = bend_euler(radius=radius, angle=angle_outer, width=width_outer, buffer=buffer)
    output.locked = False
    output = output.mirror()

    output_ref = c << output
    output_ref.connect("o2", bend_outer_ref.ports["o2"])

    pbw = bend_inner_ref.ports["o1"]
    bend_inner_ref.movey(pbw.center[1] + spacing)

    c.add_port("o1", port=bend_outer_ref.ports["o1"])
    c.add_port("o2", port=bend_inner_ref.ports["o1"])
    c.add_port("o3", port=output_ref.ports["o1"])
    c.add_port("o4", port=bend_inner_ref.ports["o2"])

    c.flatten()
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    c = bend_coupler()
    c.draw_ports()
    c.show()