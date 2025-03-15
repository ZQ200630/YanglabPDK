import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections
from YanglabPDK.components.bends.bend_circular import bend_circular
from YanglabPDK.components.bends.bend_euler import bend_euler
from YanglabPDK.components.bends.bend_bezier import bend_bezier
from YanglabPDK.components.waveguides.straight import straight
from YanglabPDK.components.tapers.taper import taper

@gf.cell
def coupler_symmetric(gap = 0.234, dy = 4.0, dx = 10.0, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler_symmetric(gap=gap, dy=dy, dx=dx, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))


@gf.cell
def coupler(gap = 0.236, length = 20.0, dy = 4.0, dx = 10.0, width=1, buffer=3):
    return Utils.pos_neg_seperate(gf.components.coupler(gap=gap, length=length, dy=dy, dx=dx, cross_section=Sections.pos_neg_resist(width=width, buffer=buffer)))

@gf.cell
def coupler90(gap=0.2, radius=100.0, width=1, buffer=3):
    c = gf.Component()

    bend90 = bend_euler(radius=radius, angle=90, width=width, buffer=buffer)
    bend_ref = c << bend90
    straight_component = straight(length=bend90.ports["o2"].center[0] - bend90.ports["o1"].center[0], width=width, buffer=buffer)

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




