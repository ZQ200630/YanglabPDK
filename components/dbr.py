import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
from yanglab_pdk.YanglabLayerStack import LAYER

@gf.cell
def dbr(w1=0.475, w2=0.525, l1=0.159, l2=0.159, n=10, buffer=3):
    component = gf.components.dbr(w1=w1, w2=w2, l1=l1, l2=l2, n=n)
    component.remap_layers(layermap={LAYER.WG: LAYER.NR})
    c = gf.Component()
    dbr = c << component
    bbox = c << gf.components.bbox(bbox=[[component.xmin, component.ymin], [component.xmax, component.ymax]], layer=LAYER.PR, top=buffer, bottom=buffer)
    bbox.center = dbr.center
    c.name = component.name
    c.ports = component.ports
    c.info = component.info
    return Utils.pos_neg_seperate(c)