import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.components.bend import bend_euler_s
from yanglab_pdk.components.mmi import mmi2x2
from yanglab_pdk.YanglabLayerStack import LAYER


@gf.cell
def mmi_coupler(length_mmi=125):
    c = gf.Component()
    # ht1 = c << Repeat.straight_heater_metal_undercut()
    # wg1 = c << Repeat.straight()
    coupler_1 = c << bend_euler_s(angle=-45, radius=100)
    coupler_2 = c << bend_euler_s(angle=45, radius=100)
    # ht2 = c << Repeat.straight_heater_metal_undercut()
    # wg2 = c << Repeat.straight()
    coupler_3 = c << bend_euler_s(angle=45, radius=100)
    coupler_4 = c << bend_euler_s(angle=-45, radius=100)
    mmi2x2_1 = c << mmi2x2(length_mmi=length_mmi)
    # mmi2x2_2 = c << mmi2x2()
    # print(mmi2x2_1.ports.keys())
    coupler_1.connect("o1", mmi2x2_1.ports["o2"])
    coupler_2.connect("o1", mmi2x2_1.ports["o1"])
    coupler_3.connect("o1", mmi2x2_1.ports["o3"])
    coupler_4.connect("o1", mmi2x2_1.ports["o4"])
    c.add_port("o1", port=coupler_1.ports["o2"])
    c.add_port("o2", port=coupler_2.ports["o2"])
    c.add_port("o3", port=coupler_3.ports["o2"])
    c.add_port("o4", port=coupler_4.ports["o2"])
    return c