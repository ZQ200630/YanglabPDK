import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK.components.tapers.taper import taper
from YanglabPDK.components.bends.bend_s import bend_s
from YanglabPDK.components.waveguides.straight import straight

@gf.cell
def coupler_adiabatic_full(
    coupling_length: float = 40.0, 
    dx: float = 10.0, 
    dy: float = 4.8, 
    gap: float = 0.5, 
    dw: float = 0.1, 
    width: float = 1, 
    buffer: float = 3
) -> gf.Component:
    """Adiabatic Full coupler.

    Design based on asymmetric adiabatic full
    coupler designs, such as the one reported in 'Integrated Optic Adiabatic
    Devices on Silicon' by Y. Shani, et al (IEEE Journal of Quantum
    Electronics, Vol. 27, No. 3 March 1991).

    1. is the first half of the input S-bend straight where the
    input straights widths taper by +dw and -dw,
    2. is the second half of the S-bend straight with constant,
    unbalanced widths,
    3. is the coupling region where the straights from unbalanced widths to
    balanced widths to reverse polarity unbalanced widths,
    4. is the fixed width straight that curves away from the coupling region,
    5.is the final curve where the straights taper back to the regular width
    specified in the straight template.

    Args:
        coupling_length: Length of the coupling region in um.
        dx: Length of the bend regions in um.
        dy: Port-to-port distance between the bend regions in um.
        gap: Distance between the two straights in um.
        dw: delta width. Top arm tapers to width - dw, bottom to width + dw in um.
        width: width of the waveguide. If None, it will use the width of the cross_section.
        buffer: buffer.

    
    Returns:
        Component with the generated layout.
    """
    c = gf.Component()

    x_top = width + dw
    x_bottom = width - dw

    taper_top = c << taper(
        length=coupling_length, width1=x_top, width2=x_bottom, buffer=buffer
    )

    taper_bottom = c << taper(
        length=coupling_length, width1=x_bottom, width2=x_top, buffer=buffer
    )

    bend_input_top = c << bend_s(
        size=(dx, (dy - gap - x_top) / 2.0), width=x_top, buffer=buffer
    )

    bend_input_top.dmovey((x_top + gap) / 2.0)
    
    bend_input_bottom = c << bend_s(
        size=(dx, (-dy + gap + x_bottom) / 2.0), width=x_bottom, buffer=buffer
    )
    bend_input_bottom.dmovey(-(x_bottom + gap) / 2.0)

    taper_top.connect("o1", bend_input_top.ports["o1"])
    taper_bottom.connect("o1", bend_input_bottom.ports["o1"])

    bend_output_top = c << bend_s(
        size=(dx, (dy - gap - x_top) / 2.0), width=x_bottom, buffer=buffer
    )
    
    bend_output_bottom = c << bend_s(
        size=(dx, (-dy + gap + x_bottom) / 2.0), width=x_top, buffer=buffer
    )

    bend_output_top.connect("o2", taper_top.ports["o2"], mirror=True)
    bend_output_bottom.connect("o2", taper_bottom.ports["o2"], mirror=True)

    c.add_port("o1", port=bend_input_bottom.ports["o2"])
    c.add_port("o2", port=bend_input_top.ports["o2"])
    c.add_port("o3", port=bend_output_top.ports["o1"])
    c.add_port("o4", port=bend_output_bottom.ports["o1"])
    c.auto_rename_ports()

    c.flatten()
    return Utils.pos_neg_seperate(c)

