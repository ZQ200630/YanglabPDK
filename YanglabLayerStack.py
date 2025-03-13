#!/usr/bin/env python
# coding=utf-8
'''
Author       : Qian Zhang
Date         : 2024-10-31 12:05:15
LastEditors  : Qian Zhang
LastEditTime : 2024-11-01 14:17:30
FilePath     : \PDK_Template\yanglab_pdk\YanglabLayerStack.py
Description  : 

Copyright (c) 2024 by Prof. Lan Yang Lab, All Rights Reserved. 
'''

from functools import partial

import gdsfactory as gf
from gdsfactory.technology import (
    LayerLevel,
    LayerStack,
    LayerView,
    LayerViews,
    LayerMap,
)
from gdsfactory.typings import Layer

gf.config.rich_output()

nm = 1e-3

class YanglabLayerMap(LayerMap):
    # Field Layer
    FD: Layer = (0, 0)
    # Waveguide Layer
    WG: Layer = (1, 0)
    # Metal Layer(Gold)
    MT1: Layer = (2, 0)
    # Second Metal Layer
    MT2: Layer = (21, 0)
    # Text Layer
    TX: Layer = (3, 0)
    # Assisted Layer, As Frame of Slabs
    AS: Layer = (5, 0)
    # Mark Layer
    MK: Layer = (7, 0)
    # Version Layer
    VT: Layer = (8, 0)
    # Anchor Point Layer, help beamer locate the fields
    AC: Layer = (9, 0)
    # Hidden Layer, show parameters
    HD: Layer = (10, 0)
    # Silica Substrate
    SL: Layer = (99, 0)
    # Cladding Layer
    CL: Layer = (55, 0)
    # Positive Photoresist Layer
    PR: Layer = (60, 0)
    # Negative Photoresist Layer
    NR: Layer = (61, 0)
    # Deep Trench Layer
    DT: Layer = (33, 0)
    # Die Layer
    DIE: Layer = (100, 0)
    # Cutting Layer
    CUT: Layer = (101, 0)
    # All
    ALL: Layer = (255, 0)
    # Keep Out Layer
    KO: Layer = (121, 0)

LAYER = YanglabLayerMap()