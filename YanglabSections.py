"""Common gdsfactory cross sections for Yang Lab layouts.

Most optical waveguide cells in this package use paired positive/negative resist
sections.  The negative resist section usually represents the waveguide core,
while positive resist buffer sections are used for process compensation and are
resolved later by `YanglabUtils.pos_neg_seperate`.
"""

import gdsfactory as gf

from YanglabPDK import *


@gf.xsection
def pos_neg_resist(width=1, buffer=3, radius=0) -> gf.CrossSection:
    """Return the default positive/negative resist waveguide cross section.

    Args:
        width: Negative-resist core width in microns.
        buffer: Width of each positive-resist side buffer in microns.
        radius: Optional bend radius metadata passed into the cross section.

    Returns:
        Cross section with optical ports `o1` and `o2` on the core section.
    """
    s0 = gf.Section(width=width, offset=0, layer=LAYER.NR, name='core', port_names=["o1", "o2"])
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=LAYER.PR, name='buffer1')
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=LAYER.PR, name='buffer2')
    x = gf.CrossSection(sections=[s0, s1, s2], radius=radius)
    return x


@gf.xsection
def pos_neg_resist_with_layer(width=1, buffer=3, layer1=LAYER.PR, layer2=LAYER.NR) -> gf.CrossSection:
    """Return a positive/negative resist cross section with configurable layers.

    Args:
        width: Center section width in microns.
        buffer: Width of each side buffer in microns.
        layer1: Layer used for the side buffers.
        layer2: Layer used for the center waveguide section.
    """
    s0 = gf.Section(width=width, offset=0, layer=layer2, port_names=["o1", "o2"])
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=layer1)
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=layer1)
    x = gf.CrossSection(sections=[s0, s1, s2])
    return x


@gf.xsection
def pos_neg_resist_without_port(width=1, buffer=3) -> gf.CrossSection:
    """Return the default resist cross section without ports.

    Use this for helper geometry that should not expose optical connectivity.
    """
    s0 = gf.Section(width=width, offset=0, layer=LAYER.NR)
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=LAYER.PR)
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=LAYER.PR)
    x = gf.CrossSection(sections=[s0, s1, s2])
    return x


@gf.xsection
def double_layer_resist(width_top=1, width_bottom=7, layer1=LAYER.PR, layer2=LAYER.NR) -> gf.CrossSection:
    """Return a two-layer resist cross section.

    Args:
        width_top: Width of the top/slot-defining section in microns.
        width_bottom: Width of the bottom/waveguide section in microns.
        layer1: Layer for the top section.
        layer2: Layer for the bottom section.
    """
    s0 = gf.Section(width=width_top, offset=0, layer=layer1, port_names=["o1", "o2"])
    s1 = gf.Section(width=width_bottom, offset=0, layer=layer2)
    x = gf.CrossSection(sections=[s0, s1])
    return x


def pos_neg_Section_Tuple(width=1, buffer=3):
    """Return the default positive/negative resist sections as a tuple.

    This helper is useful when another cross section needs to compose these
    sections manually instead of receiving a complete `gf.CrossSection`.
    """
    s0 = gf.Section(width=width, offset=0, layer=LAYER.NR)
    s1 = gf.Section(width=buffer, offset=(buffer+width)/2, layer=LAYER.PR)
    s2 = gf.Section(width=buffer, offset=-(buffer+width)/2, layer=LAYER.PR)
    return (s0, s1, s2)
