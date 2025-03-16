import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK.components.bends.bend_circular import bend_circular
from YanglabPDK.components.bends.bend_euler import bend_euler
from YanglabPDK.components.couplers.coupler_bent import coupler_bent
from YanglabPDK.components.waveguides.straight import straight
from YanglabPDK.components.couplers.coupler90 import coupler90circular_asymmetric
from YanglabPDK.components.couplers.coupler_straight_asymmetric import coupler_straight_asymmetric
from YanglabPDK.components.waveguides.straight import straight



@gf.cell
def coupler_halfring(
    gap: float = 0.2,
    radius: float = 5.0,
    length_x: float = 0,
    width_wg: float = 1,
    width_bend: float = 1,
    buffer: float = 3,
    length_extension_left: float = 20,
    length_extension_right: float = 20
) -> gf.Component:
    r"""Coupler for ring.

    Args:
        gap: spacing between parallel coupled straight waveguides.
        radius: of the bends.
        length_x: length of the parallel coupled straight waveguides.
        width_wg: width of the waveguides.
        width_bend: width of the bends.
        buffer: buffer width for positive tone resist (um)
        length_extension_left: left to extension comparing to center of the ring.
        length_extension_right: right to extension comparing to center of the ring.

    .. code::

          o2            o3
           |             |
            \           /
             \         /
           ---=========---
        o1    length_x   o4

    """
    c = gf.Component()
    gap = gf.snap.snap_to_grid(gap, grid_factor=2)

    # define subcells
    coupler90_component = coupler90circular_asymmetric(
        gap=gap,
        radius=radius,
        width_wg=width_wg,
        width_bend=width_bend,
        buffer=buffer,
    )

    coupler_straight_component = coupler_straight_asymmetric(
        gap=gap,
        length=length_x,
        width_bot=width_wg,
        width_top=width_bend,
        buffer=buffer
    )

    # add references to subcells
    cbl = c << coupler90_component
    cbr = c << coupler90_component
    cs = c << coupler_straight_component

    # connect references
    cs.connect(port="o4", other=cbr.ports["o1"])
    cbl.connect(port="o2", other=cs.ports["o2"], mirror=True)

    s1 = c << straight(length=length_extension_left-length_x/2, width=width_wg, buffer=buffer)
    s2 = c << straight(length=length_extension_right-length_x/2, width=width_wg, buffer=buffer)

    s1.connect("o2", cbl.ports["o4"])
    s2.connect("o1", cbr.ports["o4"])

    c.add_port("o1", port=s1.ports["o1"])
    c.add_port("o2", port=cbl.ports["o3"])
    c.add_port("o3", port=cbr.ports["o3"])
    c.add_port("o4", port=s2.ports["o2"])

    c.add_ports(
        gf.port.select_ports_list(ports=cbl.ports, port_type="electrical"), prefix="cbl"
    )
    c.add_ports(
        gf.port.select_ports_list(ports=cbr.ports, port_type="electrical"), prefix="cbr"
    )
    c.auto_rename_ports()
    c.flatten()
    return Utils.pos_neg_seperate(c)

@gf.cell
def coupler_halfring_pulley(
    gap: float = 0.2,
    radius: float = 5.0,
    length_x: float = 0,
    width_wg: float = 1,
    width_bend: float = 1,
    covered_angle: float = 45,
    buffer: float = 3,
    length_extension_left: float = 20,
    length_extension_right: float = 20
) -> gf.Component:
    r"""Coupler for ring.

    Args:
        gap: spacing between parallel coupled straight waveguides.
        radius: of the bends.
        length_x: length of the parallel coupled straight waveguides.
        width_wg: width of the waveguides.
        width_bend: width of the bends.
        buffer: buffer width for positive tone resist (um)
        length_extension_left: left to extension comparing to center of the ring.
        length_extension_right: right to extension comparing to center of the ring.

    .. code::

          o2            o3
           |             |
            \           /
             \         /
           ---=========---
        o1    length_x   o4

    """
    c = gf.Component()
    gap = gf.snap.snap_to_grid(gap, grid_factor=2)

    # add references to subcells
    cbl = c << coupler_bent(
        coupler_gap=gap,
        radius=radius,
        width_outer=width_wg,
        width_inner=width_bend,
        buffer=buffer,
        coupling_angle_coverage=covered_angle
    ).copy()
    cbr = c << coupler_bent(
        coupler_gap=gap,
        radius=radius,
        width_outer=width_wg,
        width_inner=width_bend,
        buffer=buffer,
        coupling_angle_coverage=covered_angle
    ).copy()
    cs = c << coupler_straight_asymmetric(
        gap=gap,
        length=length_x,
        width_bot=width_wg,
        width_top=width_bend,
        buffer=buffer
    )

    # connect references
    cs.connect(port="o4", other=cbr.ports["o1"])
    cbl.connect(port="o2", other=cs.ports["o2"], mirror=True)

    # Calculate the distance between cbl port and cbr port

    distance = abs(cbl.ports["o3"].x - cbl.ports["o2"].x)

    s1 = c << straight(length=length_extension_left-length_x/2 - distance, width=width_wg, buffer=buffer)
    s2 = c << straight(length=length_extension_right-length_x/2 - distance, width=width_wg, buffer=buffer)

    s1.connect("o2", cbl.ports["o3"])
    s2.connect("o1", cbr.ports["o3"])

    c.add_port("o1", port=s1.ports["o1"])
    c.add_port("o2", port=cbl.ports["o4"])
    c.add_port("o3", port=cbr.ports["o4"])
    c.add_port("o4", port=s2.ports["o2"])

    c.add_ports(
        gf.port.select_ports_list(ports=cbl.ports, port_type="electrical"), prefix="cbl"
    )
    c.add_ports(
        gf.port.select_ports_list(ports=cbr.ports, port_type="electrical"), prefix="cbr"
    )
    c.auto_rename_ports()
    c.flatten()
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    # c = coupler_halfring(radius=300, length_extension_left=500, length_extension_right=500)
    c = coupler_halfring_pulley(radius=300, width_bend=2, length_extension_left=500, length_extension_right=500)
    c.draw_ports()
    c.show()