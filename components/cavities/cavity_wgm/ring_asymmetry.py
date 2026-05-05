import gdsfactory as gf
import YanglabPDK.YanglabUtils as Utils
import YanglabPDK.YanglabSections as Sections
from YanglabPDK import LAYER
from YanglabPDK.components.waveguides.straight import straight
from YanglabPDK.components.tapers import taper
from YanglabPDK.components.metals.heater import microheater_arc_with_teeth

from gdsfactory.snap import snap_to_grid

@gf.cell
def half_ring_asymmetry(radius=100, short_width=0.6, long_width=2, buffer=3):
    c = gf.Component()
    circle_outer = c << gf.components.circle(radius=radius + long_width/2 + buffer, layer=LAYER.PR, angle_resolution=0.1)
    circle_inner = c << gf.components.circle(radius=radius - long_width/2 - buffer, layer=LAYER.PR, angle_resolution=0.1)
    circle_inner.center = (0, 0)
    circle_outer.center = (0, 0)
    # Boolean difference to create the ring
    pr_outer_ring = gf.boolean(
        A=circle_outer,
        B=circle_inner,
        operation="A-B",
        layer=LAYER.PR
    )
    d = gf.Component()
    circle_ring_outer = d << gf.components.circle(radius=radius + long_width/2, layer=LAYER.NR, angle_resolution=0.1)
    ellipse = d << gf.components.ellipse(radii=(radius - long_width/2, radius - short_width + long_width/2), layer=LAYER.NR, angle_resolution=0.1)
    circle_ring_outer.center = (0, 0)
    ellipse.center = (0, 0)
    nr_inner_ring = gf.boolean(
        A=circle_ring_outer,
        B=ellipse,
        operation="A-B",
        layer=LAYER.NR
    )
    comp = gf.Component()
    nr_region = comp << nr_inner_ring
    pr_region = comp << pr_outer_ring
    comp_rec1 = comp << gf.components.rectangle(size=(radius*2.5, radius*2.5), layer=LAYER.PR)
    comp_rec2 = comp << gf.components.rectangle(size=(radius*2.5, radius*2.5), layer=LAYER.NR)
    comp_rec1.x = 0
    comp_rec2.x = 0
    comp_rec1.ymax = 0
    comp_rec2.ymax = 0
    test1 = gf.boolean(
        A=pr_region,
        B=comp_rec1,
        operation="A-B",
        layer=LAYER.PR
    )
    test2 = gf.boolean(
        A=nr_region,
        B=comp_rec2,
        operation="A-B",
        layer=LAYER.NR
    )
    comp_final = gf.Component()
    comp_final << test1
    comp_final << test2
    # Add two ports
    comp_final.add_port(name="o1", center=(radius, 0), width=long_width, orientation=-90, layer=LAYER.NR)
    comp_final.add_port(name="o2", center=(-radius, 0), width=long_width, orientation=-90, layer=LAYER.NR)
    return Utils.pos_neg_seperate(comp_final)

@gf.cell
def ring_asymmetry_only(radius=100, short_width=0.6, long_width=2, racetrack_len=200, buffer=3):
    c = gf.Component()
    half1 = half_ring_asymmetry(radius=radius, short_width=short_width, long_width=long_width, buffer=buffer)
    half2 = half_ring_asymmetry(radius=radius, short_width=short_width, long_width=long_width, buffer=buffer)
    r1 = c << half1
    r2 = c << half2
    s1 = c << straight(length=racetrack_len, width=long_width, buffer=buffer)
    s2 = c << straight(length=racetrack_len, width=long_width, buffer=buffer)
    s1.connect("o1", r1.ports["o1"])
    s2.connect("o1", r1.ports["o2"])
    r2.connect("o1", s2.ports["o2"])
    c.add_port(name="o1", port=r1.ports["o1"])
    c.add_port(name="o2", port=r2.ports["o2"])
    c.info["length"] = 3.14 * radius * 2 + 2 * racetrack_len
    return c

