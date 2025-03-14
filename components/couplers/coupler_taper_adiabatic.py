import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections
from YanglabPDK.components.tapers.taper import taper

@gf.cell
def taper_adiabatic_coupler(width1 = 1, width2 = 1, length = 10, gap = 0.3, extend=5, buffer=3):
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

if __name__ == "__main__":
    c = taper_adiabatic_coupler(width1=0.5, width2=1, length=100, gap=0.4)
    c.draw_ports()
    c.show()