import gdsfactory as gf
import YanglabPDK.YanglabUtils as Utils
import YanglabPDK.YanglabSections as Sections
from YanglabPDK import LAYER

from YanglabPDK.components.cavities.cavity_wgm import ring_circle, ring_pulley_circle
from YanglabPDK.components.waveguides.straight import straight

from YanglabPDK.components.bends.bend_s import bend_s

@gf.cell
def ring_with_wg_2_in_1(
    radius: float = 80,
    gap: float = 0.5,
    width_wg: float = 1,
    width_ring: float = 1,
    offset: float = 0,
    total_length: float = 12000
) -> gf.Component:
    r"""Returns single ring with waveguides aligh to writing field, for 2 rings in 1 field array.

    Args:
        radius: Ring radius.
        gap: Ring - waveguide gap.
        width_wg: Waveguide width.
        width_ring: Ring width.
        offset: Offset from the left edge of the field.
        total_length: Total length of the component.
    """
    if(radius > 80):
        raise ValueError('Too large radius')
    c = gf.Component()
    ring = c << ring_circle(radius=radius, gap=gap, width_wg=width_wg, width_bend=width_ring, length_extension_left=radius, length_extension_right=radius)
    ring.mirror_y()

    # Waveguide with ring, should be 2x radius
    ring_length = abs(ring.ports['o1'].x - ring.ports['o2'].x)
    # WG between ring and bend, 500 - radius + 500 - 1.5 radius, make the ring and bend in the center of field
    wg3_length = 0
    # WG between ring and left edge of field, (1000 - 5*radius - wg3_length) / 2 + offset
    wg1_length = (500 - 5*radius - wg3_length) / 2 + offset
    # WG between bend and right edge of field, total length - wg1_length - wg3_length - ring_length - 3*radius
    wg2_length = total_length - wg1_length - wg3_length - ring_length - 3*radius

    wg1 = c << straight(length=wg1_length, width=width_wg)
    bend = c << bend_s(size=(radius*3, -radius*2), width=width_wg)
    wg2 = c << straight(length=wg2_length, width=width_wg)
    wg3 = c << straight(length=wg3_length, width=width_wg)
    text_G = c << gf.components.text('G = %4d nm'%(gap*1000), size=30, layer=LAYER.TX)
    ring.center = (0, 0)
    # text_R.center = (0, 50)
    text_G.center = (0, -radius - 50)
    wg1.connect(port='o1', other=ring.ports['o1'])
    wg3.connect(port='o1', other=ring.ports['o2'])
    bend.connect(port='o1', other=wg3.ports['o2'])
    wg2.connect(port='o1', other=bend.ports['o2'])
    return c

@gf.cell
def ring_with_wg_3_in_2(
    radius: float = 105,
    gap: float = 0.5,
    width_wg: float = 1,
    width_ring: float = 1,
    offset: float = 0,
    total_length: float = 12000
) -> gf.Component:
    r"""Returns single ring with waveguides aligned to writing field, 3 rings in 2 field array.

    Args:
        radius: Ring radius.
        gap: Ring - waveguide gap.
        width_wg: Waveguide width.
        width_ring: Ring width.
        offset: Offset from the left edge of the field.
        total_length: Total length of the component.
    """
    if(radius > 105):
        raise ValueError('Too large radius')
    c = gf.Component()
    ring = c << ring_circle(radius=radius, gap=gap, width_wg=width_wg, width_bend=width_ring, length_extension_left=radius, length_extension_right=radius)
    ring.mirror_y()

    # Waveguide with ring, should be 2x radius
    ring_length = abs(ring.ports['o1'].x - ring.ports['o2'].x)
    # WG between ring and bend, 500 - radius + 500 - 1.5 radius, make the ring and bend in the center of field
    wg3_length = 1000/3 - 2.5*radius
    # WG between ring and left edge of field, (1000 - 5*radius - wg3_length) / 2 + offset
    wg1_length = (1000/3 - 2*radius)/2 + offset
    # WG between bend and right edge of field, total length - wg1_length - wg3_length - ring_length - 3*radius
    wg2_length = total_length - wg1_length - wg3_length - ring_length - 3*radius

    wg1 = c << straight(length=wg1_length, width=width_wg)
    bend = c << bend_s(size=(radius*3, -radius*2), width=width_wg)
    wg2 = c << straight(length=wg2_length, width=width_wg)
    wg3 = c << straight(length=wg3_length, width=width_wg)
    text_G = c << gf.components.text('G = %4d nm'%(gap*1000), size=30, layer=LAYER.TX)
    ring.center = (0, 0)
    text_G.center = (0, -radius - 50)
    wg1.connect(port='o1', other=ring.ports['o1'])
    wg3.connect(port='o1', other=ring.ports['o2'])
    bend.connect(port='o1', other=wg3.ports['o2'])
    wg2.connect(port='o1', other=bend.ports['o2'])
    return c

