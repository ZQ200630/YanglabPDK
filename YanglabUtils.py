#!/usr/bin/env python
# coding=utf-8

'''
Author       : Qian Zhang
Date         : 2025-03-13 15:15:35
LastEditors  : Qian Zhang
LastEditTime : 2025-03-13 17:52:17
FilePath     : \YanglabPDK\YanglabUtils.py
Description  : 

Copyright (c) 2025 by Prof. Lan Yang Lab, All Rights Reserved. 
'''

import gdsfactory as gf
from YanglabPDK import YanglabLayerStack as LayerStack
LAYER = LayerStack.LAYER

# When there is a overlap between positive and negative resist, use this function to seperate them
def pos_neg_seperate(comp):
    ps_layer = comp.extract(layers=(LAYER.PR,))
    ng_layer = comp.extract(layers=(LAYER.NR,))
    rest_layer = comp.remove_layers(layers=(LAYER.PR, LAYER.NR))
    # ng_layer name not start from unnamed, start as ng
    ng_layer.name = "ng" + ng_layer.name[7:]
    tmp1 = gf.Component(name="tmp1")
    ps = tmp1.add_ref(ps_layer)
    pn = tmp1.add_ref(ng_layer)
    ps = gf.geometry.boolean(A=ps, B=pn, operation='A-B', layer=LAYER.PR)
    ps.name = "ps" + ps.name[7:]
    c = gf.Component(name="coupler_symmetric")
    c.add_ref(ps)
    c.add_ref(ng_layer)
    c.add_ref(rest_layer)
    c.name = comp.name
    c.ports = comp.ports
    c.info = comp.info
    return c

def remap_layers(comp, old_layer, new_layer):
    comp1 = comp.extract(layers=(old_layer, ))
    comp2 = comp.remove_layers(layers=(old_layer, ))
    comp3 = gf.Component()
    a1 = comp3.add_ref(comp1)
    a2 = comp3.add_ref(comp1)
    # Boolean operation
    a1 = gf.geometry.boolean(A=a1, B=a2, operation='and', layer=new_layer)
    # Merge a1 and comp2
    all_comp = gf.Component()
    all_comp.add_ref(a1)
    all_comp.add_ref(comp2)
    # All the ports should be transfer to the new layer, change the layer property of the ports
    all_comp.ports = comp.ports
    for port in all_comp.ports.values():
        if port.layer == old_layer:
            port.layer = new_layer
    return all_comp

def copy_layer(comp, layer1, layer2):
    comp1 = comp.extract(layers=(layer1, ))
    comp1 = remap_layers(comp1, layer1, layer2)
    all_comp = gf.Component()
    all_comp.add_ref(comp1)
    all_comp.add_ref(comp)
    all_comp.ports = comp.ports
    return all_comp

# Layer1 - Layer2, reserve substracted layer1 and layer2
def substract_layer(comp, layer1, layer2):
    comp1 = comp.extract(layers=(layer1, ))
    comp2 = comp.extract(layers=(layer2, ))
    comp3 = comp.remove_layers(layers=(layer1, ))
    # Boolean operation
    comp4 = gf.geometry.boolean(A=comp1, B=comp2, operation='A-B', layer=layer1)
    all_comp = gf.Component()
    all_comp.add_ref(comp4)
    all_comp.add_ref(comp3)
    all_comp.ports = comp.ports
    return all_comp

def remove_layer(comp, layer):
    comp2 = comp.remove_layers(layers=(layer, ))
    return comp2