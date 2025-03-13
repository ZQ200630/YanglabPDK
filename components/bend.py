import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.YanglabLayerStack import LAYER

@gf.cell
def bend_circular(radius, angle=90, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.bend_circular(radius=radius, angle=angle, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def bend_euler(radius, angle=90, p=0.5, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.bend_euler(radius=radius, angle=angle, p=p, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def bend_euler_s(radius, angle=90, p=0.5, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.bend_euler_s(radius=radius, angle=angle, p=p, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def bend_bezier(control_points=[[0.0, 0.0], [5.0, 0.0], [5.0, 1.8], [10.0, 1.8]], npoints=201, with_manhattan_facing_angles=True, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.bezier(control_points=control_points, npoints=npoints, with_manhattan_facing_angles=with_manhattan_facing_angles, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def bend_s(size=[10, 10], width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.bend_s(size=size, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def bend_straight_bend(straight_length=10, angle=90, p=0.5, radius=300, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.bend_straight_bend(straight_length=straight_length, angle=angle, p=p, radius=radius, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def bend_coupler(
    radius: float = 100,
    coupler_gap: float = 0.2,
    coupling_angle_coverage: float = 120.0,
    width_inner = 1,
    width_outer = 1,
    buffer = 3
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
    c = gf.Component()

    angle_inner = 90
    angle_outer = coupling_angle_coverage / 2
    gap = coupler_gap

    width = width_outer / 2 + width_inner / 2
    spacing = gap + width

    bend90_inner_right = bend_circular(radius=radius, angle=angle_inner, width=width_inner, buffer=buffer)
    bend_outer_right = bend_circular(radius=radius + spacing, angle=angle_outer, width=width_outer, buffer=buffer)

    bend_inner_ref = c << bend90_inner_right
    bend_outer_ref = c << bend_outer_right

    output = bend_euler(radius=radius, angle=angle_outer, width=width_outer, buffer=buffer).mirror()

    output_ref = c << output
    output_ref.connect("o1", bend_outer_ref.ports["o2"])

    pbw = bend_inner_ref.ports["o1"]
    bend_inner_ref.movey(pbw.center[1] + spacing)

    c.absorb(bend_outer_ref)
    c.absorb(bend_inner_ref)
    c.absorb(output_ref)

    c.add_port("o1", port=bend_outer_ref.ports["o1"])
    c.add_port("o2", port=bend_inner_ref.ports["o1"])
    c.add_port("o3", port=output_ref.ports["o2"])
    c.add_port("o4", port=bend_inner_ref.ports["o2"])
    return Utils.pos_neg_seperate(c)