@gf.cell
def ring_with_wg_1_in_1(
    radius: float = 180,
    gap: float = 0.5,
    width_wg: float = 1,
    width_ring: float = 1,
    offset: float = 2000,
    total_length: float = 12000
) -> gf.Component:
    r"""Returns single ring with waveguides aligned to writing field, for 1 ring in 1 field array.

    Args:
        radius: Ring radius.
        gap: Ring - waveguide gap.
        width_wg: Waveguide width.
        width_ring: Ring width.
        offset: Offset from the left edge of the field.
        total_length: Total length of the component.
    """
    if(radius > 210):
        raise ValueError('Too large radius')
    c = gf.Component()
    ring = c << ring_circle(radius=radius, gap=gap, width_wg=width_wg, width_bend=width_ring, length_extension_left=radius, length_extension_right=radius)
    ring.mirror_y()

    # Waveguide with ring, should be 2x radius
    ring_length = abs(ring.ports['o1'].x - ring.ports['o2'].x)
    # WG between ring and bend, 500 - radius + 500 - 1.5 radius, make the ring and bend in the center of field
    wg3_length = 0
    # WG between ring and left edge of field, (1000 - 5*radius - wg3_length) / 2 + offset
    wg1_length = (1000 - 5*radius - wg3_length) / 2 + offset
    # WG between bend and right edge of field, total length - wg1_length - wg3_length - ring_length - 3*radius
    wg2_length = total_length - wg1_length - wg3_length - ring_length - 3*radius

    wg1 = c << straight(length=wg1_length, width=width_wg)
    bend = c << bend_s(size=(radius*3, -radius*2), width=width_wg)
    wg2 = c << straight(length=wg2_length, width=width_wg)
    wg3 = c << straight(length=wg3_length, width=width_wg)
    text_G = c << gf.components.text('G = %4d nm'%(gap*1000), size=30, layer=LAYER.TX)
    ring.center = (0, 0)
    text_G.center = (0, -radius - 50)
    wg1.connect(port='o1', other=ring.ports['o1'])
    wg3.connect(port='o1', other=ring.ports['o2'])
    bend.connect(port='o1', other=wg3.ports['o2'])
    wg2.connect(port='o1', other=bend.ports['o2'])
    return c

@gf.cell
def ring_with_wg_1_in_2(
    radius: float = 300,
    gap: float = 0.5,
    width_wg: float = 1,
    width_ring: float = 1.5,
    offset: float = 0,
    total_length: float = 10000
) -> gf.Component:
    r"""Returns single ring with waveguides aligned to writing field, for 1 ring in 2 field array.

    Args:
        radius: Ring radius.
        gap: Ring - waveguide gap.
        width_wg: Waveguide width.
        width_ring: Ring width.
        offset: Offset from the left edge of the field.
        total_length: Total length of the component.
    """
    if(radius > 320):
        raise ValueError('Too large radius')
    c = gf.Component()
    ring = c << ring_circle(radius=radius, gap=gap, width_wg=width_wg, width_bend=width_ring, length_extension_left=radius, length_extension_right=radius)
    ring.mirror_y()

    # Waveguide with ring, should be 2x radius
    ring_length = abs(ring.ports['o1'].x - ring.ports['o2'].x)
    # WG between ring and bend, 500 - radius + 500 - 1.5 radius, make the ring and bend in the center of field
    wg3_length = 1000 - 2.5*radius
    # WG between ring and left edge of field, 500 - radius + offset
    wg1_length = 500 - radius + offset
    # WG between bend and right edge of field, total length - wg1_length - wg3_length - ring_length - 3*radius
    wg2_length = total_length - wg1_length - wg3_length - ring_length - 3*radius

    wg1 = c << straight(length=wg1_length, width=width_wg)
    bend = c << bend_s(size=(radius*3, -radius*2), width=width_wg)
    wg2 = c << straight(length=wg2_length, width=width_wg)
    wg3 = c << straight(length=wg3_length, width=width_wg)
    text_G = c << gf.components.text('G = %4d nm'%(gap*1000), size=30, layer=LAYER.TX)
    ring.center = (0, 0)
    text_G.center = (0, 0)
    wg1.connect(port='o1', other=ring.ports['o1'])
    wg3.connect(port='o1', other=ring.ports['o2'])
    bend.connect(port='o1', other=wg3.ports['o2'])
    wg2.connect(port='o1', other=bend.ports['o2'])
    return c


