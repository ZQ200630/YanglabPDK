#!/usr/bin/env python
# coding=utf-8
'''
Author       : Qian Zhang
Date         : 2025-03-14 00:59:59
LastEditors  : Qian Zhang
LastEditTime : 2025-03-14 10:26:40
FilePath     : \YanglabPDK\components\tapers\taper.py
Description  : 

Copyright (c) 2025 by Prof. Lan Yang Lab, All Rights Reserved. 
'''
import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

#TODO: Taper function has some problems, need to be fixed

@gf.cell
def taper(length=10.0, width1=1, width2=1, buffer=3) -> gf.Component:
    """Linear taper, which tapers only the main cross section section.

    Args:
        length: taper length.
        width1: width of the west/left port.
        width2: width of the east/right port. Defaults to width1.
        buffer: buffer width for positive tone resist (um)
    """
    Xtrans = gf.path.transition(cross_section1=Sections.pos_neg_resist(width=width1, buffer=buffer), cross_section2=Sections.pos_neg_resist(width=width2, buffer=buffer), width_type='linear', offset_type='linear')
    path = gf.path.straight(length=length, npoints=1000)
    taper_transition = gf.path.extrude_transition(path, Xtrans)
    return Utils.pos_neg_seperate(taper_transition)

if __name__ == "__main__":
    c =taper(length=10, width1=0.5, width2=10)
    c.draw_ports()
    c.show()