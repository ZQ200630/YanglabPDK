#!/usr/bin/env python
# coding=utf-8
'''
Author       : Qian Zhang
Date         : 2026-01-02 15:19:42
LastEditors  : Qian Zhang
LastEditTime : 2026-01-05 15:00:54
FilePath     : \YanglabPDK\components\shapes\circles.py
Description  : 

Copyright (c) 2026 by Prof. Lan Yang Lab, All Rights Reserved. 
'''

from YanglabPDK import *
import gdsfactory as gf
from YanglabPDK.YanglabUtils import remap_layers, pos_neg_seperate, round_unit
from YanglabPDK.components.waveguides.straight import straight  
import numpy as np

@gf.cell
def single_semi_circle(
    radius: float = 50.0,
    angle_resolution: float = 0.1,
    layer: tuple = LAYER.NR,
) -> gf.Component:
    """Generate a semicircle geometry (0° to 180°).

    Args:
        radius: radius of the semicircle.
        angle_resolution: number of degrees per point.
        layer: layer.
    
    Returns:
        Component with the generated layout.
    """
    if radius <= 0:
        raise ValueError(f"radius={radius} must be > 0")

    c = gf.Component()

    num_points = int(np.round(180.0 / angle_resolution)) + 1
    theta = np.deg2rad(np.linspace(0, 180, num_points, endpoint=True))

    points = np.stack(
        (radius * np.cos(theta), radius * np.sin(theta)),
        axis=-1,
    )
    
    c.add_polygon(points=points, layer=layer)
    return c

@gf.cell
def quarter_circle(
    radius: float = 50.0,
    angle_resolution: float = 0.1,
    layer: tuple = LAYER.NR,
) -> gf.Component:
    """Generate a quarter circle geometry (0° to 90°).

    Args:
        radius: radius of the quarter circle.
        angle_resolution: number of degrees per point.
        layer: layer.
    
    Returns:
        Component with the generated layout.
    """
    if radius <= 0:
        raise ValueError(f"radius={radius} must be > 0")

    c = gf.Component()

    num_points = int(np.round(90.0 / angle_resolution)) + 1
    theta = np.deg2rad(np.linspace(0, 90, num_points, endpoint=True))

    points = np.stack(
        (radius * np.cos(theta), radius * np.sin(theta)),
        axis=-1,
    )
    
    c.add_polygon(points=points, layer=layer)
    return c

@gf.cell
def semi_circle(
    radius: float = 50.0,
    angle_resolution: float = 0.1,
    buffer: float = 3.0,
) -> gf.Component:
    """Generate a semicircle geometry (0° to 180°).

    Args:
        radius: radius of the semicircle.
        angle_resolution: number of degrees per point.
        layer: layer.
    
    Returns:
        Component with the generated layout.
    """
    if radius <= 0:
        raise ValueError(f"radius={radius} must be > 0")

    c = gf.Component()

    num_points = int(np.round(180.0 / angle_resolution)) + 1
    theta = np.deg2rad(np.linspace(0, 180, num_points, endpoint=True))

    points = np.stack(
        (radius * np.cos(theta), radius * np.sin(theta)),
        axis=-1,
    )
    
    c.add_polygon(points=points, layer=LAYER.NR)
    # C is the semicircle on NR layer, we need to offset it inward to get PR layer
    new_c = c.copy()
    new_c.offset(distance=buffer, layer=LAYER.NR)
    new_c = remap_layers(
        comp=new_c,
        old_layer=LAYER.NR,
        new_layer=LAYER.PR,
    )
    comp = gf.Component()
    comp.add_ref(new_c)
    comp.add_ref(c)
    comp = pos_neg_seperate(comp)
    comp.flatten()
    return comp

@gf.cell
def semi_circle_with_port(
    radius: float = 50.0,
    angle_resolution: float = 0.1,
    buffer: float = 3.0,
    port_width_in: float = 1.0,
    port_width_out: float = 0.8,
    port_gap_out: float = 0.2,
    port_number_out: int = 21,
) -> gf.Component:
    """Generate a semicircle geometry (0° to 180°).

    Args:
        radius: radius of the semicircle.
        angle_resolution: number of degrees per point.
        layer: layer.
    
    Returns:
        Component with the generated layout.
    """
    if radius <= 0:
        raise ValueError(f"radius={radius} must be > 0")

    c = gf.Component()

    num_points = int(np.round(180.0 / angle_resolution)) + 1
    theta = np.deg2rad(np.linspace(0, 180, num_points, endpoint=True))

    points = np.stack(
        (radius * np.cos(theta), radius * np.sin(theta)),
        axis=-1,
    )
    
    c.add_polygon(points=points, layer=LAYER.NR)
    # C is the semicircle on NR layer, we need to offset it inward to get PR layer
    new_c = c.copy()
    new_c.offset(distance=buffer, layer=LAYER.NR)
    new_c = remap_layers(
        comp=new_c,
        old_layer=LAYER.NR,
        new_layer=LAYER.PR,
    )
    comp = gf.Component()
    comp << new_c
    comp << c
    comp.add_port(name="i1", center=(0, 0), orientation=270, layer=LAYER.NR, width=port_width_in, port_type="optical")
    # Output channels port
    R = radius
    l = port_width_out + port_gap_out
    theta_deg = 2 * np.arcsin(l / (2 * R)) * 180 / np.pi
    for i in range(port_number_out):
        if port_number_out % 2 == 1:
            # Odd number of ports
            angle = 180 - (i - (port_number_out - 1) / 2) * theta_deg
        else:
            # Even number of ports
            angle = 180 - (i - (port_number_out - 1) / 2) * theta_deg 
        angle_rad = np.deg2rad(angle)
        y = round_unit(-R * np.cos(angle_rad) * np.cos(np.deg2rad(theta_deg/2)))
        x = round_unit(R * np.sin(angle_rad) * np.cos(np.deg2rad(theta_deg/2)))
        orientation = round_unit(angle - 90)
        comp.add_port(
            name=f"o{i+1}",
            center=(x, y),
            orientation=orientation,
            layer=LAYER.NR,
            width=port_width_out,
            port_type="optical",
        )
    # comp.draw_ports()
    comp = pos_neg_seperate(comp)
    comp.flatten()
    return comp


