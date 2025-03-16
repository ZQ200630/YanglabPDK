import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK.components.bends.bend_circular import bend_circular
from YanglabPDK.components.bends.bend_euler import bend_euler
from YanglabPDK.components.waveguides.straight import straight

@gf.cell
def coupler90euler(
    gap: float = 0.2,
    radius: float | None = None,
    p: float = 0.5,
    width: float = 1,
    buffer: float = 3
) -> gf.Component:
    r"""Straight coupled to a bend.

    Args:
        gap: um.
        radius: um.
        p: proportion of the curve that is an Euler curve.
        straight: for straight.
        width: um.
        buffer: buffer width for positive tone resist (um)

    .. code::

            o3
             |
            /
           /
       o2_/
       o1___o4

    """
    c = gf.Component()

    bend90 = bend_euler(radius=radius, angle=90, p=p, width=width, buffer=buffer)
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
def coupler90circular(
    gap: float = 0.2,
    radius: float | None = None,
    width: float = 1,
    buffer: float = 3
) -> gf.Component:
    r"""Straight coupled to a bend.

    Args:
        gap: um.
        radius: um.
        straight: for straight.
        width: um.
        buffer: buffer width for positive tone resist (um)

    .. code::

            o3
             |
            /
           /
       o2_/
       o1___o4

    """
    c = gf.Component()

    bend90 = bend_circular(radius=radius, angle=90, width=width, buffer=buffer)
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
def coupler90circular_asymmetric(
    gap: float = 0.2,
    radius: float | None = None,
    width_wg: float = 1,
    width_bend: float = 1,
    buffer: float = 3
) -> gf.Component:
    r"""Straight coupled to a bend.

    Args:
        gap: um.
        radius: um.
        straight: for straight.
        width_wg: width of bus waveguide um.
        width_bend: width of bend um.
        buffer: buffer width for positive tone resist (um)

    .. code::

            o3
             |
            /
           /
       o2_/
       o1___o4

    """
    c = gf.Component()

    bend90 = bend_circular(radius=radius, angle=90, width=width_bend, buffer=buffer)
    bend_ref = c << bend90
    straight_component = straight(length=bend90.ports["o2"].center[0] - bend90.ports["o1"].center[0], width=width_wg, buffer=buffer)

    wg_ref = c << straight_component

    pbw = bend_ref.ports["o1"]
    bend_ref.movey(pbw.center[1] + gap + (width_wg + width_bend) / 2)

    c.add_ports(wg_ref.ports, prefix="wg")
    c.add_ports(bend_ref.ports, prefix="bend")
    c.auto_rename_ports()
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    # c = coupler90circular(gap=0.2, radius=100.0, width=1, buffer=3)
    # c = coupler90euler(gap=0.2, radius=100.0, width=1, buffer=3)
    c = coupler90circular_asymmetric(gap=0.2, radius=100.0, width_wg=1, width_bend=2, buffer=3)
    c.draw_ports()
    c.show()