@gf.cell
def coupler_adiabatic_50(
    l_left_taper: float = 20.0,
    l_left_s: float = 20.0,
    l_coupler_taper: float = 50.0,
    l_coupler_directional: float = 30.0,
    l_right_s: float = 30.0,
    l_right_taper: float = 20.0,
    gap: float = 1.0,
    width: float = 0.5,
    width_inner: float = 0.5,
    dw: float = 0.1,
    input_wg_sep: float = 3.0,
    output_wg_sep: float = 3.0,
    buffer: float = 3.0
) -> gf.Component:
    """Returns 50/50 adiabatic coupler.

    Design based on asymmetric adiabatic 3dB coupler designs, such as:
    - https://doi.org/10.1364/CLEO.2010.CThAA2
    - https://doi.org/10.1364/CLEO_SI.2017.SF1I.5
    - https://doi.org/10.1364/CLEO_SI.2018.STh4B.4

    The coupler consists of:
    1. Left taper region (l_left_taper): input waveguides taper by +dw and -dw.
    2. Left S-bend region (l_left_s): constant, unbalanced widths.
    3. Coupler taper region (l_coupler_taper): asymmetric waveguides gradually come together.
    4. Directional coupler region (l_coupler_directional): coupling occurs, widths become equal.
    5. Right S-bend region (l_right_s): output waveguides separate.
    6. Right taper region (l_right_taper): waveguides taper back to original width.

    Args:
        l_left_taper: Length of the left taper region (um).
        l_left_s: Length of the left S-bend region (um).
        l_coupler_taper: Length of the coupler taper region (um).
        l_coupler_directional: Length of the directional coupler region (um).
        l_right_s: Length of the right S-bend region (um).
        l_right_taper: Length of the right taper region (um).
        gap: Gap between the two waveguides in the coupling region (um).
        width: Width of the waveguides (um).
        width_inner: Width of the inner waveguides in the coupling region (um).
        dw: Delta width; top arm tapers to width+dw, bottom to width-dw (um).
        input_wg_sep: Separation between input waveguides, center-to-center (um).
        output_wg_sep: Separation between output waveguides, center-to-center (um).
        buffer: Buffer around the waveguides (um).
    
    Returns:
        Component with the generated layout.
    """
    c = gf.Component()

    if l_coupler_taper <= 0:
        dw = 0

    left_top_taper = c << taper(
        length=l_left_taper, width1=width, width2=width_inner + dw / 2, buffer=buffer
    )
    left_bottom_taper = c << taper(
        length=l_left_taper, width1=width, width2=width_inner - dw / 2, buffer=buffer
    )

    left_top_s = c << bend_s(
        size=(l_left_s, input_wg_sep / 2.0),
        width=width_inner + dw / 2,
        buffer=buffer
    )
    left_bottom_s = c << bend_s(
        size=(l_left_s, -input_wg_sep / 2.0),
        width=width_inner - dw / 2,
        buffer=buffer
    )
    
    def adiabatic_equal_coupler(
        length: float, width1: float, width2: float, gap: float, buffer: float
    ) -> gf.Component:
        """Creates an adiabatic coupler with two waveguides tapering to equal widths."""
        coupler = gf.Component()
        taper1 = coupler << taper(length=length, width1=width1, width2=(width1 + width2)/2, buffer=buffer)
        taper2 = coupler << taper(length=length, width1=width2, width2=(width1 + width2)/2, buffer=buffer)
        taper1.center = (0, -(gap + width1 / 2 + width2 / 2) / 2)
        taper2.center = (0, (gap + width1 / 2 + width2 / 2) / 2)
        # Create all ports
        coupler.add_port("o1", port=taper1.ports["o1"])
        coupler.add_port("o2", port=taper2.ports["o1"])
        coupler.add_port("o3", port=taper1.ports["o2"])
        coupler.add_port("o4", port=taper2.ports["o2"])
        return coupler

    directional_upper_wg = c << straight(
        length=l_coupler_directional, width=width_inner, buffer=buffer
    )
    directional_lower_wg = c << straight(
        length=l_coupler_directional, width=width_inner, buffer=buffer
    )

    right_top_s = c << bend_s(
        size=(l_right_s, output_wg_sep / 2.0),
        width=width_inner,
        buffer=buffer
    )

    right_bottom_s = c << bend_s(
        size=(l_right_s, -output_wg_sep / 2.0),
        width=width_inner,
        buffer=buffer
    )

    right_top_taper = c << taper(
        length=l_right_taper, width1=width_inner, width2=width, buffer=buffer
    )

    right_bottom_taper = c << taper(
        length=l_right_taper, width1=width_inner, width2=width, buffer=buffer
    )


    if l_coupler_taper > 0:
        coupler = c << adiabatic_equal_coupler(
            length=l_coupler_taper,
            width1=width_inner + dw / 2,
            width2=width_inner - dw / 2,
            gap=gap,
            buffer=buffer
        )    
        coupler.center = (0, 0)
        left_top_s.connect("o2", coupler.ports["o1"])
        left_bottom_s.connect("o2", coupler.ports["o2"])
        left_top_taper.connect("o2", left_top_s.ports["o1"])
        left_bottom_taper.connect("o2", left_bottom_s.ports["o1"])
        directional_upper_wg.connect("o1", coupler.ports["o4"])
        directional_lower_wg.connect("o1", coupler.ports["o3"])
        right_top_s.connect("o1", directional_upper_wg.ports["o2"])
        right_bottom_s.connect("o1", directional_lower_wg.ports["o2"])
        right_top_taper.connect("o1", right_top_s.ports["o2"])
        right_bottom_taper.connect("o1", right_bottom_s.ports["o2"])
        c.add_port("o1", port=left_bottom_taper.ports["o1"])
        c.add_port("o2", port=left_top_taper.ports["o1"])
        c.add_port("o3", port=right_top_taper.ports["o2"])
        c.add_port("o4", port=right_bottom_taper.ports["o2"])
    else:
        directional_upper_wg.center = (0, width_inner / 2 + gap / 2)
        directional_lower_wg.center = (0, -width_inner / 2 - gap / 2)
        left_top_s.connect("o2", directional_lower_wg.ports["o1"])
        left_bottom_s.connect("o2", directional_upper_wg.ports["o1"])
        left_top_taper.connect("o2", left_top_s.ports["o1"])
        left_bottom_taper.connect("o2", left_bottom_s.ports["o1"])
        right_top_s.connect("o1", directional_upper_wg.ports["o2"])
        right_bottom_s.connect("o1", directional_lower_wg.ports["o2"])
        right_top_taper.connect("o1", right_top_s.ports["o2"])
        right_bottom_taper.connect("o1", right_bottom_s.ports["o2"])
        c.add_port("o1", port=left_bottom_taper.ports["o1"])
        c.add_port("o2", port=left_top_taper.ports["o1"])
        c.add_port("o3", port=right_top_taper.ports["o2"])
        c.add_port("o4", port=right_bottom_taper.ports["o2"])
    return Utils.pos_neg_seperate(c)



if __name__ == "__main__":
    # c = coupler_adiabatic_full(coupling_length=100, dx=10, dy=10, gap=0.2, dw=1, width=3)
    # c.draw_ports()
    c = coupler_adiabatic_50(
        l_left_taper=20.0,
        l_left_s=40,
        l_coupler_taper=0,
        l_coupler_directional=30.0,
        l_right_s=40,
        l_right_taper=20.0,
        gap=0.2,
        width=1,
        width_inner=0.5,
        dw=0,
        input_wg_sep=20,
        output_wg_sep=20,
        buffer=3.0
    )
    c.draw_ports()
    c.show()