@gf.cell
def ring_asymmetry_only_w_heater(radius=100, short_width=0.6, long_width=2, buffer=3,
                                 w: float = 0.5,                # heater width (um)
    theta0: float = 30,         # start angle (deg)
    theta1: float = 30.0,         # end angle (deg)  (can be < theta0)
    lead_len: float = 3,        # straight lead length at each end (um)
    elef_taper_len: float = 5.0,    # length of taper from lead width to heater width (um)

    # pads
    pad_size: tuple[float, float] = (11, 11),  # (x, y) um

    # teeth (the small rectangles along the arc)
    add_teeth: bool = False,
    tooth_len: float = 3.0,         # tooth extends outward from arc outer edge (um)
    tooth_w: float = 1.2           # tooth width along tangent direction (um)):
):
    c = gf.Component()
    half1 = half_ring_asymmetry(radius=radius, short_width=short_width, long_width=long_width, buffer=buffer)
    half2 = half_ring_asymmetry(radius=radius, short_width=short_width, long_width=long_width, buffer=buffer)
    r1 = c << half1
    r2 = c << half2
    r1.ymin = 0
    r1.x = 0
    r2.connect("o1", r1.ports["o2"])
    heater = c << microheater_arc_with_teeth(R=radius, w=w, theta0=theta0, theta1=theta1, lead_len=lead_len, elef_taper_len=elef_taper_len, pad_size=pad_size, add_teeth=add_teeth, tooth_len=tooth_len, tooth_w=tooth_w)
    c.add_port(name="o1", port=r1.ports["o1"])
    c.add_port(name="o2", port=r2.ports["o2"])
    c.info["length"] = 3.14 * radius * 2
    c.add_port(name="e11", port=heater.ports["e1_0"])
    c.add_port(name="e12", port=heater.ports["e1_180"])
    c.add_port(name="e13", port=heater.ports["e1_270"])
    c.add_port(name="e21", port=heater.ports["e2_0"])
    c.add_port(name="e22", port=heater.ports["e2_180"])
    c.add_port(name="e23", port=heater.ports["e2_270"])
    return c

@gf.cell
def ring_asymmetry(radius=100, short_width=0.6, gap=0.6, wg_width=1, long_width=2, racetrack_len=200, buffer=3):
    c = gf.Component()
    ring = c << ring_asymmetry_only(radius=radius, short_width=short_width, long_width=long_width, racetrack_len=racetrack_len, buffer=buffer)
    bus_wg = c << straight(length=2*radius, width=wg_width, buffer=buffer)
    ring.center = (0, 0)
    bus_wg.center = (0, racetrack_len / 2 + radius + long_width/2 + wg_width/2 + gap)
    c.add_port(name="o1", port=bus_wg.ports["o1"])
    c.add_port(name="o2", port=bus_wg.ports["o2"])
    return Utils.pos_neg_seperate(c)

@gf.cell
def ring_assymmetry_add_drop(radius=100, short_width=0.6, gap=0.6, wg_width=0.8, width=1, long_width=2, racetrack_len=200, buffer=3):
    c = gf.Component()
    ring = c << ring_asymmetry_only(radius=radius, short_width=short_width, long_width=long_width, racetrack_len=racetrack_len, buffer=buffer)
    bus_wg_comp = gf.Component()
    s1 = bus_wg_comp << straight(length=30, width=wg_width, buffer=buffer)
    t1 = bus_wg_comp << taper(width1=wg_width, width2=width, length=radius - 15)
    t2 = bus_wg_comp << taper(width1=width, width2=wg_width, length=radius - 15)
    t1.connect("o1", s1.ports["o1"])
    t2.connect("o2", s1.ports["o2"])
    bus_wg_comp.add_port(name="o1", port=t1.ports["o2"])
    bus_wg_comp.add_port(name="o2", port=t2.ports["o1"])
    bus_wg1 = c << bus_wg_comp
    bus_wg2 = c << bus_wg_comp
    ring.center = (0, 0)
    bus_wg1.center = (0, racetrack_len / 2 + radius + long_width/2 + wg_width/2 + gap)
    bus_wg2.center = (0, - (racetrack_len / 2 + radius + long_width/2 + wg_width/2 + gap))
    c.add_port(name="o1", port=bus_wg1.ports["o1"])
    c.add_port(name="o2", port=bus_wg1.ports["o2"])
    c.add_port(name="o3", port=bus_wg2.ports["o1"])
    c.add_port(name="o4", port=bus_wg2.ports["o2"])
    return Utils.pos_neg_seperate(c)

