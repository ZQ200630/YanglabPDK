#!/usr/bin/env python
# coding=utf-8
'''
Author       : Qian Zhang
Date         : 2025-08-27 14:30:55
LastEditors  : Qian Zhang
LastEditTime : 2025-08-27 14:50:31
FilePath     : \YanglabPDK\components\reflectors\sagnac_loop.py
Description  : 

Copyright (c) 2025 by Prof. Lan Yang Lab, All Rights Reserved. 
'''


import gdsfactory as gf
import YanglabPDK.YanglabUtils as Utils
import YanglabPDK.YanglabSections as Sections
from YanglabPDK import LAYER
from YanglabPDK.components.waveguides.straight import straight
from YanglabPDK.components.mmis import mmi1x2
from YanglabPDK.components.bends import bend_circular, bend_s

@gf.cell
def sagnac_loop(
    radius_loop: float = 75,
    length_loop: float = 250,
    width: float | None = 1,
    width_taper: float = 2.424,
    length_taper: float = 30,
    length_mmi: float = 30.424,
    width_mmi: float = 6.024,
    gap_mmi: float = 0.675,
    buffer: float = 3.0):
    c = gf.Component()
    mmi = c << mmi1x2(width=width, width_taper=width_taper, length_taper=length_taper, length_mmi=length_mmi, width_mmi=width_mmi, gap_mmi=gap_mmi, buffer=buffer)
    bend_cir = c << bend_circular(radius=radius_loop, angle=180, width=width, buffer=buffer)
    s_bend1 = c << bend_s(size=[length_loop, radius_loop - gap_mmi / 2 - width_taper / 2], width=width, buffer=buffer)
    s_bend2 = c << bend_s(size=[length_loop, -(radius_loop - gap_mmi / 2 - width_taper / 2)], width=width, buffer=buffer)
    mmi.center = (0, 0)
    mmi.rotate(180)
    s_bend1.connect("o1", mmi.ports["o2"])
    s_bend2.connect("o1", mmi.ports["o3"])
    bend_cir.connect("o1", s_bend2.ports["o2"])
    c.add_port(name="o1", port=mmi.ports["o1"])
    return Utils.pos_neg_seperate(c)
    

if __name__ == "__main__":
    c = sagnac_loop()
    c.show()