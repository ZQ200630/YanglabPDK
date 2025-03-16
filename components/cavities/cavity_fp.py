import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections
from YanglabPDK.components.couplers.coupler import coupler
from YanglabPDK.components.filters.dbr import dbr

@gf.cell
def cavity_fp(dbr=dbr(w1=1, w2=0.5, n=20), coupler=coupler(dy=8, dx=20)):
    c = gf.Component()
    c.component = dbr
    cr = c << coupler
    ml = c << dbr
    mr = c << dbr

    ml.connect(port="o1", other=cr.ports["o2"])
    mr.connect(port="o1", other=cr.ports["o3"])
    c.add_port("o1", port=cr.ports["o1"])
    c.add_port("o2", port=cr.ports["o4"])
    c.copy_child_info(dbr)
    return c

if __name__ == "__main__":
    c = cavity_fp()
    c.draw_ports()
    c.show()