def pulley_ring_with_wg_3_in_2(radius=105, gap=0.5, width_wg=1, width_ring=1, angle=20, offset=0, total_length=12000):
    if(radius > 105):
        raise ValueError('Too large radius')
    c = gf.Component()
    ring = c << ring_pulley_circle(radius=radius, gap=gap, coupling_angle_coverage=angle, width_inner=width_ring, width_outer=width_wg, length_extension_left=radius, length_extension_right=radius)
    ring.mirror_y()

    # Waveguide with ring, should be 2x radius
    ring_length = abs(ring.ports['o1'].x - ring.ports['o2'].x)
    # ring_length = radius * 2
    # WG between ring and bend, 500 - radius + 500 - 1.5 radius, make the ring and bend in the center of field
    wg3_length = 1000/3 - 2.5*radius + radius - abs(ring.ports['o1'].x - ring.ports['o2'].x) / 2
    # WG between ring and left edge of field, (1000 - 5*radius - wg3_length) / 2 + offset
    wg1_length = (1000/3 - 2*radius)/2 + offset + radius - abs(ring.ports['o1'].x - ring.ports['o2'].x)
    # WG between bend and right edge of field, total length - wg1_length - wg3_length - ring_length - 3*radius
    wg2_length = total_length - wg1_length - wg3_length - abs(ring.ports['o1'].x - ring.ports['o2'].x) - 3*radius

    wg1 = c << straight(length=wg1_length, width=width_wg)
    bend = c << bend_s(size=(radius*3, -radius*2), width=width_wg)
    wg2 = c << straight(length=wg2_length, width=width_wg)
    wg3 = c << straight(length=wg3_length, width=width_wg)
    # text_R = c << gf.components.text('R = %3d um'%(radius), size=30, layer=LAYER.TX)
    text_G = c << gf.components.text('A = %.1f D'%(angle), size=30, layer=LAYER.TX)
    ring.center = (0, 0)
    # text_R.center = (0, 50)
    text_G.center = (0, -radius - 50)
    wg1.connect(port='o1', other=ring.ports['o1'])
    wg3.connect(port='o1', other=ring.ports['o2'])
    bend.connect(port='o1', other=wg3.ports['o2'])
    wg2.connect(port='o1', other=bend.ports['o2'])
    c.flatten()
    return c

if __name__ == "__main__":
    # c = ring_with_wg_2_in_1(radius=80, gap=0.5, width_wg=1, width_ring=1, offset=0, total_length=12000)
    # c = ring_with_wg_3_in_2(radius=105, gap=0.5, width_wg=1, width_ring=1, offset=0, total_length=12000)
    # c = ring_with_wg_1_in_1(radius=180, gap=0.5, width_wg=1, width_ring=1, offset=2000, total_length=12000)
    # c = ring_with_wg_1_in_2(radius=300, gap=0.5, width_wg=1, width_ring=1.5, offset=0, total_length=10000)
    c = pulley_ring_with_wg_3_in_2(radius=100, gap=0.5, width_wg=1, width_ring=1, angle=30, offset=150, total_length=12000)
    c.show()

