#!/usr/bin/env python
# coding=utf-8
'''
Author       : Qian Zhang
Date         : 2026-01-04 16:19:12
LastEditors  : Qian Zhang
LastEditTime : 2026-01-05 16:10:31
FilePath     : \YanglabPDK\components\filters\awg.py
Description  : 

Copyright (c) 2026 by Prof. Lan Yang Lab, All Rights Reserved. 
'''
from YanglabPDK import *
import gdsfactory as gf
from YanglabPDK.YanglabUtils import remap_layers, pos_neg_seperate
from YanglabPDK.components.waveguides.straight import straight  
from YanglabPDK.components.bends import bend_circular, bend_s
from YanglabPDK.components.tapers import taper
import numpy as np

from YanglabPDK.components.shapes.circles import semi_circle_with_port, rowland_circle_with_port



# def calculate_arc_parameters(L_dist, L_total, theta_deg):
#     """Calculate the radius and angle for an arc given the distance between ports,
#     total length of the arc, and angle in degrees.

#     Args:
#         L_dist: Distance between the two ports.
#         L_total: Total length of the arc.
#         theta_deg: Angle in degrees.
#     """
#     print(f"Calculating arc parameters with L_dist={L_dist}, L_total={L_total}, theta_deg={theta_deg}")
#     theta_rad = np.deg2rad(theta_deg)
#     L1 = (L_total - L_dist / np.sin(theta_rad)) / (theta_rad / np.cos(theta_rad) - 1/np.sin(theta_rad))
#     L2 = L_dist - L1
#     print(f"L1: {L1}, L2: {L2}")
#     wg_length = L2 / np.sin(theta_rad)
#     radius = L1 / np.cos(theta_rad)
#     return wg_length, radius

def calculate_arc_parameters(L_dist, L_total, theta_deg):
    # R = (L_dist - L_total * np.cos(np.deg2rad(theta_deg))) / (np.sin(np.deg2rad(theta_deg)- np.deg2rad(theta_deg)*np.cos(np.deg2rad(theta_deg))))
    # L1 = L_total - R * np.deg2rad(theta_deg)
    # print(f"Calculated arc parameters: WG_Length={L1}, Radius={R}")
    # L_dist = 80.936
    # L_total = 97.51008600788649

    theta = theta_deg
    theta_rad = np.deg2rad(theta)

    R = (L_dist - (L_total * np.cos(theta_rad))) / (np.sin(theta_rad)-theta_rad*np.cos(theta_rad))
    L1 = L_total - R * theta_rad
    return L1, R

@gf.cell
def awg():
    c = gf.Component()
    # Define some parameters, which can be changed
    semi_circle_to_center_dist = 100
    lambda_0 = 1.064
    n_eff = 1.8
    order = 41
    delta_L = order * lambda_0 / n_eff
    delta_L = 28.5726
    w_port = 0.8
    awg_wg_number = 41
    awg_out_number = 8
    # Define the left semi-circle
    semi_circle = c << semi_circle_with_port(radius=38.0692, port_number_out=awg_wg_number)
    bend_left = c << bend_circular(radius=60, angle=-90, width=1)
    bend_left.connect(port="o1", other=semi_circle.ports[0])
    straight_left = c << straight(length=150, width=1)
    straight_left.connect(port="o1", other=bend_left.ports["o2"])
    # Define some commonly used ports
    last_port = semi_circle.ports[-1]
    first_port = semi_circle.ports[0]
    # Define the reference waveguide array length
    port_dist = abs(last_port.center[0] - first_port.center[1])
    R = (semi_circle_to_center_dist - port_dist) / np.sin(np.deg2rad(last_port.orientation))
    bend_circ = c << bend_circular(radius=R, angle=-last_port.orientation*2, width=w_port)
    bend_circ.connect(port="o1", other=last_port)
    L_reference = abs(R * np.deg2rad(-last_port.orientation))
    wg_l, rad = calculate_arc_parameters(semi_circle_to_center_dist+first_port.center[0]-last_port.center[0], L_reference, abs(last_port.orientation))
    # Generate a new port list, the first port is semi_circle.ports[-2], the last port is bend_circ.ports[1]
    new_ports = []
    for i in range(len(semi_circle.ports)-2):
        new_ports.append(semi_circle.ports[-2 - i])
    for i, port in enumerate(new_ports):
        L_total = L_reference + (i + 1) * delta_L / 2
        L_dist = semi_circle_to_center_dist+first_port.center[0]-port.center[0]
        theta_deg = abs(port.orientation)
        wg_length, radius = calculate_arc_parameters(L_dist, L_total, theta_deg)
        bend = c << bend_circular(radius=radius, angle=-port.orientation*2, width=w_port)
        straight_wg1 = c << straight(length=wg_length, width=w_port)
        straight_wg2 = c << straight(length=wg_length, width=w_port)
        straight_wg1.connect(port="o1", other=port, allow_width_mismatch=True)
        bend.connect(port="o1", other=straight_wg1.ports["o2"], allow_width_mismatch=True)
        straight_wg2.connect(port="o1", other=bend.ports["o2"], allow_width_mismatch=True)

    semi_circle_out = c << rowland_circle_with_port(radius=38.0692, port_number_out=awg_wg_number, port_number_in=awg_out_number)
    
    semi_circle_out.connect(port="o1", other=bend_circ.ports[1])
    
    global reference_out_position
    reference_out_position = None
    
    c.add_port(name="i1", port=straight_left.ports["o2"])
    
    for i in range(awg_out_number):
        if i == 0:
            reference_out_position = semi_circle_out.ports[f"i{i+1}"].center
        s = c << straight(length=15, width=w_port)
        bend = c << bend_circular(radius=50, angle=360-semi_circle_out.ports[f"i{i+1}"].orientation, width=w_port)
        s.connect(port="o1", other=semi_circle_out.ports[f"i{i+1}"])
        bend.connect(port="o1", other=s.ports["o2"])
        t = c << taper(length=30, width1=w_port, width2=1)
        t.connect(port="o1", other=bend.ports["o2"])
        s_compensate = c << straight(length=70 - abs(bend.ports["o2"].center[0]-reference_out_position[0]), width=1)
        s_compensate.connect(port="o1", other=t.ports["o2"])
        bend_compensate = c << bend_s(size=[350, 50 * i -100 - abs(bend.ports["o2"].center[1]-reference_out_position[1])], width=1, buffer=3)
        bend_compensate.connect(port="o1", other=s_compensate.ports["o2"])
        left_most_position = straight_left.ports["o2"].center[0]
        right_most_position = bend_compensate.ports["o2"].center[0]
        final_straight = c << straight(length=1000 + (left_most_position - right_most_position), width=1)
        final_straight.connect(port="o1", other=bend_compensate.ports["o2"])
        c.add_port(name=f"o{i+1}", port=final_straight.ports["o2"])
    # c.draw_ports()
    c.flatten()
    return pos_neg_seperate(c)

if __name__ == "__main__":
    c = awg()
    c.show()
