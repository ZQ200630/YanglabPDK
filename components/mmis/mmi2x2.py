import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

@gf.cell
def mmi2x2(width_taper=2, length_taper=20, length_mmi=125, width_mmi=15, gap_mmi=4, width=1, buffer=3):
    c = gf.Component()
    gap_mmi = gf.snap.snap_to_grid(gap_mmi, grid_factor=2)
    w_taper = width_taper
    x = Sections.pos_neg_resist(width=width, buffer=buffer)
    width = width or x.width

    _taper = taper(
        length=length_taper,
        width1=width,
        width2=w_taper,
        buffer=buffer
    )

    delta_width = width_mmi - width
    y = width_mmi / 2
    pos_box = c.add_polygon([(-buffer, -y-buffer), (length_mmi+buffer, -y-buffer), (length_mmi+buffer, y+buffer), (-buffer, y+buffer)], layer=LAYER.PR)
    neg_box = c.add_polygon([(0, -y), (length_mmi, -y), (length_mmi, y), (0, y)], layer=LAYER.NR)
    pos_box.center = (0, 0)
    neg_box.center = (0, 0)
    left_top_taper = c << _taper
    left_bot_taper = c << _taper
    right_top_taper = c << _taper
    right_bot_taper = c << _taper
    right_bot_taper.mirror()
    right_top_taper.mirror()
    left_top_taper.xmax = neg_box.xmin
    left_bot_taper.xmax = neg_box.xmin
    right_top_taper.xmin = neg_box.xmax
    right_bot_taper.xmin = neg_box.xmax
    left_top_taper.y = gap_mmi / 2
    left_bot_taper.y = -gap_mmi / 2
    right_top_taper.y = gap_mmi / 2
    right_bot_taper.y = -gap_mmi / 2


    c.add_port(name="o1", port=left_bot_taper.ports["o1"])
    c.add_port(name="o2", port=left_top_taper.ports["o1"])
    c.add_port(name="o3", port=right_top_taper.ports["o1"])
    c.add_port(name="o4", port=right_bot_taper.ports["o1"])
    return Utils.pos_neg_seperate(c)