def rotate_point(x, y, theta):
    """
    将点 (x, y) 绕原点逆时针旋转 theta（弧度）
    
    Args:
        x: X coordinate.
        y: Y coordinate.
        theta: Rotation angle in radians.

    Returns:
        Rotated point coordinates.
    """
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    v = np.array([x, y])
    v_rot = R @ v   # 等价于 np.dot(R, v)
    
    return v_rot


@gf.cell
def angled_arc_with_port(
    radius: float = 50.0,
    angle: float = 90.0,
    angle_resolution: float = 0.1,
    buffer: float = 3.0,
    port_width_in: float = 1.0,
    port_width_out: float = 0.8,
    port_gap_out: float = 0.2,
    port_number_out: int = 21,
) -> gf.Component:
    """Generate a semicircle geometry (0° to 180°).

    Args:
        radius: radius of the semicircle.
        angle_resolution: number of degrees per point.
        layer: layer.
    
    Returns:
        Component with the generated layout.
    """
    if radius <= 0:
        raise ValueError(f"radius={radius} must be > 0")

    c = gf.Component()

    num_points = int(np.round(angle / angle_resolution)) + 1
    theta = np.deg2rad(np.linspace(0, angle, num_points, endpoint=True))

    arc_pts = np.stack(
    (radius * np.cos(theta), radius * np.sin(theta)),
    axis=-1,
    )

    points = np.vstack(
        [
            (0.0, 0.0),   # 圆心
            arc_pts,
            (0.0, 0.0),   # 回到圆心，保证闭合
        ]
    )
    
    c.add_polygon(points=points, layer=LAYER.NR)
    c.rotate(angle=angle/4)
    # C is the semicircle on NR layer, we need to offset it inward to get PR layer
    new_c = c.copy()
    new_c.offset(distance=buffer, layer=LAYER.NR)
    new_c = remap_layers(
        comp=new_c,
        old_layer=LAYER.NR,
        new_layer=LAYER.PR,
    )
    comp = gf.Component()
    comp << new_c
    comp << c
    comp.add_port(name="o0", center=(0, 0), orientation=270, layer=LAYER.NR, width=port_width_in, port_type="optical")
    # Output channels port
    R = radius
    l = port_width_out + port_gap_out
    theta_deg = 2 * np.arcsin(l / (2 * R)) * 180 / np.pi
    for i in range(port_number_out):
        if port_number_out % 2 == 1:
            # Odd number of ports
            angle = 180 - (i - (port_number_out - 1) / 2) * theta_deg
        else:
            # Even number of ports
            angle = 180 - (i - (port_number_out - 1) / 2) * theta_deg
        angle_rad = np.deg2rad(angle)
        y = -R * np.cos(angle_rad) * np.cos(np.deg2rad(theta_deg/2))
        x = R * np.sin(angle_rad) * np.cos(np.deg2rad(theta_deg/2))
        orientation = angle - 90
        comp.add_port(
            name=f"o{i+1}",
            center=(x, y),
            orientation=orientation,
            layer=LAYER.NR,
            width=port_width_out,
            port_type="optical",
        )
    # comp.draw_ports()
    comp = pos_neg_seperate(comp)
    return comp

