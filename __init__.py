"""YanglabPDK public package interface.

This package provides lab-specific layer definitions, cross sections, utilities,
and reusable photonic components on top of gdsfactory.  The top-level namespace
keeps the most frequently used modules available as:

- `YanglabPDK.LAYER`
- `YanglabPDK.Utils`
- `YanglabPDK.Sections`
"""

import gdsfactory as gf
from YanglabPDK import YanglabLayerStack as LayerStack

LAYER = LayerStack.YanglabLayerMap

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

gf.config.rich_output()
# gf.CONF.logfilter.level = "CRITICAL"


__all__ = [
    "LAYER",
    "Utils",
    "Sections",
]
