#!/usr/bin/env python
# coding=utf-8
'''
Author       : Qian Zhang
Date         : 2024-11-01 14:29:39
LastEditors  : Qian Zhang
LastEditTime : 2025-01-06 14:04:28
FilePath     : \20250102_PS_LASER_TEST1\yanglab_pdk\YanglabSections.py
Description  : 

Copyright (c) 2024 by Prof. Lan Yang Lab, All Rights Reserved. 
'''
import gdsfactory as gf

from YanglabPDK import *



# Generate a cross section with both positive and negative resist
@gf.xsection
def pos_neg_resist(width=1, buffer=3) -> gf.CrossSection:
    print(LAYER)
    s0 = gf.Section(width=width, offset=0, layer=LAYER.NR, name='core', port_names=["o1", "o2"])
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=LAYER.PR, name='buffer1')
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=LAYER.PR, name='buffer2')
    x = gf.CrossSection(sections=[s0, s1, s2])
    return x

# Generate a cross section with both positive and negative resist, can select the layer
@gf.xsection
def pos_neg_resist_with_layer(width=1, buffer=3, layer1=LAYER.PR, layer2=LAYER.NR) -> gf.CrossSection:
    s0 = gf.Section(width=width, offset=0, layer=layer2, port_names=["o1", "o2"])
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=layer1)
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=layer1)
    x = gf.CrossSection(sections=[s0, s1, s2])
    return x

# Generate a cross section with both positive and negative resist, no port contained
@gf.xsection
def pos_neg_resist_without_port(width=1, buffer=3) -> gf.CrossSection:
    s0 = gf.Section(width=width, offset=0, layer=LAYER.NR)
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=LAYER.PR)
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=LAYER.PR)
    x = gf.CrossSection(sections=[s0, s1, s2])
    return x

# Generate a cross section with for two layers pattern, the first layer forms a slot, the second layer forms a waveguide
@gf.xsection
def double_layer_resist(width_top=1, width_bottom=7, layer1=LAYER.PR, layer2=LAYER.NR) -> gf.CrossSection:
    s0 = gf.Section(width=width_top, offset=0, layer=layer1, port_names=["o1", "o2"])
    s1 = gf.Section(width=width_bottom, offset=0, layer=layer2)
    x = gf.CrossSection(sections=[s0, s1])
    return x

# Not return a CrossSection, but a tuple of sections
def pos_neg_Section_Tuple(width=1, buffer=3):
    s0 = gf.Section(width=width, offset=0, layer=LAYER.NR)
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=LAYER.PR)
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=LAYER.PR)
    return (s0, s1, s2)