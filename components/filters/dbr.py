import gdsfactory as gf
from gdsfactory.snap import snap_to_grid

from YanglabPDK import LAYER
from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

from YanglabPDK.components.waveguides.straight import straight


period = 318e-3
w0 = 0.5
dw = 100e-3
w1 = w0 - dw / 2
w2 = w0 + dw / 2


@gf.cell
def dbr_cell(
    w1: float = w1,
    w2: float = w2,
    l1: float = period / 2,
    l2: float = period / 2,
    buffer: float = 3,
) -> gf.Component:
    """Distributed Bragg Reflector unit cell.

    Args:
        w1: thin width in um.
        l1: thin length in um.
        w2: thick width in um.
        l2: thick length in um.
        n: number of periods.
        cross_section: cross_section spec.

    .. code::

           l1      l2
        <-----><-------->
                _________
        _______|

          w1       w2
        _______
               |_________
    """
    l1 = snap_to_grid(l1)
    l2 = snap_to_grid(l2)
    w1 = snap_to_grid(w1, 2)
    w2 = snap_to_grid(w2, 2)

    c = gf.Component()
    if w1 > w2:
        c1 = c << straight(length=l1, width=w1, buffer=buffer)
        c2 = c << straight(length=l2, width=w2, buffer=buffer + (w1 - w2) / 2)
    else:
        c1 = c << straight(length=l1, width=w1, buffer=buffer + (w2 - w1) / 2)
        c2 = c << straight(length=l2, width=w2, buffer=buffer)
    c2.connect(port="o1", other=c1.ports["o2"], allow_width_mismatch=True)
    c.add_port("o1", port=c1.ports["o1"])
    c.add_port("o2", port=c2.ports["o2"])
    c.flatten()
    return Utils.pos_neg_seperate(c)


@gf.cell
def dbr(
    w1: float = w1,
    w2: float = w2,
    l1: float = period / 2,
    l2: float = period / 2,
    n: int = 10,
    length: float = 0.1,
    width: float = 1,
    buffer: float = 3,
) -> gf.Component:
    """Distributed Bragg Reflector.

    Args:
        w1: thin width in um.
        w2: thick width in um.
        l1: thin length in um.
        l2: thick length in um.
        n: number of periods.
        width: waveguide width in um.
        length: length of straight.

    .. code::

           l1      l2
        <-----><-------->
                _________
        _______|

          w1       w2       ...  n times
        _______
               |_________
    """
    c = gf.Component()

    s1 = c << straight(length=length, width=width, buffer=buffer)
    s2 = c << straight(length=length, width=width, buffer=buffer)

    buffer_dbr_cell = buffer

    if width > max(w1, w2):
        buffer_dbr_cell = buffer + (width - max(w1, w2)) / 2

    cell = dbr_cell(w1=w1, w2=w2, l1=l1, l2=l2, buffer=buffer_dbr_cell)
    ref = c.add_ref(cell, columns=n, rows=1, column_pitch=l1 + l2)

    s1.connect(port="o1", other=cell.ports["o1"], allow_width_mismatch=True)
    s2.connect(port="o1", other=cell.ports["o2"], allow_width_mismatch=True)
    s2.dxmin = ref.dxmax

    c.add_port("o1", port=s1.ports["o2"])
    return Utils.pos_neg_seperate(c)

# @gf.cell
# def dbr(w1=0.475, w2=0.525, l1=0.159, l2=0.159, n=10, buffer=3):
#     component = gf.components.dbr(w1=w1, w2=w2, l1=l1, l2=l2, n=n)
#     component.locked = False
#     component.flatten()
#     component = Utils.remap_layers(component, LAYER.WG, LAYER.NR)
#     c = gf.Component()
#     dbr = c << component
#     bbox = c << gf.components.bbox(bbox=[[component.xmin, component.ymin], [component.xmax, component.ymax]], layer=LAYER.PR, top=buffer, bottom=buffer)
#     bbox.center = dbr.center
#     c.name = component.name
#     c.ports = component.ports
#     c.info = component.info
#     return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    # c = dbr_cell()
    c = dbr()
    c.show()