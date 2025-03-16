#!/usr/bin/env python
# coding=utf-8

# '''
# Author       : Qian Zhang
# Date         : 2025-03-13 15:15:35
# LastEditors  : Qian Zhang
# LastEditTime : 2025-03-13 18:12:18
# FilePath     : \20250313_TESTc:\Users\Qian\OneDrive\GDS\WorkSpace\MY_GDS_PACKAGE_V3\YanglabPDK\YanglabUtils.py
# Description  : 

# Copyright (c) 2025 by Prof. Lan Yang Lab, All Rights Reserved. 
# '''

import gdsfactory as gf
from YanglabPDK import *

# When there is a overlap between positive and negative resist, use this function to seperate them
def pos_neg_seperate(comp):
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
    c = gf.Component(name="coupler_symmetric")
    c.add_ref(ps)
    c.add_ref(ng_layer)
    c.add_ref(rest_layer)
    c.name = comp.name
    c.ports = comp.ports
    c.info = comp.info
    return c

# Used for transfer the layer from old_layer to new_layer
def remap_layers(comp, old_layer, new_layer):
    comp1 = comp.copy().extract(layers=(old_layer, ))
    comp2 = comp.copy().remove_layers(layers=(old_layer, ))
    comp3 = gf.Component()
    a1 = comp3.add_ref(comp1)
    a2 = comp3.add_ref(comp1)
    # Boolean operation
    a1 = gf.boolean(A=a1, B=a2, operation='and', layer=new_layer)
    # Merge a1 and comp2
    all_comp = gf.Component()
    all_comp.add_ref(a1)
    all_comp.add_ref(comp2)
    # All the ports should be transfer to the new layer, change the layer property of the ports
    for port in comp.ports:
        if port.layer == old_layer:
            all_comp.add_port(name=port.name, port=port, layer=new_layer)
        else:
            all_comp.add_port(name=port.name, port=port)
    return all_comp

# Layer1 - Layer2, reserve substracted layer1 and layer2
def substract_layer(comp, layer1, layer2):
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

# Copy layer1 pattern to layer2, reserve layer1
def copy_layer(comp, layer1, layer2):
    comp1 = comp.copy().extract(layers=(layer1, ))
    comp1 = remap_layers(comp1, layer1, layer2)
    all_comp = gf.Component()
    all_comp.add_ref(comp1)
    all_comp.add_ref(comp)
    all_comp.ports = comp.ports
    return all_comp

# Remove the layer from the component
def remove_layer(comp, layer):
    comp2 = comp.copy().remove_layers(layers=(layer, ))
    return comp2

if __name__ == "__main__":
    pass