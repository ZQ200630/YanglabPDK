#!/usr/bin/env python
# coding=utf-8
'''
Author       : Qian Zhang
Date         : 2025-08-27 14:55:13
LastEditors  : Qian Zhang
LastEditTime : 2025-08-27 16:09:28
FilePath     : \YanglabPDK\components\lasers\sagnet_feedback.py
Description  : 

Copyright (c) 2025 by Prof. Lan Yang Lab, All Rights Reserved. 
'''

import gdsfactory as gf
import YanglabPDK.YanglabUtils as Utils
import YanglabPDK.YanglabSections as Sections
from YanglabPDK import LAYER
from YanglabPDK.components.waveguides.straight import straight
from YanglabPDK.components.waveguides.straight_heater_metal import straight_heater_metal_undercut
from YanglabPDK.components.mmis import mmi1x2
from YanglabPDK.components.bends import bend_circular, bend_s
from YanglabPDK.components.reflectors.sagnac_loop import sagnac_loop
from YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry import ring_assymmetry_add_drop
from YanglabPDK.components.tapers import taper

@gf.cell
def sagnet_feedback(
    # Loop parameters
    radius_loop: float = 75,
    length_loop: float = 250,

    # Waveguide widths
    width: float | None = 1,
    wg_width: float = 0.8,
    short_width: float = 0.8,
    long_width: float = 2,

    # Taper parameters
    width_taper: float = 2.424,
    length_taper: float = 30,

    # MMI parameters
    length_mmi: float = 30.424,
    width_mmi: float = 6.024,
    gap_mmi: float = 0.675,

    # Sagnac loop/cavity parameters
    radius: float = 99,
    gap: float = 0.45,
    racetrack_len: float = 190,

    # Miscellaneous
    buffer: float = 3.0,
):
    c = gf.Component()
    add_drop = c << ring_assymmetry_add_drop(radius=radius, short_width=short_width, gap=gap, width=width, wg_width=wg_width, long_width=long_width, racetrack_len=racetrack_len, buffer=buffer)
    loop = c << sagnac_loop(radius_loop=radius_loop, length_loop=length_loop, width=width, width_taper=width_taper, length_taper=length_taper, length_mmi=length_mmi, width_mmi=width_mmi, gap_mmi=gap_mmi, buffer=buffer)
    circle1 = c << bend_circular(radius=radius_loop, angle=180, width=width, buffer=buffer)
    circle1.connect("o1", add_drop.ports["o2"])
    taper1 = c << taper(width1=width, width2=0.05, length=30)
    taper1.connect("o1", add_drop.ports["o1"])
    loop.connect("o1", circle1.ports["o2"])
    rec_terminal = gf.components.rectangle(size=(10, 2 * buffer + 0.05), layer=LAYER.PR).copy()
    rec_terminal.add_port(name="o1", center=(0, (2 * buffer + 0.05)/2), width=0.05, orientation=180, layer=LAYER.NR)
    term = c << rec_terminal
    term.connect("o1", taper1.ports["o2"])
    c.add_port(name="o1", port=add_drop.ports["o3"])
    c.add_port(name="o2", port=add_drop.ports["o4"])
    c.flatten()
    return c

