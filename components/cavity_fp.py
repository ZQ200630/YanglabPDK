import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.components.dbr import dbr
from yanglab_pdk.components.coupler_directional import coupler
from yanglab_pdk.YanglabLayerStack import LAYER

@gf.cell
def cavity(dbr=dbr(w1=1, w2=0.5, n=20), coupler=coupler(dy=8, dx=20)):
    c = gf.Component()
    c.component = dbr
    cr = c << coupler
    ml = c << dbr
    mr = c << dbr

    ml.connect("o1", destination=cr.ports["o2"])
    mr.connect("o1", destination=cr.ports["o3"])
    c.add_port("o1", port=cr.ports["o1"])
    c.add_port("o2", port=cr.ports["o4"])
    c.copy_child_info(dbr)
    return c