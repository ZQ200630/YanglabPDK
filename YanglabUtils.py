"""Geometry utility functions for YanglabPDK components.

These helpers wrap common gdsfactory layer operations used by lab components.
They are intentionally small and explicit because most of them are called just
before returning a generated layout cell.
"""

import gdsfactory as gf
from YanglabPDK import *


def pos_neg_seperate(comp):
    """Separate overlapping positive and negative resist geometry.

    The lab's resist convention often draws a negative-resist core together with
    positive-resist side buffers.  When both layers overlap, this function keeps
    the negative-resist geometry and subtracts it from the positive-resist layer.

    Args:
        comp: Component containing `LAYER.PR` and `LAYER.NR` geometry.

    Returns:
        A flattened copy of `comp` with positive resist minus negative resist,
        plus the original negative resist and all remaining layers.
    """
    comp = comp.copy()
    ps_layer = comp.extract(layers=(LAYER.PR,))
    ng_layer = comp.extract(layers=(LAYER.NR,))
    comp.locked = False
    comp.flatten()
    rest_layer = comp.remove_layers(layers=(LAYER.PR, LAYER.NR))
    # ng_layer name not start from unnamed, start as ng
    ng_layer.name = "ng" + ng_layer.name[7:]
    tmp1 = gf.Component()
    ps = tmp1.add_ref(ps_layer)
    pn = tmp1.add_ref(ng_layer)
    ps = gf.boolean(A=ps, B=pn, operation='A-B', layer=LAYER.PR, layer1=LAYER.PR, layer2=LAYER.NR)

    ps.name = "ps" + ps.name[7:]
    c = gf.Component()
    c.add_ref(ps)
    c.add_ref(ng_layer)
    c.add_ref(rest_layer)
    c.name = comp.name
    c.ports = comp.ports
    c.info = comp.info
    c.flatten()
    return c


def remap_layers(comp, old_layer, new_layer):
    """Move all polygons on one layer to another layer.

    Ports that were on `old_layer` are copied onto `new_layer`; other ports are
    preserved unchanged.
    """
    comp1 = comp.copy().extract(layers=(old_layer, ))
    comp2 = comp.copy().remove_layers(layers=(old_layer, ))
    comp3 = gf.Component()
    a1 = comp3.add_ref(comp1)
    a2 = comp3.add_ref(comp1)
    # Boolean operation
    aaa = gf.boolean(A=a1, B=a2, operation='and', layer=new_layer, layer1=old_layer, layer2=old_layer)
    # Merge a1 and comp2
    all_comp = gf.Component()
    all_comp.add_ref(aaa)
    all_comp.add_ref(comp2)
    # All the ports should be transfer to the new layer, change the layer property of the ports
    for port in comp.ports:
        if port.layer == old_layer:
            all_comp.add_port(name=port.name, port=port, layer=new_layer)
        else:
            all_comp.add_port(name=port.name, port=port)
    return all_comp


def substract_layer(comp, layer1, layer2):
    """Subtract `layer2` polygons from `layer1` while preserving other layers."""
    comp1 = comp.copy().extract(layers=(layer1, ))
    comp2 = comp.copy().extract(layers=(layer2, ))
    comp3 = comp.copy().remove_layers(layers=(layer1, ))
    # Boolean operation
    comp4 = gf.boolean(A=comp1, B=comp2, operation='A-B', layer=layer1)
    all_comp = gf.Component()
    all_comp.add_ref(comp4)
    all_comp.add_ref(comp3)
    all_comp.ports = comp.ports
    return all_comp


def copy_layer(comp, layer1, layer2):
    """Copy polygons from `layer1` to `layer2` while keeping `layer1`."""
    comp1 = comp.copy().extract(layers=(layer1, ))
    comp1 = remap_layers(comp1, layer1, layer2)
    all_comp = gf.Component()
    all_comp.add_ref(comp1)
    all_comp.add_ref(comp)
    all_comp.ports = comp.ports
    return all_comp


def remove_layer(comp, layer):
    """Return a copy of `comp` without polygons on `layer`."""
    comp2 = comp.copy().remove_layers(layers=(layer, ))
    return comp2


def round_unit(value, unit=0.001):
    """Round a value to the nearest layout grid unit.

    Args:
        value: Numeric value in microns.
        unit: Grid size in microns. Defaults to 1 nm.
    """
    return round(value / unit) * unit

if __name__ == "__main__":
    rounded_value = round_unit(12.34567, unit=0.001)
    print(f"Rounded Value: {rounded_value}")