@gf.cell
def sagnet_feedback_1(
    # Loop parameters
    radius_loop: float = 75,
    length_loop: float = 250,

    # Waveguide widths
    width: float | None = 1,
    wg_width: float = 0.8,
    short_width: float = 0.8,
    long_width: float = 2,

    # Taper parameters
    width_taper: float = 2.424,
    length_taper: float = 30,

    # MMI parameters
    length_mmi: float = 30.424,
    width_mmi: float = 6.024,
    gap_mmi: float = 0.675,

    # Sagnac loop/cavity parameters
    radius: float = 99,
    gap: float = 0.45,
    racetrack_len: float = 190,

    # Miscellaneous
    buffer: float = 3.0,
):
    c = gf.Component()
    add_drop = c << ring_assymmetry_add_drop(radius=radius, short_width=short_width, gap=gap, width=width, wg_width=wg_width, long_width=long_width, racetrack_len=racetrack_len, buffer=buffer)
    loop = c << sagnac_loop(radius_loop=radius_loop, length_loop=length_loop, width=width, width_taper=width_taper, length_taper=length_taper, length_mmi=length_mmi, width_mmi=width_mmi, gap_mmi=gap_mmi, buffer=buffer)
    # circle1 = c << bend_circular(radius=radius_loop, angle=180, width=width, buffer=buffer)
    # circle1.connect("o1", add_drop.ports["o2"])
    taper1 = c << taper(width1=width, width2=0.05, length=30)
    taper1.connect("o1", add_drop.ports["o2"])
    loop.connect("o1", add_drop.ports["o1"])
    rec_terminal = gf.components.rectangle(size=(10, 2 * buffer + 0.05), layer=LAYER.PR).copy()
    rec_terminal.add_port(name="o1", center=(0, (2 * buffer + 0.05)/2), width=0.05, orientation=180, layer=LAYER.NR)
    term = c << rec_terminal
    term.connect("o1", taper1.ports["o2"])
    c.add_port(name="o1", port=add_drop.ports["o3"])
    c.add_port(name="o2", port=add_drop.ports["o4"])
    c.flatten()
    return c

@gf.cell
def sagnet_feedback_with_curve(# Loop parameters
    radius_loop: float = 75,
    length_loop: float = 250,

    # Waveguide widths
    width: float | None = 1,
    wg_width: float = 0.8,
    short_width: float = 0.8,
    long_width: float = 2,

    # Taper parameters
    width_taper: float = 2.424,
    length_taper: float = 30,

    # MMI parameters
    length_mmi: float = 30.424,
    width_mmi: float = 6.024,
    gap_mmi: float = 0.675,

    # Sagnac loop/cavity parameters
    radius: float = 99,
    gap: float = 0.45,
    racetrack_len: float = 200,
    
    # Band coupler out
    radius_outbend = 280,
    angle_outbend = 110,
    
    # Total Len & Offset
    total_lens = 12000,
    offset = 4000,
    pos_edge_coupler = 3010,
    edge_coupler_len = 250,
    edge_coupler_width = 0.15,

    # Miscellaneous
    buffer: float = 3.0
    ):
    c = gf.Component()
    feedback_comp = c << sagnet_feedback(radius_loop=radius_loop, length_loop=length_loop, width=width, wg_width=wg_width, short_width=short_width, long_width=long_width, width_taper=width_taper, length_taper=length_taper, length_mmi=length_mmi, width_mmi=width_mmi, gap_mmi=gap_mmi, radius=radius, gap=gap, racetrack_len=racetrack_len, buffer=buffer)
    bend1 = c << bend_circular(radius=radius_outbend, angle=-angle_outbend, width=width, buffer=buffer)
    bend2 = c << bend_circular(radius=radius_outbend, angle=angle_outbend, width=width, buffer=buffer)
    bend1.connect("o1", feedback_comp.ports["o1"])
    bend2.connect("o1", bend1.ports["o2"])
    shape_size_x = feedback_comp.ports["o2"].x - bend2.ports["o2"].x + radius_loop
    l1 = (1000 - shape_size_x) / 2
    l2 = (1000 - shape_size_x) / 2 + radius_loop
    straight_left = c << straight(length=l1 + offset, width=width, buffer=buffer)
    straight_right = c << straight(length=l2 + total_lens - offset - 1000 - edge_coupler_len - pos_edge_coupler, width=width, buffer=buffer)
    taper_coupler = c << taper(length=edge_coupler_len, width1=width, width2=edge_coupler_width, buffer=buffer)
    straight_right_right = c << straight(length=pos_edge_coupler, width=edge_coupler_width, buffer=buffer)
    straight_left.connect("o1", bend2.ports["o2"])
    straight_right.connect("o1", feedback_comp.ports["o2"])
    taper_coupler.connect("o1", straight_right.ports["o2"])
    straight_right_right.connect("o1", taper_coupler.ports["o2"])
    return Utils.pos_neg_seperate(c)