@gf.cell
def ring_assymmetry_add_drop_w_heater(radius=100, short_width=0.6, gap=0.6, wg_width=0.8, width=1, long_width=2, buffer=3,
                                    w: float = 0.5,                # heater width (um)
    theta0: float = 30,         # start angle (deg)
    theta1: float = 30.0,         # end angle (deg)  (can be < theta0)
    lead_len: float = 3,        # straight lead length at each end (um)
    elef_taper_len: float = 5.0,    # length of taper from lead width to heater width (um)

    # pads
    pad_size: tuple[float, float] = (11, 11),  # (x, y) um

    # teeth (the small rectangles along the arc)
    add_teeth: bool = False,
    tooth_len: float = 3.0,         # tooth extends outward from arc outer edge (um)
    tooth_w: float = 1.2           # tooth width along tangent direction (um)):
    ):
    c = gf.Component()
    ring = c << ring_asymmetry_only_w_heater(radius=radius, short_width=short_width, long_width=long_width, buffer=buffer, w=w, theta0=theta0, theta1=theta1, lead_len=lead_len, elef_taper_len=elef_taper_len, pad_size=pad_size, add_teeth=add_teeth, tooth_len=tooth_len, tooth_w=tooth_w)
    bus_wg_comp = gf.Component()
    s1 = bus_wg_comp << straight(length=30, width=wg_width, buffer=buffer)
    t1 = bus_wg_comp << taper(width1=wg_width, width2=width, length=radius - 15)
    t2 = bus_wg_comp << taper(width1=width, width2=wg_width, length=radius - 15)
    t1.connect("o1", s1.ports["o1"])
    t2.connect("o2", s1.ports["o2"])
    bus_wg_comp.add_port(name="o1", port=t1.ports["o2"])
    bus_wg_comp.add_port(name="o2", port=t2.ports["o1"])
    bus_wg1 = c << bus_wg_comp
    bus_wg2 = c << bus_wg_comp
    # ring.center = (0, 0)
    bus_wg1.center = (0, radius + long_width/2 + wg_width/2 + gap)
    bus_wg2.center = (0, - (radius + long_width/2 + wg_width/2 + gap))
    c.add_port(name="o1", port=bus_wg1.ports["o1"])
    c.add_port(name="o2", port=bus_wg1.ports["o2"])
    c.add_port(name="o3", port=bus_wg2.ports["o1"])
    c.add_port(name="o4", port=bus_wg2.ports["o2"])
    # Add electrical ports
    c.add_port(name="e11", port=ring.ports["e11"])
    c.add_port(name="e12", port=ring.ports["e12"])
    c.add_port(name="e13", port=ring.ports["e13"])
    c.add_port(name="e21", port=ring.ports["e21"])
    c.add_port(name="e22", port=ring.ports["e22"])
    c.add_port(name="e23", port=ring.ports["e23"])
    return Utils.pos_neg_seperate(c)

# @gf.cell
# def ring_assymmetry_add_drop_w_heater(radius=100, short_width=0.6, gap=0.6, wg_width=0.8, width=1, long_width=2, racetrack_len=200, buffer=3):
#     c = gf.Component()
#     ring = c << ring_asymmetry_only(radius=radius, short_width=short_width, long_width=long_width, racetrack_len=racetrack_len, buffer=buffer)
#     bus_wg_comp = gf.Component()
#     s1 = bus_wg_comp << straight(length=30, width=wg_width, buffer=buffer)
#     t1 = bus_wg_comp << taper(width1=wg_width, width2=width, length=radius - 15)
#     t2 = bus_wg_comp << taper(width1=width, width2=wg_width, length=radius - 15)
#     t1.connect("o1", s1.ports["o1"])
#     t2.connect("o2", s1.ports["o2"])
#     bus_wg_comp.add_port(name="o1", port=t1.ports["o2"])
#     bus_wg_comp.add_port(name="o2", port=t2.ports["o1"])
#     bus_wg1 = c << bus_wg_comp
#     bus_wg2 = c << bus_wg_comp
#     ring.center = (0, 0)
#     bus_wg1.center = (0, racetrack_len / 2 + radius + long_width/2 + wg_width/2 + gap)
#     bus_wg2.center = (0, - (racetrack_len / 2 + radius + long_width/2 + wg_width/2 + gap))
#     c.add_port(name="o1", port=bus_wg1.ports["o1"])
#     c.add_port(name="o2", port=bus_wg1.ports["o2"])
#     c.add_port(name="o3", port=bus_wg2.ports["o1"])
#     c.add_port(name="o4", port=bus_wg2.ports["o2"])
#     return Utils.pos_neg_seperate(c)

# comp = ring_assymmetry_add_drop()
# comp.show()

# comp = ring_assymmetry_add_drop_w_heater()
# comp.show()
