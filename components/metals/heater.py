import numpy as np
import gdsfactory as gf
from YanglabPDK import *

def arc_meander_points_one_side(
    R: float,
    theta_start: float,   # rad
    theta_end: float,     # rad
    tooth_w: float,
    tooth_len: float,
) -> np.ndarray:
    """
    One-side arc meander, per your rule:
    - use arc-direction half-step start: theta_start + (tooth_w/R)/2
    - inner/outer radii differ by tooth_len
    - stop at last theta_k < theta_end (no need to hit exactly)
    Returns Nx2 points.
    """
    dtheta = tooth_w / max(R, 1e-12)

    # ensure direction consistent
    if theta_end < theta_start:
        dtheta = -abs(dtheta)
    else:
        dtheta = abs(dtheta)

    # start at half step along the arc (this fixes your “start point” issue)
    theta0 = theta_start + 0.5 * dtheta

    # generate theta nodes, stop at last < theta_end
    thetas = []
    th = theta0
    if dtheta > 0:
        while th < theta_end:
            thetas.append(th)
            th += dtheta
    else:
        while th > theta_end:
            thetas.append(th)
            th += dtheta
    thetas = np.array(thetas, float)

    r_in  = R - tooth_len / 2.0
    r_out = R + tooth_len / 2.0

    def xy(r, th):
        return np.array([r * np.cos(th), r * np.sin(th)], float)

    pts = []
    if len(thetas) == 0:
        # fallback: just one arc point
        pts.append(xy(R, theta_start))
        return np.asarray(pts, float)

    # sequence: out(th0) -> in(th0)
    pts.append(xy(r_out, thetas[0]))
    pts.append(xy(r_in,  thetas[0]))

    # then alternate to create the “parallelogram cells” you circled
    for i in range(1, len(thetas)):
        th = thetas[i]
        if i % 2 == 1:
            # go along inner rail then radial out
            pts.append(xy(r_in,  th))
            pts.append(xy(r_out, th))
        else:
            # go along outer rail then radial in
            pts.append(xy(r_out, th))
            pts.append(xy(r_in,  th))

    return np.asarray(pts, float)

def mirror_points_y(points: np.ndarray) -> np.ndarray:
    pts = np.asarray(points, float).copy()
    pts[:, 0] *= -1.0
    return pts



