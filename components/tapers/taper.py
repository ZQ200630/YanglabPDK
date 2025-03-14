import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

#TODO: Taper function has some problems, need to be fixed

@gf.cell
def taper(length=10.0, width1=1, width2=1, buffer=3) -> gf.Component:
    """Linear taper, which tapers only the main cross section section.

    Args:
        length: taper length.
        width1: width of the west/left port.
        width2: width of the east/right port. Defaults to width1.
        buffer: buffer width for positive tone resist (um)
    """
    port_names=['o1', 'o2']
    port_types=['optical', 'optical']
    with_two_ports=True
    c = gf.Component()
    if (width1 <= width2):
        c = gf.components.taper(length=length, width1=width1, width2=width2, with_two_ports=with_two_ports, port_names=port_names, port_types=port_types, cross_section=Sections.pos_neg_resist(width=width1, buffer=buffer))
    else:
        port_names.reverse()
        c = gf.components.taper(length=length, width1=width2, width2=width1, with_two_ports=with_two_ports, port_names=port_names, port_types=port_types, cross_section=Sections.pos_neg_resist(width=width2, buffer=buffer))
        c.locked = False
        c = c.rotate(180)
        c.show()
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    c = taper(length=100, width1=5, width2=2)
    # c.show()