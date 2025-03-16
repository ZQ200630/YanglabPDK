import gdsfactory as gf
import yanglab_pdk.YanglabUtils as Utils
import yanglab_pdk.YanglabSections as Sections
from yanglab_pdk.components import bend as Bend
from yanglab_pdk.components import coupler_wgm as Coupler_WGM
from yanglab_pdk.components import basic as Basic
from functools import partial





ring_circle_pulley = partial(ring_single_pulley, radius=100, gap=0.5, length_x=0, length_y=0, width_inner=1, width_outer=1, buffer=3)