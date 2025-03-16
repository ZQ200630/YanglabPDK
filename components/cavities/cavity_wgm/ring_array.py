import gdsfactory as gf
import YanglabPDK.YanglabUtils as Utils
import YanglabPDK.YanglabSections as Sections
from YanglabPDK import LAYER

from YanglabPDK.components.cavities.cavity_wgm import ring_circle
from YanglabPDK.components.waveguides.straight import straight

from YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks import (
    ring_with_wg_3_in_2,
    ring_with_wg_2_in_1,
    ring_with_wg_1_in_1,
    ring_with_wg_1_in_2,
    pulley_ring_with_wg_3_in_2
)

from YanglabPDK.components.bends.bend_s import bend_s


def six_parallel_rings_2_in_1(parameters):
    c = gf.Component()
    ring1 = c << ring_with_wg_2_in_1(radius=parameters[0]['radius'], gap=parameters[0]['gap'], width_wg=parameters[0]['width_wg'], width_ring=parameters[0]['width_ring'], offset=3000, total_length=parameters[0]['total_length'])
    ring2 = c << ring_with_wg_2_in_1(radius=parameters[1]['radius'], gap=parameters[1]['gap'], width_wg=parameters[1]['width_wg'], width_ring=parameters[1]['width_ring'], offset=3500, total_length=parameters[1]['total_length'])
    ring3 = c << ring_with_wg_2_in_1(radius=parameters[2]['radius'], gap=parameters[2]['gap'], width_wg=parameters[2]['width_wg'], width_ring=parameters[2]['width_ring'], offset=4000, total_length=parameters[2]['total_length'])
    ring4 = c << ring_with_wg_2_in_1(radius=parameters[3]['radius'], gap=parameters[3]['gap'], width_wg=parameters[3]['width_wg'], width_ring=parameters[3]['width_ring'], offset=4500, total_length=parameters[3]['total_length'])
    ring5 = c << ring_with_wg_2_in_1(radius=parameters[4]['radius'], gap=parameters[4]['gap'], width_wg=parameters[4]['width_wg'], width_ring=parameters[4]['width_ring'], offset=5000, total_length=parameters[4]['total_length'])
    ring6 = c << ring_with_wg_2_in_1(radius=parameters[5]['radius'], gap=parameters[5]['gap'], width_wg=parameters[5]['width_wg'], width_ring=parameters[5]['width_ring'], offset=5500, total_length=parameters[5]['total_length'])
    ring1.center = (0, -250)
    ring2.center = (0, -150)
    ring3.center = (0, -50)
    ring4.center = (0, 50)
    ring5.center = (0, 150)
    ring6.center = (0, 250)
    return c

def six_parallel_rings_3_in_2(parameters):
    # total_length for six parameters must be same
    for param in parameters:
        if param['total_length'] != parameters[0]['total_length']:
            raise ValueError('Total length for six parameters must be same')
    # Total length must be multiple of 2000
    if parameters[0]['total_length'] % 2000 != 0:
        raise ValueError('Total length must be multiple of 2000')
    offset_initial = (parameters[0]['total_length'] - 4000) / 2
    c = gf.Component()
    ring1 = c << ring_with_wg_3_in_2(radius=parameters[0]['radius'], gap=parameters[0]['gap'], width_wg=parameters[0]['width_wg'], width_ring=parameters[0]['width_ring'], offset=offset_initial, total_length=parameters[0]['total_length'])
    ring2 = c << ring_with_wg_3_in_2(radius=parameters[1]['radius'], gap=parameters[1]['gap'], width_wg=parameters[1]['width_wg'], width_ring=parameters[1]['width_ring'], offset=offset_initial+1000*2/3*1, total_length=parameters[1]['total_length'])
    ring3 = c << ring_with_wg_3_in_2(radius=parameters[2]['radius'], gap=parameters[2]['gap'], width_wg=parameters[2]['width_wg'], width_ring=parameters[2]['width_ring'], offset=offset_initial+1000*2/3*2, total_length=parameters[2]['total_length'])
    ring4 = c << ring_with_wg_3_in_2(radius=parameters[3]['radius'], gap=parameters[3]['gap'], width_wg=parameters[3]['width_wg'], width_ring=parameters[3]['width_ring'], offset=offset_initial+1000*2/3*3, total_length=parameters[3]['total_length'])
    ring5 = c << ring_with_wg_3_in_2(radius=parameters[4]['radius'], gap=parameters[4]['gap'], width_wg=parameters[4]['width_wg'], width_ring=parameters[4]['width_ring'], offset=offset_initial+1000*2/3*4, total_length=parameters[4]['total_length'])
    ring6 = c << ring_with_wg_3_in_2(radius=parameters[5]['radius'], gap=parameters[5]['gap'], width_wg=parameters[5]['width_wg'], width_ring=parameters[5]['width_ring'], offset=offset_initial+1000*2/3*5, total_length=parameters[5]['total_length'])
    ring1.center = (0, -250)
    ring2.center = (0, -150)
    ring3.center = (0, -50)
    ring4.center = (0, 50)
    ring5.center = (0, 150)
    ring6.center = (0, 250)
    return c