@gf.cell
def microheater_arc_with_teeth(
    R: float = 30.0,               # arc centerline radius (um)
    w: float = 0.5,                # heater width (um)
    theta0: float = 30,         # start angle (deg)
    theta1: float = 30.0,         # end angle (deg)  (can be < theta0)
    lead_len: float = 3,        # straight lead length at each end (um)
    elef_taper_len: float = 5.0,    # length of taper from lead width to heater width (um)

    # pads
    pad_size: tuple[float, float] = (11, 11),  # (x, y) um

    # teeth (the small rectangles along the arc)
    add_teeth: bool = False,
    tooth_len: float = 3.0,         # tooth extends outward from arc outer edge (um)
    tooth_w: float = 1.2,           # tooth width along tangent direction (um)
) -> gf.Component:
    c = gf.Component()
    if add_teeth:
        # Define left arc using points
        N_points = 1000
        theta_deg_right = np.linspace(theta0 - 90, 90 - theta1, N_points)
        theta_right = np.deg2rad(theta_deg_right)

        theta_deg_left = np.linspace(90 + theta1, 270 - theta0, N_points)
        theta_left = np.deg2rad(theta_deg_left)

        x_right = R * np.cos(theta_right)
        y_right = R * np.sin(theta_right)

        x_left = R * np.cos(theta_left)
        y_left = R * np.sin(theta_left)
        # 1) 点列（单位：um）
        right = np.column_stack((x_right, y_right))          # Nx2
        left  = np.column_stack((x_left,  y_left))           # Nx2

        p_pre  = np.array([x_right[0], y_right[0] - lead_len - elef_taper_len])   # 要加在最前面的点，形状 (1,2)
        p_post = np.array([x_left[-1], y_left[-1] - lead_len - elef_taper_len])   # 要加在最后的点

        # angles as you originally define
        # 右侧弧的角度范围（按你原来的定义）
        theta_start = np.deg2rad(theta0 - 90)
        theta_end   = np.deg2rad(90 - theta1)

        right = arc_meander_points_one_side(
            R=R,
            theta_start=theta_start,
            theta_end=theta_end,
            tooth_w=tooth_w,
            tooth_len=tooth_len,
        )

        # 左边对称得到，并反向保持整体走线方向一致
        left = mirror_points_y(right)[::-1]

        p_pre  = np.array([right[0, 0], right[0, 1] - lead_len - elef_taper_len])
        p_post = np.array([left[-1, 0], left[-1, 1] - lead_len - elef_taper_len])

        points = np.vstack([p_pre, right, left, p_post])

        # 2) Path
        p = gf.Path(points)

        # 3) CrossSection（最常用：只给 width + layer）
        xs = gf.CrossSection(
            sections=[
                gf.Section(width=w, layer=LAYER.MT2, port_names=["e1", "e2"]),  # 主体线宽 2 um
            ],
            
        )

        # 4) Extrude 成几何
        heater = c << gf.path.extrude(p, cross_section=xs)
        # Left taper
        taper_left = c << gf.components.taper(length=elef_taper_len, width1=pad_size[0], width2=w, layer=LAYER.MT2)
        taper_left.connect("o2", heater.ports["e1"], allow_type_mismatch=True)
        pad_left_1 = c << gf.components.pad(size=pad_size, layer=LAYER.MT2)
        pad_left_1.connect("e1", taper_left.ports["o1"], allow_type_mismatch=True)
        pad_left_2 = c << gf.components.pad(size=pad_size, layer=LAYER.MT1)
        pad_left_2.connect("e1", taper_left.ports["o1"], allow_type_mismatch=True, allow_layer_mismatch=True)
        # Right taper
        taper_right = c << gf.components.taper(length=elef_taper_len, width1=pad_size[0], width2=w, layer=LAYER.MT2)
        taper_right.connect("o2", heater.ports["e2"], allow_type_mismatch=True, allow_layer_mismatch=True)
        pad_right_1 = c << gf.components.pad(size=pad_size, layer=LAYER.MT2)
        pad_right_1.connect("e1", taper_right.ports["o1"], allow_type_mismatch=True)
        pad_right_2 = c << gf.components.pad(size=pad_size, layer=LAYER.MT1)
        pad_right_2.connect("e1", taper_right.ports["o1"], allow_type_mismatch=True, allow_layer_mismatch=True)

        c.add_port(name="e2_0", port=pad_left_2.ports["e2"])
        c.add_port(name="e2_180", port=pad_left_2.ports["e4"])
        c.add_port(name="e2_270", port=pad_left_2.ports["e3"])

        c.add_port(name="e1_0", port=pad_right_2.ports["e2"])
        c.add_port(name="e1_180", port=pad_right_2.ports["e4"])
        c.add_port(name="e1_270", port=pad_right_2.ports["e3"])
    else:
        # Define left arc using points
        N_points = 1000
        theta_deg_right = np.linspace(theta0 - 90, 90 - theta1, N_points)
        theta_right = np.deg2rad(theta_deg_right)

        theta_deg_left = np.linspace(90 + theta1, 270 - theta0, N_points)
        theta_left = np.deg2rad(theta_deg_left)

        x_right = R * np.cos(theta_right)
        y_right = R * np.sin(theta_right)

        x_left = R * np.cos(theta_left)
        y_left = R * np.sin(theta_left)
        # 1) 点列（单位：um）
        right = np.column_stack((x_right, y_right))          # Nx2
        left  = np.column_stack((x_left,  y_left))           # Nx2

        p_pre  = np.array([x_right[0], y_right[0] - lead_len - elef_taper_len])   # 要加在最前面的点，形状 (1,2)
        p_post = np.array([x_left[-1], y_left[-1] - lead_len - elef_taper_len])   # 要加在最后的点

        points = np.vstack([p_pre, right, left, p_post])                # (2N+2)x2，闭合轮廓

        # 2) Path
        p = gf.Path(points)

        # 3) CrossSection（最常用：只给 width + layer）
        xs = gf.CrossSection(
            sections=[
                gf.Section(width=w, layer=LAYER.MT2, port_names=["e1", "e2"]),  # 主体线宽 2 um
            ],
            
        )

        # 4) Extrude 成几何
        heater = c << gf.path.extrude(p, cross_section=xs)
        # Left taper
        taper_left = c << gf.components.taper(length=elef_taper_len, width1=pad_size[0], width2=w, layer=LAYER.MT2)
        taper_left.connect("o2", heater.ports["e1"], allow_type_mismatch=True)
        pad_left_1 = c << gf.components.pad(size=pad_size, layer=LAYER.MT2)
        pad_left_1.connect("e1", taper_left.ports["o1"], allow_type_mismatch=True)
        pad_left_2 = c << gf.components.pad(size=pad_size, layer=LAYER.MT1)
        pad_left_2.connect("e1", taper_left.ports["o1"], allow_type_mismatch=True, allow_layer_mismatch=True)
        # Right taper
        taper_right = c << gf.components.taper(length=elef_taper_len, width1=pad_size[0], width2=w, layer=LAYER.MT2)
        taper_right.connect("o2", heater.ports["e2"], allow_type_mismatch=True, allow_layer_mismatch=True)
        pad_right_1 = c << gf.components.pad(size=pad_size, layer=LAYER.MT2)
        pad_right_1.connect("e1", taper_right.ports["o1"], allow_type_mismatch=True)
        pad_right_2 = c << gf.components.pad(size=pad_size, layer=LAYER.MT1)
        pad_right_2.connect("e1", taper_right.ports["o1"], allow_type_mismatch=True, allow_layer_mismatch=True)

        c.add_port(name="e2_0", port=pad_left_2.ports["e2"])
        c.add_port(name="e2_180", port=pad_left_2.ports["e4"])
        c.add_port(name="e2_270", port=pad_left_2.ports["e3"])

        c.add_port(name="e1_0", port=pad_right_2.ports["e2"])
        c.add_port(name="e1_180", port=pad_right_2.ports["e4"])
        c.add_port(name="e1_270", port=pad_right_2.ports["e3"])

    # c.draw_ports()
    c.flatten()
    return c