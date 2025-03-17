import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections
from YanglabPDK import LAYER
from YanglabPDK.components.tapers.taper import taper
from YanglabPDK.components.waveguides.straight import straight
from YanglabPDK.components.mmis import mmi1x2
from YanglabPDK.components.bends import bend_euler_s

@gf.cell
def mzi_mmi(
    width: float | None = 1,
    width_taper: float = 1.0,
    length_taper: float = 10.0,
    length_mmi: float = 5.5,
    width_mmi: float = 2.5,
    gap_mmi: float = 0.25,
    bend_angle: float = 30,
    straight_length: float = 10.0,
    edge_length: float = 500,
    buffer: float = 3.0,
) -> gf.Component:
    c = gf.Component()
    mmi_left = c << mmi1x2(width=width, width_taper=width_taper, length_taper=length_taper, length_mmi=length_mmi, width_mmi=width_mmi, gap_mmi=gap_mmi, buffer=buffer).copy()
    mmi_right = c << mmi1x2(width=width, width_taper=width_taper, length_taper=length_taper, length_mmi=length_mmi, width_mmi=width_mmi, gap_mmi=gap_mmi, buffer=buffer).copy()
    bend_up_left = c << bend_euler_s(radius=100, angle=bend_angle, p=0.5, width=width, buffer=buffer).copy()
    bend_bottom_left = c << bend_euler_s(radius=100, angle=-bend_angle, p=0.5, width=width, buffer=buffer).copy()
    bend_up_right = c << bend_euler_s(radius=100, angle=-bend_angle, p=0.5, width=width, buffer=buffer).copy()
    bend_bottom_right = c << bend_euler_s(radius=100, angle=bend_angle, p=0.5, width=width, buffer=buffer).copy()
    
    bend_up_left.connect("o2", mmi_left.ports["o2"])
    bend_bottom_left.connect("o2", mmi_left.ports["o3"])
    straight_up = c << straight(length=straight_length, width=width, buffer=buffer)
    straight_bottom = c << straight(length=straight_length, width=width, buffer=buffer)
    straight_up.connect("o1", bend_up_left.ports["o1"])
    straight_bottom.connect("o1", bend_bottom_left.ports["o1"])
    bend_up_right.connect("o2", straight_up.ports["o2"])
    bend_bottom_right.connect("o2", straight_bottom.ports["o2"])
    mmi_right.connect("o3", bend_up_right.ports["o1"])
    text_len_mii = c << gf.components.text(text="L = %.1f um"%(length_mmi), size=10, layer=LAYER.TX)
    text_len_mii.center = (straight_up.x, (straight_up.y + straight_bottom.y)/2)
    straight_edge_left = c << straight(length=edge_length, width=width, buffer=buffer)
    straight_edge_right = c << straight(length=edge_length, width=width, buffer=buffer)
    straight_edge_left.connect("o1", mmi_left.ports["o1"])
    straight_edge_right.connect("o1", mmi_right.ports["o1"])
    c = Utils.pos_neg_seperate(c)
    c.flatten()
    return c

if __name__ == "__main__":
    c = mzi_mmi(width=1.5, width_taper=3.6, width_mmi=10, length_mmi=58, length_taper=50, gap_mmi=1.8, straight_length=1000)
    c.show()