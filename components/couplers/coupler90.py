import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK.components.bends.bend_circular import bend_circular
from YanglabPDK.components.waveguides.straight import straight

@gf.cell
def coupler90euler(
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
        bend: bend spec.
        cross_section: cross_section spec.
        cross_section_bend: optional bend cross_section spec.

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
    return c

@gf.cell
def coupler90circular(gap=0.2, radius=100.0, width=1, buffer=3) -> gf.Component:
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

if __name__ == "__main__":
    c = coupler90circular(gap=0.2, radius=100.0, width=1, buffer=3)
    c.draw_ports()
    c.show()