import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.YanglabLayerStack import LAYER

@gf.cell
def taper(length=10.0, width1=1, width2=1, buffer=3):
    port_names=['o1', 'o2']
    port_types=['optical', 'optical']
    with_two_ports=True
    if (width1 <= width2):
        return Utils.pos_neg_seperate(gf.components.taper(length=length, width1=width1, width2=width2, with_two_ports=with_two_ports, port_names=port_names, port_types=port_types, cross_section=Sections.pos_neg_resist(width=width1, buffer=buffer)))
    else:
        port_names.reverse()
        return Utils.pos_neg_seperate(gf.components.taper(length=length, width1=width2, width2=width1, with_two_ports=with_two_ports, port_names=port_names, port_types=port_types, cross_section=Sections.pos_neg_resist(width=width2, buffer=buffer)).rotate(180))

@gf.cell
def taper_two_adiabatic(width1 = 1, width2 = 1, length = 10, gap = 0.3, extend=5, buffer=3):
    c = gf.Component()
    taper1 = c << taper(length=length, width1=width1, width2=width2, buffer=buffer)
    taper2 = c << taper(length=length, width1=width2, width2=width1, buffer=buffer)
    taper1.center = (0, (width1/2+width2/2+gap)/2)
    taper2.center = (0, -(width1/2+width2/2+gap)/2)
    c.add_port("o1", port=taper1.ports["o1"])
    c.add_port("o2", port=taper1.ports["o2"])
    c.add_port("o3", port=taper2.ports["o1"])
    c.add_port("o4", port=taper2.ports["o2"])
    return Utils.pos_neg_seperate(c)