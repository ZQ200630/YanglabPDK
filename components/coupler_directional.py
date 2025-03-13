import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
import yanglab_pdk.components.bend as bend
import yanglab_pdk.components.basic as basic
import yanglab_pdk.components.taper as taper
from yanglab_pdk.YanglabLayerStack import LAYER

@gf.cell
def coupler_symmetric(gap = 0.234, dy = 4.0, dx = 10.0, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler_symmetric(gap=gap, dy=dy, dx=dx, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def coupler_straight(length=10.0, gap=0.27, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler_straight(length=length, gap=gap, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def coupler(gap = 0.236, length = 20.0, dy = 4.0, dx = 10.0, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler(gap=gap, length=length, dy=dy, dx=dx, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def coupler90(gap=0.2, radius=100.0, width=1, buffer=3):
    c = gf.Component()

    bend90 = bend.bend_euler(radius=radius, angle=90, width=width, buffer=buffer)
    bend_ref = c << bend90
    straight_component = basic.straight(length=bend90.ports["o2"].center[0] - bend90.ports["o1"].center[0], width=width, buffer=buffer)

    wg_ref = c << straight_component

    pbw = bend_ref.ports["o1"]
    bend_ref.movey(pbw.center[1] + gap + width)

    c.add_ports(wg_ref.ports, prefix="wg")
    c.add_ports(bend_ref.ports, prefix="bend")
    c.auto_rename_ports()
    return Utils.pos_neg_seperate(c)


@gf.cell
def coupler90bend(radius=100.0, gap=0.2, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler90bend(radius=radius, gap=gap, cross_section_inner=Sections.pos_neg_resist(width=width, buffer=buffer), cross_section_outer=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def coupler90circular(gap=0.2, radius=100.0, width=1, buffer=3):
    c = gf.Component()

    bend90 = bend.bend_circular(radius=radius, angle=90, width=width, buffer=buffer)
    bend_ref = c << bend90
    straight_component = basic.straight(length=bend90.ports["o2"].center[0] - bend90.ports["o1"].center[0], width=width, buffer=buffer)

    wg_ref = c << straight_component

    pbw = bend_ref.ports["o1"]
    bend_ref.movey(pbw.center[1] + gap + width)

    c.add_ports(wg_ref.ports, prefix="wg")
    c.add_ports(bend_ref.ports, prefix="bend")
    c.auto_rename_ports()
    return Utils.pos_neg_seperate(c)

@gf.cell
def coupler_adiabatic(length1=20.0, length2=50.0, length3=30.0, wg_sep=1.0, input_wg_sep=20, output_wg_sep=20, dw=0.1, width=1, buffer=3):
    control_points_input_top = [
        (0, 0),
        (length1 / 2.0, 0),
        (length1 / 2.0, -input_wg_sep / 2.0 + wg_sep / 2.0),
        (length1, -input_wg_sep / 2.0 + wg_sep / 2.0),
    ]

    control_points_input_bottom = [
        (0, -input_wg_sep),
        (length1 / 2.0, -input_wg_sep),
        (length1 / 2.0, -input_wg_sep / 2.0 - wg_sep / 2.0),
        (length1, -input_wg_sep / 2.0 - wg_sep / 2.0),
    ]

    control_points_output_top = [
        (length1 + length2, -input_wg_sep / 2.0 + wg_sep / 2.0),
        (
            length1 + length2 + length3 / 2.0,
            -input_wg_sep / 2.0 + wg_sep / 2.0,
        ),
        (
            length1 + length2 + length3 / 2.0,
            -input_wg_sep / 2.0 + output_wg_sep / 2.0,
        ),
        (
            length1 + length2 + length3,
            -input_wg_sep / 2.0 + output_wg_sep / 2.0,
        ),
    ]

    c = gf.Component()

    width_top = width + dw
    width_bot = width - dw

    coupler = c << coupler_straight(length=length2, width=width, buffer=buffer)

    taper_top = c << taper.taper(length=length1, width1=width, width2=width_top, buffer=buffer)
    taper_bot = c << taper.taper(length=length1, width1=width, width2=width_bot, buffer=buffer)

    taper_bot.connect("o1", coupler.ports["o1"])
    taper_top.connect("o1", coupler.ports["o2"])

    sbend_left_top = c << bend.bend_bezier(
        control_points=control_points_input_top, width=width_top, buffer=buffer
    )
    sbend_left_bot = c << bend.bend_bezier(
        control_points=control_points_input_bottom, width=width_bot, buffer=buffer
    )

    sbend_left_top.connect("o2", taper_top.ports["o2"])
    sbend_left_bot.connect("o2", taper_bot.ports["o2"])

    sbend_right = bend.bend_bezier(control_points=control_points_output_top, width=width, buffer=buffer)
    sbend_right_top = c << sbend_right
    sbend_right_bot = c << sbend_right
    sbend_right_bot.mirror()

    sbend_right_top.connect("o1", coupler.ports["o3"])
    sbend_right_bot.connect("o1", coupler.ports["o4"])

    c.add_port("o1", port=sbend_left_bot.ports["o1"])
    c.add_port("o2", port=sbend_left_top.ports["o1"])
    c.add_port("o3", port=sbend_right_top.ports["o2"])
    c.add_port("o4", port=sbend_right_bot.ports["o2"])
    return Utils.pos_neg_seperate(c)

@gf.cell
def coupler_asymmetric(gap=0.234, dy=2.5, dx=10.0, coupling_angle_coverage: float = 120.0, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler_asymmetric(gap=gap, dy=dy, dx=dx, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def coupler_bend(radius=100.0, coupler_gap=0.2, coupling_angle_coverage=120.0, width=1, buffer=3):
    c = gf.Component()

    angle_inner = 90
    angle_outer = coupling_angle_coverage / 2
    gap = coupler_gap

    spacing = gap + width


    bend90_inner_right = bend.bend_circular(radius=radius, angle=angle_inner, width=width, buffer=buffer)


    bend_outer_right = bend.bend_circular(radius=radius + spacing, angle=angle_outer, width=width, buffer=buffer)
    
    bend_inner_ref = c << bend90_inner_right
    bend_outer_ref = c << bend_outer_right

    output = bend.bend_euler(radius=radius + spacing, angle=angle_outer, p=0.5, width=width, buffer=buffer).mirror()

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