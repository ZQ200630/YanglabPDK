import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections
from YanglabPDK import LAYER
from YanglabPDK.components.tapers.taper import taper
from YanglabPDK.components.waveguides.straight import straight

@gf.cell
def mmi1x2(
    width: float | None = 1,
    width_taper: float = 1.0,
    length_taper: float = 10.0,
    length_mmi: float = 5.5,
    width_mmi: float = 2.5,
    gap_mmi: float = 0.25,
    buffer: float = 3.0,
) -> gf.Component:
    r"""1x2 MultiMode Interferometer (MMI).

    Args:
        width: input and output straight width. Defaults to cross_section width.
        width_taper: interface between input straights and mmi region.
        length_taper: into the mmi region.
        length_mmi: in x direction.
        width_mmi: in y direction.
        gap_mmi:  gap between tapered wg.
        buffer: Buffer width for positive tone resist


    .. code::

               length_mmi
                <------>
                ________
               |        |
               |         \__
               |          __  o2
            __/          /_ _ _ _
         o1 __          | _ _ _ _| gap_mmi
              \          \__
               |          __  o3
               |         /
               |________|

             <->
        length_taper

    """
    c = gf.Component()
    gap_mmi = gf.snap.snap_to_grid(gap_mmi, grid_factor=2)
    x = Sections.pos_neg_resist(width=width, buffer=buffer)
    width = width or x.width



    _taper_left = taper(
        length=length_taper,
        width1=width,
        width2=width_taper,
        buffer=buffer+(width_mmi-width_taper)/2,
        is_buffer_aligned=True
    )

    _taper_right = taper(
        length=length_taper,
        width1=width_taper,
        width2=width,
        buffer=buffer+(width_mmi-2*width_taper-gap_mmi)/2,
        is_buffer_aligned=True
    )

    a = gap_mmi / 2 + width_taper / 2
    _ = c << straight(length=length_mmi, width=width_mmi, buffer=buffer)

    temp_component = gf.Component()

    ports = [
        temp_component.add_port(
            name="o1",
            orientation=180,
            center=(0, 0),
            width=width_taper,
            layer=LAYER.NR,
            cross_section=x,
        ),
        temp_component.add_port(
            name="o2",
            orientation=0,
            center=(+length_mmi, +a),
            width=width_taper,
            layer=LAYER.NR,
            cross_section=x,
        ),
        temp_component.add_port(
            name="o3",
            orientation=0,
            center=(+length_mmi, -a),
            width=width_taper,
            layer=LAYER.NR,
            cross_section=x,
        ),
    ]

    taper_1 = c << _taper_left
    taper_2 = c << _taper_right
    taper_3 = c << _taper_right

    taper_1.connect(port="o2", other=temp_component.ports["o1"], allow_width_mismatch=True)
    taper_2.connect(port="o1", other=temp_component.ports["o2"], allow_width_mismatch=True)
    taper_3.connect(port="o1", other=temp_component.ports["o3"], allow_width_mismatch=True)

    c.add_port(name="o1", port=taper_1.ports["o1"])
    c.add_port(name="o2", port=taper_2.ports["o2"])
    c.add_port(name="o3", port=taper_3.ports["o2"])

    c.flatten()
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    c = mmi1x2(width=1.5, width_taper=3.6, width_mmi=10, length_mmi=58, length_taper=50, gap_mmi=1.8)
    c.draw_ports()
    c.show()