@gf.cell
def rowland_circle_with_port(
    radius: float = 50.0,
    angle: float = 75.0,
    angle_resolution: float = 0.1,
    buffer: float = 3.0,
    port_width_in: float = 0.8,
    port_width_out: float = 0.8,
    port_gap_out: float = 0.2,
    port_number_out: int = 21,
    port_number_in: int = 8,
    port_gap_in: float = 0.336
) -> gf.Component:
    """Generate a semicircle geometry (0° to 180°).

    Args:
        radius: radius of the semicircle.
        angle_resolution: number of degrees per point.
        layer: layer.
    
    Returns:
        Component with the generated layout.
    """
    if radius <= 0:
        raise ValueError(f"radius={radius} must be > 0")

    c = gf.Component()

    num_points = int(np.round(angle / angle_resolution)) + 1
    theta = np.deg2rad(np.linspace(0, angle, num_points, endpoint=True))

    arc_pts = np.stack(
    (rotate_point(radius * np.cos(theta), radius * np.sin(theta), np.deg2rad(90 - angle/2))),
    axis=-1,
    )

    points = np.vstack(
        [
            (0.0, 0.0),   # 圆心
            arc_pts,
            (0.0, 0.0),   # 回到圆心，保证闭合
        ]
    )
    
    c.add_polygon(points=points, layer=LAYER.NR)
    c.rotate(angle=90 - angle/2)
    new_c = gf.Component()
    # arc = new_c << c
    
    c = gf.Component()
    
    num_points_circle_poly = int(np.round(180.0 / angle_resolution)) + 1
    theta_circle_poly = np.deg2rad(np.linspace(0, 180, num_points_circle_poly, endpoint=True))

    pts_circle_poly = np.stack(
        (radius / 2 * np.cos(theta_circle_poly), - radius / 2 * np.sin(theta_circle_poly) + radius / 2),
        axis=-1,
    )
    
    points_circle_poly = np.vstack(
        [
            # rotate_point(radius * np.cos(theta[0]), radius * np.sin(theta[0]), np.deg2rad(90 - angle/2)),
            # pts_circle_poly,
            # rotate_point(radius * np.cos(theta[-1]), radius * np.sin(theta[-1]), np.deg2rad(90 - angle/2)),
            arc_pts,
            pts_circle_poly[::-1],
            # pts_circle_poly[0],
        ]
    )
    
    c.add_polygon(points=points_circle_poly, layer=LAYER.NR)
    circle_poly = new_c << c
    # circle = new_c << gf.components.circle(radius=radius/2, layer=LAYER.NR, angle_resolution=angle_resolution)
    # circle.move((0, radius/2))
    new_c.flatten()
    c = new_c
    # C is the semicircle on NR layer, we need to offset it inward to get PR layer
    new_c = c.copy()
    new_c.offset(distance=buffer, layer=LAYER.NR)
    new_c.show()
    new_c = remap_layers(
        comp=new_c,
        old_layer=LAYER.NR,
        new_layer=LAYER.PR,
    )
    comp = gf.Component()
    comp << new_c
    comp << c
    # Input channels port
    R = radius / 2
    l = port_width_in + port_gap_in
    theta_deg = 2 * np.arcsin(l / (2 * R)) * 180 / np.pi
    for i in range(port_number_in):
        if port_number_in % 2 == 1:
            # Odd number of ports
            angle = 0 + (i - (port_number_in - 1) / 2) * theta_deg
        else:
            # Even number of ports
            angle = 0 + (i - (port_number_in - 1) / 2) * theta_deg
        angle_rad = np.deg2rad(angle)
        x = R * np.sin(angle_rad) * np.cos(np.deg2rad(theta_deg/2))
        y = R - R * np.cos(angle_rad) * np.cos(np.deg2rad(theta_deg/2))
        orientation = angle-90
        comp.add_port(
            name=f"i{i+1}",
            center=(x, y),
            orientation=orientation,
            layer=LAYER.NR,
            width=port_width_in,
            port_type="optical",
        )
    # Output channels port
    R = radius
    l = port_width_out + port_gap_out
    theta_deg = 2 * np.arcsin(l / (2 * R)) * 180 / np.pi
    for i in range(port_number_out):
        if port_number_out % 2 == 1:
            # Odd number of ports
            angle = 180 - (i - (port_number_out - 1) / 2) * theta_deg
        else:
            # Even number of ports
            angle = 180 - (i - (port_number_out - 1) / 2) * theta_deg
        angle_rad = np.deg2rad(angle)
        y = -R * np.cos(angle_rad) * np.cos(np.deg2rad(theta_deg/2))
        x = R * np.sin(angle_rad) * np.cos(np.deg2rad(theta_deg/2))
        orientation = angle - 90
        comp.add_port(
            name=f"o{i+1}",
            center=(x, y),
            orientation=orientation,
            layer=LAYER.NR,
            width=port_width_out,
            port_type="optical",
        )
    # comp.draw_ports()
    comp = pos_neg_seperate(comp)
    return comp

# assumes you already have:
# - LAYER.NR, LAYER.PR
# - remap_layers(comp, old_layer, new_layer)
# - pos_neg_seperate(comp)


if __name__ == "__main__":
    c = gf.Component()
    # semi_c = c << semi_circle_with_port(radius=50.0, angle_resolution=0.1)
    # wg = c << straight(width=1, length=50)
    # wg.connect("o1", semi_c.ports["o0"])
    c << rowland_circle_with_port(radius=37.5, angle=75, angle_resolution=0.1)
    c.show()
    
