import gdsfactory as gf

import YanglabPDK.YanglabUtils as Utils
import YanglabPDK.YanglabSections as Sections

from YanglabPDK.components.couplers.coupler_ring import coupler_halfring
from YanglabPDK.components.bends.bend_circular import bend_circular
from YanglabPDK.components.waveguides.straight import straight

from functools import partial

@gf.cell
def ring_single(
    gap: float = 0.2,
    radius: float = 10.0,
    length_x: float = 4.0,
    length_y: float = 0.6,
    width_wg: float = 1,
    width_bend: float = 1,
    buffer: float = 3,
    length_extension_left: float = 500,
    length_extension_right: float = 500
) -> gf.Component:
    """Returns a single ring.

    ring coupler (cb: bottom) connects to two vertical straights (sl: left, sr: right),
    two bends (bl, br) and horizontal straight (wg: top)

    Args:
        gap: gap between for coupler.
        radius: for the bend and coupler.
        length_x: ring coupler length.
        length_y: vertical straight length.

    .. code::

                    xxxxxxxxxxxxx
                xxxxx           xxxx
              xxx                   xxx
            xxx                       xxx
           xx                           xxx
           x                             xxx
          xx                              xx▲
          xx                              xx│length_y
          xx                              xx▼
          xx                             xx
           xx          length_x          x
            xx     ◄───────────────►    x
             xx                       xxx
               xx                   xxx
                xxx──────▲─────────xxx
                         │gap
                 o1──────▼─────────o2
    """
    if length_y < 0:
        raise ValueError(f"length_y={length_y} must be >= 0")

    if length_x < 0:
        raise ValueError(f"length_x={length_x} must be >= 0")

    c = gf.Component()

    cb = c << coupler_halfring(
        gap=gap,
        radius=radius,
        length_x=length_x,
        width_wg=width_wg,
        width_bend=width_bend,
        buffer=buffer,
        length_extension_left=length_extension_left,
        length_extension_right=length_extension_right
    )

    sl = c << straight(length=length_y, width=width_bend, buffer=buffer)
    sr = c << straight(length=length_y, width=width_bend, buffer=buffer)
    st = c << straight(length=length_x, width=width_bend, buffer=buffer)
    bl = c << bend_circular(radius=radius, width=width_bend, buffer=buffer)
    br = c << bend_circular(radius=radius, width=width_bend, buffer=buffer)

    sl.connect(port="o1", other=cb.ports["o2"])
    bl.connect(port="o2", other=sl.ports["o2"])
    st.connect(port="o2", other=bl.ports["o1"])
    br.connect(port="o2", other=st.ports["o1"])
    sr.connect(port="o1", other=br.ports["o1"])
    sr.connect(port="o2", other=cb.ports["o3"])

    c.add_port("o2", port=cb.ports["o4"])
    c.add_port("o1", port=cb.ports["o1"])
    return Utils.pos_neg_seperate(c)

ring_circle = partial(ring_single, length_x=0, length_y=0)

if __name__ == "__main__":
    c = ring_single(length_x=100, length_y=0, radius=40)
    # c = ring_circle(width_wg = 5, length_extension_left = 500, length_extension_right = 500)
    c.show()