@gf.cell
def sagnet_feedback_with_curve_micro_heater(# Loop parameters
    radius_loop: float = 75,
    length_loop: float = 250,

    # Waveguide widths
    width: float | None = 1,
    wg_width: float = 0.8,
    short_width: float = 0.8,
    long_width: float = 2,

    # Taper parameters
    width_taper: float = 2.424,
    length_taper: float = 30,

    # MMI parameters
    length_mmi: float = 30.424,
    width_mmi: float = 6.024,
    gap_mmi: float = 0.675,

    # Sagnac loop/cavity parameters
    radius: float = 99,
    gap: float = 0.45,
    racetrack_len: float = 200,
    
    # Band coupler out
    radius_outbend = 280,
    angle_outbend = 110,
    
    # Total Len & Offset
    total_lens = 12000,
    offset = 4000,
    pos_edge_coupler = 3010,
    edge_coupler_len = 250,
    edge_coupler_width = 0.15,

    # Micro heater
    heater_length: float = 500,
    heater_width: float = 0.5,
    heater_offset: float = 3000,

    # Miscellaneous
    buffer: float = 3.0
    ):
    c = gf.Component()
    feedback_comp = c << sagnet_feedback(radius_loop=radius_loop, length_loop=length_loop, width=width, wg_width=wg_width, short_width=short_width, long_width=long_width, width_taper=width_taper, length_taper=length_taper, length_mmi=length_mmi, width_mmi=width_mmi, gap_mmi=gap_mmi, radius=radius, gap=gap, racetrack_len=racetrack_len, buffer=buffer)
    bend1 = c << bend_circular(radius=radius_outbend, angle=-angle_outbend, width=width, buffer=buffer)
    bend2 = c << bend_circular(radius=radius_outbend, angle=angle_outbend, width=width, buffer=buffer)
    bend1.connect("o1", feedback_comp.ports["o1"])
    bend2.connect("o1", bend1.ports["o2"])
    shape_size_x = feedback_comp.ports["o2"].x - bend2.ports["o2"].x + radius_loop
    l1 = (1000 - shape_size_x) / 2
    l2 = (1000 - shape_size_x) / 2 + radius_loop
    straight_left = c << straight(length=l1 + offset, width=width, buffer=buffer)
    straight_right = c << straight(length=l2 + total_lens - offset - 1000 - edge_coupler_len - pos_edge_coupler - heater_length - heater_offset, width=width, buffer=buffer)
    straight_right_heater = c << straight_heater_metal_undercut(length = heater_length, width=width, heater_width=heater_width, buffer=buffer)
    straight_right_heater_right = c << straight(length=heater_offset, width=width, buffer=buffer)
    taper_coupler = c << taper(length=edge_coupler_len, width1=width, width2=edge_coupler_width, buffer=buffer)
    straight_right_right = c << straight(length=pos_edge_coupler, width=edge_coupler_width, buffer=buffer)
    straight_left.connect("o1", bend2.ports["o2"])
    straight_right.connect("o1", feedback_comp.ports["o2"])
    straight_right_heater.connect("o1", straight_right.ports["o2"])
    straight_right_heater_right.connect("o1", straight_right_heater.ports["o2"])
    taper_coupler.connect("o1", straight_right_heater_right.ports["o2"])
    straight_right_right.connect("o1", taper_coupler.ports["o2"])
    c.add_port(name="e_left", port=straight_right_heater.ports["l_e4"])
    c.add_port(name="e_right", port=straight_right_heater.ports["r_e4"])
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    # c = sagnet_feedback_with_curve()
    c = sagnet_feedback_with_curve_micro_heater()
    c.draw_ports()
    c.show()