def four_parallel_rings_1_in_1(parameters):
    c = gf.Component()
    ring1 = c << ring_with_wg_1_in_1(radius=parameters[0]['radius'], gap=parameters[0]['gap'], width_wg=parameters[0]['width_wg'], width_ring=parameters[0]['width_ring'],offset=4000, total_length=parameters[0]['total_length'])
    ring2 = c << ring_with_wg_1_in_1(radius=parameters[1]['radius'], gap=parameters[1]['gap'], width_wg=parameters[1]['width_wg'], width_ring=parameters[1]['width_ring'], offset=5000, total_length=parameters[1]['total_length'])
    ring3 = c << ring_with_wg_1_in_1(radius=parameters[2]['radius'], gap=parameters[2]['gap'], width_wg=parameters[2]['width_wg'], width_ring=parameters[2]['width_ring'], offset=6000, total_length=parameters[2]['total_length'])
    ring4 = c << ring_with_wg_1_in_1(radius=parameters[3]['radius'], gap=parameters[3]['gap'], width_wg=parameters[3]['width_wg'], width_ring=parameters[3]['width_ring'], offset=7000, total_length=parameters[3]['total_length'])
    ring1.center = (0, -150)
    ring2.center = (0, -50)
    ring3.center = (0, 50)
    ring4.center = (0, 150)
    return c

def three_parallel_rings_1_in_2(parameters):
    c = gf.Component()
    ring1 = c << ring_with_wg_1_in_2(radius=parameters[0]['radius'], gap=parameters[0]['gap'], width_wg=parameters[0]['width_wg'], width_ring=parameters[0]['width_ring'], offset=3000, total_length=parameters[0]['total_length'])
    ring2 = c << ring_with_wg_1_in_2(radius=parameters[1]['radius'], gap=parameters[1]['gap'], width_wg=parameters[1]['width_wg'], width_ring=parameters[1]['width_ring'], offset=5000, total_length=parameters[1]['total_length'])
    ring3 = c << ring_with_wg_1_in_2(radius=parameters[2]['radius'], gap=parameters[2]['gap'], width_wg=parameters[2]['width_wg'], width_ring=parameters[2]['width_ring'], offset=7000, total_length=parameters[2]['total_length'])
    ring1.center = (0, -100)
    ring2.center = (0, 0)
    ring3.center = (0, 100)
    return c

def parallel_rings_with_parameters_l_80(parameters):
    if len(parameters) % 6 != 0:
        raise ValueError('The number of parameters must be multiple integer of 6')
    c = gf.Component()
    all_comp = []
    for i in range(0, len(parameters), 6):
        all_comp.append(c << six_parallel_rings_2_in_1(parameters[i:i+6]))
    for index, comp in enumerate(all_comp):
        comp.x = 0
        comp.y = index * 1000
    return c

def parallel_rings_with_parameters_80_105(parameters):
    if len(parameters) % 6 != 0:
        raise ValueError('The number of parameters must be multiple integer of 6')
    c = gf.Component()
    all_comp = []
    for i in range(0, len(parameters), 6):
        all_comp.append(c << six_parallel_rings_3_in_2(parameters[i:i+6]))
    for index, comp in enumerate(all_comp):
        comp.x = 0
        comp.y = index * 1000
    return c

def parallel_rings_with_parameters_105_210(parameters):
    if len(parameters) % 4 != 0:
        raise ValueError('The number of parameters must be multiple integer of 4')
    c = gf.Component()
    all_comp = []
    for i in range(0, len(parameters), 4):
        all_comp.append(c << four_parallel_rings_1_in_1(parameters[i:i+4]))
    for index, comp in enumerate(all_comp):
        comp.x = 0
        comp.y = index * 1000
    return c

def parallel_rings_with_parameters_210_320(parameters):
    if len(parameters) % 3 != 0:
        raise ValueError('The number of parameters must be multiple integer of 3')
    c = gf.Component()
    all_comp = []
    for i in range(0, len(parameters), 3):
        all_comp.append(c << three_parallel_rings_1_in_2(parameters[i:i+3]))
    for index, comp in enumerate(all_comp):
        comp.x = 0
        comp.y = index * 1000
    return c

