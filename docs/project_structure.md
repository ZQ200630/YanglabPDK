# Project Structure

YanglabPDK is organized as a thin lab-specific layer above gdsfactory.  The
source tree is intentionally grouped by design responsibility rather than by
mask project.

```text
YanglabPDK/
|-- __init__.py
|-- YanglabLayerStack.py
|-- YanglabSections.py
|-- YanglabUtils.py
|-- components/
|   |-- bends/
|   |-- cavities/
|   |-- couplers/
|   |-- filters/
|   |-- lasers/
|   |-- metals/
|   |-- mmis/
|   |-- mzis/
|   |-- reflectors/
|   |-- shapes/
|   |-- spirals/
|   |-- tapers/
|   |-- utils/
|   `-- waveguides/
`-- docs/
```

## Core Modules

`YanglabLayerStack.py`

Defines symbolic layer names.  This is the first file to update when the lab
adds a new process layer or needs to reserve a layer number for layout metadata.

`YanglabSections.py`

Defines reusable cross sections.  Most waveguide-like devices build on these
sections rather than constructing `gf.Section` objects directly in every
component file.

`YanglabUtils.py`

Contains layout post-processing helpers.  These utilities are the bridge
between convenient gdsfactory-generated geometry and the layer conventions
needed by the lab fabrication flow.

## Components

The `components/` folder contains public reusable cells.  Each subpackage should
export its public functions from its own `__init__.py`, which allows scripts to
use imports such as:

```python
from YanglabPDK.components.waveguides import straight
from YanglabPDK.components.couplers import coupler
```

When adding a new device family, create a new subfolder only if the function
does not naturally belong to an existing family.
