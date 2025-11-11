import gdsfactory as gf
import YanglabPDK.YanglabUtils as Utils
import YanglabPDK.YanglabSections as Sections
from YanglabPDK import LAYER
from YanglabPDK.components.waveguides.straight import straight
from YanglabPDK.components.tapers import taper

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

# comp = ring_assymmetry_add_drop()
# comp.show()
