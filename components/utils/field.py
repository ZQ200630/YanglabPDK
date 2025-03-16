import gdsfactory as gf

from gdsfactory.typings import Layer
from YanglabPDK import LAYER
from YanglabPDK.components.utils.mark import cross

from functools import partial


def die_marker_field(field_size=1000, die_size=(10000, 10000), mark_pair_num=3, calipers=None):
    LUT = {
        # Left Top, Left Bottom, Right Top, Right Bottom
        0: ((0, 0), (0, 0), (0, 0), (0, 0)),
        1: ((1, 0), (1, 0), (-1, 0), (-1, 0)),
        2: ((0, -1), (0, 1), (0, -1), (0, 1)),
        3: ((2, 0), (2, 0), (-2, 0), (-2, 0)),
        4: ((0, -2), (0, 2), (0, -2), (0, 2)),
    }
    # If the die size is not integer times of field size, exception will be raised
    if die_size[0] % field_size != 0 or die_size[1] % field_size != 0:
        raise ValueError("Die size is not integer times of field size")
    die = gf.components.die(size=die_size, street_width=20, street_length=400, die_name='', text_size=100.0,  text_location='SW', text=partial(gf.components.text, layer=LAYER.CUT), layer=LAYER.DIE, bbox_layer=LAYER.CUT, draw_corners=True)
    field = gf.Component()
    field_number_x = die_size[0] // field_size + 2
    field_number_y = die_size[1] // field_size + 2
    for i in range(field_number_x):
        for j in range(field_number_y):
            field.add_ref(gf.components.rectangle(size=(field_size, field_size), layer=LAYER.FD)).movex(i*field_size).movey(j*field_size)
    marker = gf.Component()
    for i in range(mark_pair_num):
        left_top = marker << cross(text=str(i + 1))
        left_bot = marker << cross(text=str(i + 1))
        right_top = marker << cross(text=str(i + 1))
        right_bot = marker << cross(text=str(i + 1))
        left_top.center = (-die_size[0]/2-field_size/2+LUT[i][0][0]*field_size, die_size[1]/2+field_size/2+LUT[i][0][1]*field_size)
        left_bot.center = (-die_size[0]/2-field_size/2+LUT[i][1][0]*field_size, -die_size[1]/2-field_size/2+LUT[i][1][1]*field_size)
        right_top.center = (die_size[0]/2+field_size/2+LUT[i][2][0]*field_size, die_size[1]/2+field_size/2+LUT[i][2][1]*field_size)
        right_bot.center = (die_size[0]/2+field_size/2+LUT[i][3][0]*field_size, -die_size[1]/2-field_size/2+LUT[i][3][1]*field_size)
    
    anchor = gf.Component()
    left_top = anchor << gf.components.rectangle(size=(40, 40), layer=LAYER.AC)
    left_bot = anchor << gf.components.rectangle(size=(40, 40), layer=LAYER.AC)
    right_top = anchor << gf.components.rectangle(size=(40, 40), layer=LAYER.AC)
    right_bot = anchor << gf.components.rectangle(size=(40, 40), layer=LAYER.AC)
    left_top.center = (-die_size[0]/2-field_size+20, die_size[1]/2+field_size-20)
    left_bot.center = (-die_size[0]/2-field_size+20, -die_size[1]/2-field_size+20)
    right_top.center = (die_size[0]/2+field_size-20, die_size[1]/2+field_size-20)
    right_bot.center = (die_size[0]/2+field_size-20, -die_size[1]/2-field_size+20)

    c = gf.Component()
    # d = c << die
    f = c << field
    m = c << marker
    a = c << anchor
    straight = c << gf.components.rectangle(size=(2000, 5), layer=LAYER.MK)
    
    if calipers is not None:
        cal1 = c << calipers
        cal2 = c << calipers.rotate(90)
        cal3 = c << calipers
        cal4 = c << calipers.rotate(90)
        cal1.center = (-field_size/3, -die_size[1]/2-field_size*1/3)
        cal2.center = (-field_size*2/3, -die_size[1]/2-field_size*1/3)
        cal3.center = (field_size/3, -die_size[1]/2-field_size*1/3)
        cal4.center = (field_size*2/3, -die_size[1]/2-field_size*1/3)
    
    # shadow = c << gf.components.bbox(d.bbox, top=field_size, bottom=field_size, left=field_size, right=field_size, layer=LAYER.ALL)
    # shadow.center = (0, 0)
    # d.center = (0, 0)
    straight.center = (0, -die_size[1]/2-field_size*2/3)
    f.center = (0, 0)
    m.center = (0, 0)
    a.center = (0, 0)
    return c

if __name__ == "__main__":
    c = die_marker_field()
    c.show()