def parallel_rings_with_parameters_all_in_one(parameters):
    """Returns parallel rings array with optimized spatial arrangement.

    Args:
        parameters: list of parameters for each ring, need radius, gap, width_wg, width_ring, total_length
    """
    c = gf.Component()
    for param in parameters:
        # If all parameter's radius is same, that's ok, but if not, raise error
        if param['radius'] != parameters[0]['radius']:
            raise ValueError('All parameters must have same radius')
    if parameters[0]['radius'] < 80:
        # Parameters must be multiple integer of 6, compensate copy the last parameter to make it multiple integer of 6
        if len(parameters) % 6 != 0:
            for i in range(6 - len(parameters) % 6):
                parameters.append(parameters[-1])
        c << parallel_rings_with_parameters_l_80(parameters)
    elif parameters[0]['radius'] < 110:
        # Parameters must be multiple integer of 6, compensate copy the last parameter to make it multiple integer of 6
        if len(parameters) % 6 != 0:
            for i in range(6 - len(parameters) % 6):
                parameters.append(parameters[-1])
        c << parallel_rings_with_parameters_80_105(parameters)
    elif parameters[0]['radius'] < 180:
        # Parameters must be multiple integer of 4, compensate copy the last parameter to make it multiple integer of 4
        if len(parameters) % 4 != 0:
            for i in range(4 - len(parameters) % 4):
                parameters.append(parameters[-1])
        c << parallel_rings_with_parameters_105_210(parameters)
    elif parameters[0]['radius'] < 380:
        # Parameters must be multiple integer of 3, compensate copy the last parameter to make it multiple integer of 3
        if len(parameters) % 3 != 0:
            for i in range(3 - len(parameters) % 3):
                parameters.append(parameters[-1])
        c << parallel_rings_with_parameters_210_320(parameters)
    else:
        raise ValueError('Too large radius')
    return c

def pulley_six_parallel_rings_3_in_2(parameters, comments=None):
    # total_length for six parameters must be same
    for param in parameters:
        if param['total_length'] != parameters[0]['total_length']:
            raise ValueError('Total length for six parameters must be same')
    # Total length must be multiple of 2000
    if parameters[0]['total_length'] % 2000 != 0:
        raise ValueError('Total length must be multiple of 2000')
    offset_initial = (parameters[0]['total_length'] - 4000) / 2
    c = gf.Component()
    ring1 = c << pulley_ring_with_wg_3_in_2(width_ring=parameters[0]['width_ring'],width_wg=parameters[0]['width_wg'],angle=parameters[0]['angle'], radius=parameters[0]['radius'], gap=parameters[0]['gap'], offset=offset_initial, total_length=parameters[0]['total_length'])
    ring2 = c << pulley_ring_with_wg_3_in_2(width_ring=parameters[1]['width_ring'],width_wg=parameters[1]['width_wg'], angle=parameters[1]['angle'], radius=parameters[1]['radius'], gap=parameters[1]['gap'], offset=offset_initial+1000*2/3*1, total_length=parameters[1]['total_length'])
    ring3 = c << pulley_ring_with_wg_3_in_2(width_ring=parameters[2]['width_ring'],width_wg=parameters[2]['width_wg'], angle=parameters[2]['angle'], radius=parameters[2]['radius'], gap=parameters[2]['gap'], offset=offset_initial+1000*2/3*2, total_length=parameters[2]['total_length'])
    ring4 = c << pulley_ring_with_wg_3_in_2(width_ring=parameters[3]['width_ring'],width_wg=parameters[3]['width_wg'], angle=parameters[3]['angle'], radius=parameters[3]['radius'], gap=parameters[3]['gap'], offset=offset_initial+1000*2/3*3, total_length=parameters[3]['total_length'])
    ring5 = c << pulley_ring_with_wg_3_in_2(width_ring=parameters[4]['width_ring'],width_wg=parameters[4]['width_wg'], angle=parameters[4]['angle'], radius=parameters[4]['radius'], gap=parameters[4]['gap'], offset=offset_initial+1000*2/3*4, total_length=parameters[4]['total_length'])
    ring6 = c << pulley_ring_with_wg_3_in_2(width_ring=parameters[5]['width_ring'],width_wg=parameters[5]['width_wg'], angle=parameters[5]['angle'], radius=parameters[5]['radius'], gap=parameters[5]['gap'], offset=offset_initial+1000*2/3*5, total_length=parameters[5]['total_length'])
    ring1.center = (0, -250)
    ring2.center = (0, -150)
    ring3.center = (0, -50)
    ring4.center = (0, 50)
    ring5.center = (0, 150)
    ring6.center = (0, 250)
    if comments is not None:
        text = c << gf.components.text(comments, size=30, layer=LAYER.TX)
        text.center = (-2200, -200)
    return c

if __name__ == "__main__":
    c = six_parallel_rings_3_in_2(
        [
            {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
            {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
            {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
            {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
            {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
            {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
        ]
    )
    # c = pulley_six_parallel_rings_3_in_2(
    #     [
    #         {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
    #         {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
    #         {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
    #         {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
    #         {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 1, 'width_wg': 1, 'total_length': 10000},
    #         {'radius': 100, 'gap': 0.2, 'angle': 45, 'width_ring': 4, 'width_wg': 1, 'total_length': 10000},
    #     ],
    #     comments='This is a test'
    # )
    c.show()