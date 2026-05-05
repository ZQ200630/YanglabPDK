# Generated Component Reference

This page is generated from the `components/` source tree.  Do not edit it by hand.

## Contents

- <a href="#bends">bends</a>
- <a href="#cavities">cavities</a>
- <a href="#couplers">couplers</a>
- <a href="#filters">filters</a>
- <a href="#lasers">lasers</a>
- <a href="#metals">metals</a>
- <a href="#mmis">mmis</a>
- <a href="#mzis">mzis</a>
- <a href="#reflectors">reflectors</a>
- <a href="#shapes">shapes</a>
- <a href="#spirals">spirals</a>
- <a href="#tapers">tapers</a>
- <a href="#utils">utils</a>
- <a href="#waveguides">waveguides</a>

## bends

### `YanglabPDK.components.bends.bend_bezier.bend_bezier`

```python
YanglabPDK.components.bends.bend_bezier.bend_bezier(control_points: Coordinates=[[0.0, 0.0], [5.0, 0.0], [50, 5], [100.0, 20]], npoints: int=201, with_manhattan_facing_angles=True, start_angle: int | None=None, end_angle: int | None=None, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/bends/bend_bezier.py:9`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns Bezier bend.

**Parameters:**

- **control_points** (Coordinates) - list of points. Defaults to `[[0.0, 0.0], [5.0, 0.0], [50, 5], [100.0, 20]]`.
- **npoints** (int) - number of points varying between 0 and 1. Defaults to `201`.
- **with_manhattan_facing_angles** (Any) - bool. Defaults to `True`.
- **start_angle** (int | None) - optional start angle in deg. Defaults to `None`.
- **end_angle** (int | None) - optional end angle in deg. Defaults to `None`.
- **width** (float) - width to use. Defaults to cross_section.width. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.bends.bend_circular.bend_circular`

```python
YanglabPDK.components.bends.bend_circular.bend_circular(radius: float=100, angle: float=90, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/bends/bend_circular.py:7`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns a radial arc.

**Parameters:**

- **radius** (float) - in um. Defaults to cross_section_radius. Defaults to `100`.
- **angle** (float) - angle of arc (degrees). Defaults to `90`.
- **width** (float) - width to use. Defaults to cross_section.width. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.bends.bend_euler.bend_euler`

```python
YanglabPDK.components.bends.bend_euler.bend_euler(radius: float=100, angle: float=90, p: float=0.5, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/bends/bend_euler.py:7`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Regular degree euler bend.

**Parameters:**

- **radius** (float) - in um. Defaults to cross_section_radius. Defaults to `100`.
- **angle** (float) - total angle of the curve. Defaults to `90`.
- **p** (float) - Proportion of the curve that is an Euler curve. Defaults to `0.5`.
- **width** (float) - width to use. Defaults to cross_section.width. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.bends.bend_euler.bend_euler_s`

```python
YanglabPDK.components.bends.bend_euler.bend_euler_s(radius: float=100, angle: float=30, p: float=0.5, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/bends/bend_euler.py:29`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Sbend made of 2 euler bends.

**Parameters:**

- **radius** (float) - in um. Defaults to cross_section_radius. Defaults to `100`.
- **angle** (float) - total angle of the curve Defaults to `30`.
- **p** (float) - Proportion of the curve that is an Euler curve. Defaults to `0.5`.
- **width** (float) - width to use. Defaults to cross_section.width. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.bends.bend_s.bend_s`

```python
YanglabPDK.components.bends.bend_s.bend_s(size: Size=[10, 10], width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/bends/bend_s.py:9`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return S bend with bezier curve. stores min_bend_radius property in self.info['min_bend_radius'] min_bend_radius depends on height and length

**Parameters:**

- **size** (Size) - in x and y direction. Defaults to `[10, 10]`.
- **width** (float) - width to use. Defaults to cross_section.width. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## cavities

### `YanglabPDK.components.cavities.cavity_fp.cavity_fp`

```python
YanglabPDK.components.cavities.cavity_fp.cavity_fp(dbr=dbr(w1=1, w2=0.5, n=20), coupler=coupler(dy=8, dx=20))
```

[source: `components/cavities/cavity_fp.py:9`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a Fabry-Perot cavity assembled from DBR and coupler cells.

**Parameters:**

- **dbr** (Any) - DBR mirror component used in the cavity. Defaults to `dbr(w1=1, w2=0.5, n=20)`.
- **coupler** (Any) - Coupler component connected to the cavity. Defaults to `coupler(dy=8, dx=20)`.

**Returns:**

Component containing the assembled Fabry-Perot cavity.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.four_parallel_rings_1_in_1`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.four_parallel_rings_1_in_1(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:76`]

**Preview:** skipped - function has required arguments without defaults

Create a four parallel rings 1 in 1 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_105_210`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_105_210(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:155`]

**Preview:** skipped - function has required arguments without defaults

Create a parallel rings with parameters 105 210 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_210_320`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_210_320(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:175`]

**Preview:** skipped - function has required arguments without defaults

Create a parallel rings with parameters 210 320 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_80_105`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_80_105(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:135`]

**Preview:** skipped - function has required arguments without defaults

Create a parallel rings with parameters 80 105 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_all_in_one`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_all_in_one(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:195`]

**Preview:** skipped - function has required arguments without defaults

Returns parallel rings array with optimized spatial arrangement.

**Parameters:**

- **parameters** (Any) - list of parameters for each ring, need radius, gap, width_wg, width_ring, total_length

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `__all__`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_l_80`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.parallel_rings_with_parameters_l_80(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:115`]

**Preview:** skipped - function has required arguments without defaults

Create a parallel rings with parameters l 80 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.pulley_six_parallel_rings_3_in_2`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.pulley_six_parallel_rings_3_in_2(parameters, comments=None)
```

[source: `components/cavities/cavity_wgm/ring_array.py:237`]

**Preview:** skipped - function has required arguments without defaults

Create a pulley six parallel rings 3 in 2 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.
- **comments** (Any) - Optional text label added to the layout. Defaults to `None`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.six_parallel_rings_2_in_1`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.six_parallel_rings_2_in_1(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:20`]

**Preview:** skipped - function has required arguments without defaults

Create a six parallel rings 2 in 1 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.six_parallel_rings_3_in_2`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.six_parallel_rings_3_in_2(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:44`]

**Preview:** skipped - function has required arguments without defaults

Create a six parallel rings 3 in 2 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array.three_parallel_rings_1_in_2`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array.three_parallel_rings_1_in_2(parameters)
```

[source: `components/cavities/cavity_wgm/ring_array.py:97`]

**Preview:** skipped - function has required arguments without defaults

Create a three parallel rings 1 in 2 component.

**Parameters:**

- **parameters** (Any) - List of ring parameter dictionaries. Each dictionary should include radius, gap, width_wg, width_ring, and total_length; pulley variants also use angle.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `component return`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.pulley_ring_with_wg_3_in_2`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.pulley_ring_with_wg_3_in_2(radius=80, gap=0.5, width_wg=1, width_ring=1, angle=20, offset=0, total_length=12000) -> gf.Component
```

[source: `components/cavities/cavity_wgm/ring_array_blocks.py:215`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a pulley ring with waveguides aligned for a 3-in-2 field array.

**Parameters:**

- **radius** (Any) - Ring radius in microns. Defaults to `80`.
- **gap** (Any) - Gap between ring and bus waveguide in microns. Defaults to `0.5`.
- **width_wg** (Any) - Bus waveguide width in microns. Defaults to `1`.
- **width_ring** (Any) - Ring waveguide width in microns. Defaults to `1`.
- **angle** (Any) - Pulley coupling angle in degrees. Defaults to `20`.
- **offset** (Any) - Horizontal offset from the field edge in microns. Defaults to `0`.
- **total_length** (Any) - Total component length in microns. Defaults to `12000`.

**Returns:**

Component with the pulley ring and routed bus waveguide.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_1_in_1`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_1_in_1(radius: float=180, gap: float=0.5, width_wg: float=1, width_ring: float=1, offset: float=2000, total_length: float=12000) -> gf.Component
```

[source: `components/cavities/cavity_wgm/ring_array_blocks.py:113`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns single ring with waveguides aligned to writing field, for 1 ring in 1 field array.

**Parameters:**

- **radius** (float) - Ring radius. Defaults to `180`.
- **gap** (float) - Ring - waveguide gap. Defaults to `0.5`.
- **width_wg** (float) - Waveguide width. Defaults to `1`.
- **width_ring** (float) - Ring width. Defaults to `1`.
- **offset** (float) - Offset from the left edge of the field. Defaults to `2000`.
- **total_length** (float) - Total length of the component. Defaults to `12000`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_1_in_2`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_1_in_2(radius: float=300, gap: float=0.5, width_wg: float=1, width_ring: float=1.5, offset: float=0, total_length: float=10000) -> gf.Component
```

[source: `components/cavities/cavity_wgm/ring_array_blocks.py:163`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns single ring with waveguides aligned to writing field, for 1 ring in 2 field array.

**Parameters:**

- **radius** (float) - Ring radius. Defaults to `300`.
- **gap** (float) - Ring - waveguide gap. Defaults to `0.5`.
- **width_wg** (float) - Waveguide width. Defaults to `1`.
- **width_ring** (float) - Ring width. Defaults to `1.5`.
- **offset** (float) - Offset from the left edge of the field. Defaults to `0`.
- **total_length** (float) - Total length of the component. Defaults to `10000`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_2_in_1`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_2_in_1(radius: float=80, gap: float=0.5, width_wg: float=1, width_ring: float=1, offset: float=0, total_length: float=12000) -> gf.Component
```

[source: `components/cavities/cavity_wgm/ring_array_blocks.py:12`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns single ring with waveguides aligh to writing field, for 2 rings in 1 field array.

**Parameters:**

- **radius** (float) - Ring radius. Defaults to `80`.
- **gap** (float) - Ring - waveguide gap. Defaults to `0.5`.
- **width_wg** (float) - Waveguide width. Defaults to `1`.
- **width_ring** (float) - Ring width. Defaults to `1`.
- **offset** (float) - Offset from the left edge of the field. Defaults to `0`.
- **total_length** (float) - Total length of the component. Defaults to `12000`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_3_in_2`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_array_blocks.ring_with_wg_3_in_2(radius: float=105, gap: float=0.5, width_wg: float=1, width_ring: float=1, offset: float=0, total_length: float=12000) -> gf.Component
```

[source: `components/cavities/cavity_wgm/ring_array_blocks.py:63`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns single ring with waveguides aligned to writing field, 3 rings in 2 field array.

**Parameters:**

- **radius** (float) - Ring radius. Defaults to `105`.
- **gap** (float) - Ring - waveguide gap. Defaults to `0.5`.
- **width_wg** (float) - Waveguide width. Defaults to `1`.
- **width_ring** (float) - Ring width. Defaults to `1`.
- **offset** (float) - Offset from the left edge of the field. Defaults to `0`.
- **total_length** (float) - Total length of the component. Defaults to `12000`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.half_ring_asymmetry`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.half_ring_asymmetry(radius=100, short_width=0.6, long_width=2, buffer=3)
```

[source: `components/cavities/cavity_wgm/ring_asymmetry.py:12`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return one half of an asymmetric-width ring.

**Parameters:**

- **radius** (Any) - Centerline radius in microns. Defaults to `100`.
- **short_width** (Any) - Narrow side width in microns. Defaults to `0.6`.
- **long_width** (Any) - Wide side width in microns. Defaults to `2`.
- **buffer** (Any) - Positive-resist buffer width in microns. Defaults to `3`.

**Returns:**

Component with optical ports `o1` and `o2`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_assymmetry_add_drop`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_assymmetry_add_drop(radius=100, short_width=0.6, gap=0.6, wg_width=0.8, width=1, long_width=2, racetrack_len=200, buffer=3)
```

[source: `components/cavities/cavity_wgm/ring_asymmetry.py:187`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an asymmetric add-drop racetrack ring.

**Parameters:**

- **radius** (Any) - Bend radius in microns. Defaults to `100`.
- **short_width** (Any) - Narrow ring width in microns. Defaults to `0.6`.
- **gap** (Any) - Coupling gap in microns. Defaults to `0.6`.
- **wg_width** (Any) - Narrow bus waveguide width in microns. Defaults to `0.8`.
- **width** (Any) - Access waveguide width in microns. Defaults to `1`.
- **long_width** (Any) - Wide ring width in microns. Defaults to `2`.
- **racetrack_len** (Any) - Straight ring section length in microns. Defaults to `200`.
- **buffer** (Any) - Positive-resist buffer width in microns. Defaults to `3`.

**Returns:**

Component with four optical ports `o1`, `o2`, `o3`, and `o4`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_assymmetry_add_drop_w_heater`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_assymmetry_add_drop_w_heater(radius=100, short_width=0.6, gap=0.6, wg_width=0.8, width=1, long_width=2, buffer=3, w: float=0.5, theta0: float=30, theta1: float=30.0, lead_len: float=3, elef_taper_len: float=5.0, pad_size: tuple[float, float]=(11, 11), add_teeth: bool=False, tooth_len: float=3.0, tooth_w: float=1.2)
```

[source: `components/cavities/cavity_wgm/ring_asymmetry.py:225`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an asymmetric add-drop ring with an integrated microheater.

**Parameters:**

- **radius** (Any) - Bend radius in microns. Defaults to `100`.
- **short_width** (Any) - Narrow ring width in microns. Defaults to `0.6`.
- **gap** (Any) - Coupling gap in microns. Defaults to `0.6`.
- **wg_width** (Any) - Narrow bus waveguide width in microns. Defaults to `0.8`.
- **width** (Any) - Access waveguide width in microns. Defaults to `1`.
- **long_width** (Any) - Wide ring width in microns. Defaults to `2`.
- **buffer** (Any) - Positive-resist buffer width in microns. Defaults to `3`.
- **w** (float) - Heater width in microns. Defaults to `0.5`.
- **theta0** (float) - Heater start angle in degrees. Defaults to `30`.
- **theta1** (float) - Heater end angle in degrees. Defaults to `30.0`.
- **lead_len** (float) - Straight heater lead length in microns. Defaults to `3`.
- **elef_taper_len** (float) - Electrical taper length in microns. Defaults to `5.0`.
- **pad_size** (tuple[float, float]) - Electrical pad size `(x, y)` in microns. Defaults to `(11, 11)`.
- **add_teeth** (bool) - Whether to add meander teeth along the heater. Defaults to `False`.
- **tooth_len** (float) - Tooth length in microns. Defaults to `3.0`.
- **tooth_w** (float) - Tooth width in microns. Defaults to `1.2`.

**Returns:**

Component with four optical ports and electrical heater ports.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_asymmetry`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_asymmetry(radius=100, short_width=0.6, gap=0.6, wg_width=1, long_width=2, racetrack_len=200, buffer=3)
```

[source: `components/cavities/cavity_wgm/ring_asymmetry.py:162`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an asymmetric racetrack ring coupled to one bus waveguide.

**Parameters:**

- **radius** (Any) - Bend radius in microns. Defaults to `100`.
- **short_width** (Any) - Narrow ring width in microns. Defaults to `0.6`.
- **gap** (Any) - Ring-to-waveguide gap in microns. Defaults to `0.6`.
- **wg_width** (Any) - Bus waveguide width in microns. Defaults to `1`.
- **long_width** (Any) - Wide ring width in microns. Defaults to `2`.
- **racetrack_len** (Any) - Straight section length in microns. Defaults to `200`.
- **buffer** (Any) - Positive-resist buffer width in microns. Defaults to `3`.

**Returns:**

Component with bus waveguide ports `o1` and `o2`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_asymmetry_only`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_asymmetry_only(radius=100, short_width=0.6, long_width=2, racetrack_len=200, buffer=3)
```

[source: `components/cavities/cavity_wgm/ring_asymmetry.py:77`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an asymmetric racetrack ring without bus waveguides.

**Parameters:**

- **radius** (Any) - Bend radius in microns. Defaults to `100`.
- **short_width** (Any) - Narrow ring width in microns. Defaults to `0.6`.
- **long_width** (Any) - Wide ring width in microns. Defaults to `2`.
- **racetrack_len** (Any) - Straight section length in microns. Defaults to `200`.
- **buffer** (Any) - Positive-resist buffer width in microns. Defaults to `3`.

**Returns:**

Component with optical ports `o1` and `o2`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_asymmetry_only_w_heater`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_asymmetry.ring_asymmetry_only_w_heater(radius=100, short_width=0.6, long_width=2, buffer=3, w: float=0.5, theta0: float=30, theta1: float=30.0, lead_len: float=3, elef_taper_len: float=5.0, pad_size: tuple[float, float]=(11, 11), add_teeth: bool=False, tooth_len: float=3.0, tooth_w: float=1.2)
```

[source: `components/cavities/cavity_wgm/ring_asymmetry.py:106`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an asymmetric ring with integrated arc microheater.

**Parameters:**

- **radius** (Any) - Bend radius in microns. Defaults to `100`.
- **short_width** (Any) - Narrow ring width in microns. Defaults to `0.6`.
- **long_width** (Any) - Wide ring width in microns. Defaults to `2`.
- **buffer** (Any) - Positive-resist buffer width in microns. Defaults to `3`.
- **w** (float) - Heater width in microns. Defaults to `0.5`.
- **theta0** (float) - Heater start angle in degrees. Defaults to `30`.
- **theta1** (float) - Heater end angle in degrees. Defaults to `30.0`.
- **lead_len** (float) - Straight heater lead length in microns. Defaults to `3`.
- **elef_taper_len** (float) - Electrical taper length in microns. Defaults to `5.0`.
- **pad_size** (tuple[float, float]) - Electrical pad size `(x, y)` in microns. Defaults to `(11, 11)`.
- **add_teeth** (bool) - Whether to add meander teeth along the heater. Defaults to `False`.
- **tooth_len** (float) - Tooth length in microns. Defaults to `3.0`.
- **tooth_w** (float) - Tooth width in microns. Defaults to `1.2`.

**Returns:**

Component with optical and electrical ports.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.cavities.cavity_wgm.ring_pulley.ring_single_pulley`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_pulley.ring_single_pulley(radius: float=100, gap: float=0.2, coupling_angle_coverage: float=90, length_x: float=0.6, length_y: float=0.6, width_inner: float=1, width_outer: float=1, buffer: float=3, length_extension_left: float=500, length_extension_right: float=500) -> gf.Component
```

[source: `components/cavities/cavity_wgm/ring_pulley.py:12`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns ring with curved coupler. TODO: enable euler bends.

**Parameters:**

- **radius** (float) - um. Defaults to `100`.
- **gap** (float) - um. Defaults to `0.2`.
- **coupling_angle_coverage** (float) - No description available. Defaults to `90`.
- **length_x** (float) - horizontal straight length. Defaults to `0.6`.
- **length_y** (float) - vertical straight length. Defaults to `0.6`.
- **width_inner** (float) - No description available. Defaults to `1`.
- **width_outer** (float) - No description available. Defaults to `1`.
- **buffer** (float) - No description available. Defaults to `3`.
- **length_extension_left** (float) - No description available. Defaults to `500`.
- **length_extension_right** (float) - No description available. Defaults to `500`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.cavities.cavity_wgm.ring_single.ring_single`

```python
YanglabPDK.components.cavities.cavity_wgm.ring_single.ring_single(gap: float=0.2, radius: float=10.0, length_x: float=4.0, length_y: float=0.6, width_wg: float=1, width_bend: float=1, buffer: float=3, length_extension_left: float=500, length_extension_right: float=500) -> gf.Component
```

[source: `components/cavities/cavity_wgm/ring_single.py:13`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns a single ring. ring coupler (cb: bottom) connects to two vertical straights (sl: left, sr: right), two bends (bl, br) and horizontal straight (wg: top)

**Parameters:**

- **gap** (float) - gap between for coupler. Defaults to `0.2`.
- **radius** (float) - for the bend and coupler. Defaults to `10.0`.
- **length_x** (float) - ring coupler length. Defaults to `4.0`.
- **length_y** (float) - vertical straight length. Defaults to `0.6`.
- **width_wg** (float) - No description available. Defaults to `1`.
- **width_bend** (float) - No description available. Defaults to `1`.
- **buffer** (float) - No description available. Defaults to `3`.
- **length_extension_left** (float) - No description available. Defaults to `500`.
- **length_extension_right** (float) - No description available. Defaults to `500`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## couplers

### `YanglabPDK.components.couplers.coupler.coupler`

```python
YanglabPDK.components.couplers.coupler.coupler(gap: float=0.236, length: float=20.0, dy: float=4.0, dx: float=10.0, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler.py:37`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Symmetric coupler.

**Parameters:**

- **gap** (float) - between straights in um. Defaults to `0.236`.
- **length** (float) - of coupling region in um. Defaults to `20.0`.
- **dy** (float) - port to port vertical spacing in um. Defaults to `4.0`.
- **dx** (float) - length of bend in x direction in um. Defaults to `10.0`.
- **width** (float) - No description available. Defaults to `1`.
- **buffer** (float) - No description available. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler.coupler_straight`

```python
YanglabPDK.components.couplers.coupler.coupler_straight(length: float=10.0, gap: float=0.27, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler.py:8`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Coupler_straight with two parallel straights.

**Parameters:**

- **length** (float) - of straight. Defaults to `10.0`.
- **gap** (float) - between straights. Defaults to `0.27`.
- **width** (float) - of the straights. Defaults to `1`.
- **buffer** (float) - buffer. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler90.coupler90circular`

```python
YanglabPDK.components.couplers.coupler90.coupler90circular(gap: float=0.2, radius: float=100.0, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler90.py:56`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Straight coupled to a bend.

**Parameters:**

- **gap** (float) - um. Defaults to `0.2`.
- **radius** (float) - um. Defaults to `100.0`.
- **width** (float) - um. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.couplers.coupler90.coupler90circular_asymmetric`

```python
YanglabPDK.components.couplers.coupler90.coupler90circular_asymmetric(gap: float=0.2, radius: float=100.0, width_wg: float=1, width_bend: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler90.py:101`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Straight coupled to a bend.

**Parameters:**

- **gap** (float) - um. Defaults to `0.2`.
- **radius** (float) - um. Defaults to `100.0`.
- **width_wg** (float) - width of bus waveguide um. Defaults to `1`.
- **width_bend** (float) - width of bend um. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler90.coupler90euler`

```python
YanglabPDK.components.couplers.coupler90.coupler90euler(gap: float=0.2, radius: float=100.0, p: float=0.5, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler90.py:9`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Straight coupled to a bend.

**Parameters:**

- **gap** (float) - um. Defaults to `0.2`.
- **radius** (float) - um. Defaults to `100.0`.
- **p** (float) - proportion of the curve that is an Euler curve. Defaults to `0.5`.
- **width** (float) - um. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.couplers.coupler90bend.coupler90bend`

```python
YanglabPDK.components.couplers.coupler90bend.coupler90bend(radius: float=100.0, gap: float=0.2, width_outter: float=1, width_inner: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler90bend.py:7`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns 2 coupled bends.

**Parameters:**

- **radius** (float) - um. Defaults to `100.0`.
- **gap** (float) - um. Defaults to `0.2`.
- **width_outter** (float) - outter bend width um. Defaults to `1`.
- **width_inner** (float) - inner bend width um. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler_adiabatic.coupler_adiabatic_50`

```python
YanglabPDK.components.couplers.coupler_adiabatic.coupler_adiabatic_50(l_left_taper: float=20.0, l_left_s: float=20.0, l_coupler_taper: float=50.0, l_coupler_directional: float=30.0, l_right_s: float=30.0, l_right_taper: float=20.0, gap: float=1.0, width: float=0.5, width_inner: float=0.5, dw: float=0.1, input_wg_sep: float=3.0, output_wg_sep: float=3.0, buffer: float=3.0) -> gf.Component
```

[source: `components/couplers/coupler_adiabatic.py:96`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns 50/50 adiabatic coupler. Design based on asymmetric adiabatic 3dB coupler designs, such as: - https://doi.org/10.1364/CLEO.2010.CThAA2 - https://doi.org/10.1364/CLEO_SI.2017.SF1I.5 - https://doi.org/10.1364/CLEO_SI.2018.STh4B.4 The coupler consists of: 1. Left taper region (l_left_taper): input waveguides taper by +dw and -dw. 2. Left S-bend region (l_left_s): constant, unbalanced widths. 3. Coupler taper region (l_coupler_taper): asymmetric waveguides gradually come together. 4. Directional coupler region (l_coupler_directional): coupling occurs, widths become equal. 5. Right S-bend region (l_right_s): output waveguides separate. 6. Right taper region (l_right_taper): waveguides taper back to original width.

**Parameters:**

- **l_left_taper** (float) - Length of the left taper region (um). Defaults to `20.0`.
- **l_left_s** (float) - Length of the left S-bend region (um). Defaults to `20.0`.
- **l_coupler_taper** (float) - Length of the coupler taper region (um). Defaults to `50.0`.
- **l_coupler_directional** (float) - Length of the directional coupler region (um). Defaults to `30.0`.
- **l_right_s** (float) - Length of the right S-bend region (um). Defaults to `30.0`.
- **l_right_taper** (float) - Length of the right taper region (um). Defaults to `20.0`.
- **gap** (float) - Gap between the two waveguides in the coupling region (um). Defaults to `1.0`.
- **width** (float) - Width of the waveguides (um). Defaults to `0.5`.
- **width_inner** (float) - Width of the inner waveguides in the coupling region (um). Defaults to `0.5`.
- **dw** (float) - Delta width; top arm tapers to width+dw, bottom to width-dw (um). Defaults to `0.1`.
- **input_wg_sep** (float) - Separation between input waveguides, center-to-center (um). Defaults to `3.0`.
- **output_wg_sep** (float) - Separation between output waveguides, center-to-center (um). Defaults to `3.0`.
- **buffer** (float) - Buffer around the waveguides (um). Defaults to `3.0`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.couplers.coupler_adiabatic.coupler_adiabatic_full`

```python
YanglabPDK.components.couplers.coupler_adiabatic.coupler_adiabatic_full(coupling_length: float=40.0, dx: float=10.0, dy: float=4.8, gap: float=0.5, dw: float=0.1, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler_adiabatic.py:9`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Adiabatic Full coupler. Design based on asymmetric adiabatic full coupler designs, such as the one reported in 'Integrated Optic Adiabatic Devices on Silicon' by Y. Shani, et al (IEEE Journal of Quantum Electronics, Vol. 27, No. 3 March 1991). 1. is the first half of the input S-bend straight where the input straights widths taper by +dw and -dw, 2. is the second half of the S-bend straight with constant, unbalanced widths, 3. is the coupling region where the straights from unbalanced widths to balanced widths to reverse polarity unbalanced widths, 4. is the fixed width straight that curves away from the coupling region, 5.is the final curve where the straights taper back to the regular width specified in the straight template.

**Parameters:**

- **coupling_length** (float) - Length of the coupling region in um. Defaults to `40.0`.
- **dx** (float) - Length of the bend regions in um. Defaults to `10.0`.
- **dy** (float) - Port-to-port distance between the bend regions in um. Defaults to `4.8`.
- **gap** (float) - Distance between the two straights in um. Defaults to `0.5`.
- **dw** (float) - delta width. Top arm tapers to width - dw, bottom to width + dw in um. Defaults to `0.1`.
- **width** (float) - width of the waveguide. If None, it will use the width of the cross_section. Defaults to `1`.
- **buffer** (float) - buffer. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.couplers.coupler_asymmetric.coupler_asymmetric`

```python
YanglabPDK.components.couplers.coupler_asymmetric.coupler_asymmetric(gap: float=0.234, dy: float=2.5, dx: float=10.0, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler_asymmetric.py:7`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Bend coupled to straight waveguide.

**Parameters:**

- **gap** (float) - um. Defaults to `0.234`.
- **dy** (float) - port to port vertical spacing. Defaults to `2.5`.
- **dx** (float) - bend length in x direction. Defaults to `10.0`.
- **width** (float) - waveguide width in um. Defaults to `1`.
- **buffer** (float) - buffer. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler_bent.coupler_bent`

```python
YanglabPDK.components.couplers.coupler_bent.coupler_bent(radius: float=100, coupler_gap: float=0.2, coupling_angle_coverage: float=120.0, width_inner: float=1, width_outer: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler_bent.py:8`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Compact curved coupler with bezier escape. TODO: fix for euler bends.

**Parameters:**

- **radius** (float) - um. Defaults to `100`.
- **coupler_gap** (float) - No description available. Defaults to `0.2`.
- **coupling_angle_coverage** (float) - No description available. Defaults to `120.0`.
- **width_inner** (float) - No description available. Defaults to `1`.
- **width_outer** (float) - No description available. Defaults to `1`.
- **buffer** (float) - No description available. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler_ring.coupler_halfring`

```python
YanglabPDK.components.couplers.coupler_ring.coupler_halfring(gap: float=0.2, radius: float=5.0, length_x: float=0, width_wg: float=1, width_bend: float=1, buffer: float=3, length_extension_left: float=20, length_extension_right: float=20) -> gf.Component
```

[source: `components/couplers/coupler_ring.py:15`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Coupler for ring.

**Parameters:**

- **gap** (float) - spacing between parallel coupled straight waveguides. Defaults to `0.2`.
- **radius** (float) - of the bends. Defaults to `5.0`.
- **length_x** (float) - length of the parallel coupled straight waveguides. Defaults to `0`.
- **width_wg** (float) - width of the waveguides. Defaults to `1`.
- **width_bend** (float) - width of the bends. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.
- **length_extension_left** (float) - left to extension comparing to center of the ring. Defaults to `20`.
- **length_extension_right** (float) - right to extension comparing to center of the ring. Defaults to `20`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler_ring.coupler_halfring_pulley`

```python
YanglabPDK.components.couplers.coupler_ring.coupler_halfring_pulley(gap: float=0.2, radius: float=5.0, length_x: float=0, width_wg: float=1, width_bend: float=1, covered_angle: float=45, buffer: float=3, length_extension_left: float=20, length_extension_right: float=20) -> gf.Component
```

[source: `components/couplers/coupler_ring.py:101`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Coupler for ring.

**Parameters:**

- **gap** (float) - spacing between parallel coupled straight waveguides. Defaults to `0.2`.
- **radius** (float) - of the bends. Defaults to `5.0`.
- **length_x** (float) - length of the parallel coupled straight waveguides. Defaults to `0`.
- **width_wg** (float) - width of the waveguides. Defaults to `1`.
- **width_bend** (float) - width of the bends. Defaults to `1`.
- **covered_angle** (float) - No description available. Defaults to `45`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.
- **length_extension_left** (float) - left to extension comparing to center of the ring. Defaults to `20`.
- **length_extension_right** (float) - right to extension comparing to center of the ring. Defaults to `20`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.couplers.coupler_straight_asymmetric.coupler_straight_asymmetric`

```python
YanglabPDK.components.couplers.coupler_straight_asymmetric.coupler_straight_asymmetric(length: float=10.0, gap: float=0.27, width_top: float=0.5, width_bot: float=1, buffer: float=3) -> gf.Component
```

[source: `components/couplers/coupler_straight_asymmetric.py:9`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Coupler with two parallel straights of different widths.

**Parameters:**

- **length** (float) - of straight. Defaults to `10.0`.
- **gap** (float) - between straights. Defaults to `0.27`.
- **width_top** (float) - of top straight. Defaults to `0.5`.
- **width_bot** (float) - of bottom straight. Defaults to `1`.
- **buffer** (float) - No description available. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## filters

### `YanglabPDK.components.filters.awg.awg`

```python
YanglabPDK.components.filters.awg.awg()
```

[source: `components/filters/awg.py:68`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an arrayed waveguide grating layout.

**Parameters:**

This component does not expose public parameters.

**Returns:**

Component containing input waveguide, Rowland regions, waveguide array, and output routing.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.filters.dbr.dbr`

```python
YanglabPDK.components.filters.dbr.dbr(w1: float=w1, w2: float=w2, l1: float=period / 2, l2: float=period / 2, n: int=10, length: float=0.1, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/filters/dbr.py:70`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Distributed Bragg Reflector.

**Parameters:**

- **w1** (float) - thin width in um. Defaults to `w1`.
- **w2** (float) - thick width in um. Defaults to `w2`.
- **l1** (float) - thin length in um. Defaults to `period / 2`.
- **l2** (float) - thick length in um. Defaults to `period / 2`.
- **n** (int) - number of periods. Defaults to `10`.
- **length** (float) - length of straight. Defaults to `0.1`.
- **width** (float) - waveguide width in um. Defaults to `1`.
- **buffer** (float) - No description available. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.filters.dbr.dbr_cell`

```python
YanglabPDK.components.filters.dbr.dbr_cell(w1: float=w1, w2: float=w2, l1: float=period / 2, l2: float=period / 2, buffer: float=3) -> gf.Component
```

[source: `components/filters/dbr.py:19`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Distributed Bragg Reflector unit cell.

**Parameters:**

- **w1** (float) - thin width in um. Defaults to `w1`.
- **w2** (float) - thick width in um. Defaults to `w2`.
- **l1** (float) - thin length in um. Defaults to `period / 2`.
- **l2** (float) - thick length in um. Defaults to `period / 2`.
- **buffer** (float) - No description available. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

## lasers

### `YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback`

```python
YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback(radius_loop: float=75, length_loop: float=250, width: float | None=1, wg_width: float=0.8, short_width: float=0.8, long_width: float=2, width_taper: float=2.424, length_taper: float=30, length_mmi: float=30.424, width_mmi: float=6.024, gap_mmi: float=0.675, radius: float=99, gap: float=0.45, racetrack_len: float=190, buffer: float=3.0)
```

[source: `components/lasers/sagnet_feedback.py:27`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a Sagnac-feedback cavity connected to an asymmetric add-drop ring.

**Parameters:**

- **radius_loop** (float) - Sagnac loop bend radius in microns. Defaults to `75`.
- **length_loop** (float) - Sagnac loop routing length in microns. Defaults to `250`.
- **width** (float | None) - Main waveguide width in microns. Defaults to `1`.
- **wg_width** (float) - Add-drop bus waveguide width in microns. Defaults to `0.8`.
- **short_width** (float) - Narrow ring width in microns. Defaults to `0.8`.
- **long_width** (float) - Wide ring width in microns. Defaults to `2`.
- **width_taper** (float) - MMI taper width in microns. Defaults to `2.424`.
- **length_taper** (float) - MMI taper length in microns. Defaults to `30`.
- **length_mmi** (float) - MMI body length in microns. Defaults to `30.424`.
- **width_mmi** (float) - MMI body width in microns. Defaults to `6.024`.
- **gap_mmi** (float) - MMI output gap in microns. Defaults to `0.675`.
- **radius** (float) - Ring radius in microns. Defaults to `99`.
- **gap** (float) - Ring coupling gap in microns. Defaults to `0.45`.
- **racetrack_len** (float) - Ring straight section length in microns. Defaults to `190`.
- **buffer** (float) - Positive-resist buffer width in microns. Defaults to `3.0`.

**Returns:**

Component with optical ports `o1` and `o2`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback_1`

```python
YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback_1(radius_loop: float=75, length_loop: float=250, width: float | None=1, wg_width: float=0.8, short_width: float=0.8, long_width: float=2, width_taper: float=2.424, length_taper: float=30, length_mmi: float=30.424, width_mmi: float=6.024, gap_mmi: float=0.675, radius: float=99, gap: float=0.45, racetrack_len: float=190, buffer: float=3.0)
```

[source: `components/lasers/sagnet_feedback.py:95`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an alternate Sagnac-feedback ring routing.

**Parameters:**

- **radius_loop** (float) - Sagnac loop bend radius in microns. Defaults to `75`.
- **length_loop** (float) - Sagnac loop routing length in microns. Defaults to `250`.
- **width** (float | None) - Main waveguide width in microns. Defaults to `1`.
- **wg_width** (float) - Add-drop bus waveguide width in microns. Defaults to `0.8`.
- **short_width** (float) - Narrow ring width in microns. Defaults to `0.8`.
- **long_width** (float) - Wide ring width in microns. Defaults to `2`.
- **width_taper** (float) - MMI taper width in microns. Defaults to `2.424`.
- **length_taper** (float) - MMI taper length in microns. Defaults to `30`.
- **length_mmi** (float) - MMI body length in microns. Defaults to `30.424`.
- **width_mmi** (float) - MMI body width in microns. Defaults to `6.024`.
- **gap_mmi** (float) - MMI output gap in microns. Defaults to `0.675`.
- **radius** (float) - Ring radius in microns. Defaults to `99`.
- **gap** (float) - Ring coupling gap in microns. Defaults to `0.45`.
- **racetrack_len** (float) - Ring straight section length in microns. Defaults to `190`.
- **buffer** (float) - Positive-resist buffer width in microns. Defaults to `3.0`.

**Returns:**

Component with optical ports `o1` and `o2`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback_with_curve`

```python
YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback_with_curve(radius_loop: float=75, length_loop: float=250, width: float | None=1, wg_width: float=0.8, short_width: float=0.8, long_width: float=2, width_taper: float=2.424, length_taper: float=30, length_mmi: float=30.424, width_mmi: float=6.024, gap_mmi: float=0.675, radius: float=99, gap: float=0.45, racetrack_len: float=200, radius_outbend=280, angle_outbend=110, total_lens=12000, offset=4000, pos_edge_coupler=3010, edge_coupler_len=250, edge_coupler_width=0.15, buffer: float=3.0)
```

[source: `components/lasers/sagnet_feedback.py:163`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a Sagnac-feedback ring with curved output routing.

**Parameters:**

- **radius_loop** (float) - Sagnac loop bend radius in microns. Defaults to `75`.
- **length_loop** (float) - Sagnac loop routing length in microns. Defaults to `250`.
- **width** (float | None) - Main waveguide width in microns. Defaults to `1`.
- **wg_width** (float) - Add-drop bus waveguide width in microns. Defaults to `0.8`.
- **short_width** (float) - Narrow ring width in microns. Defaults to `0.8`.
- **long_width** (float) - Wide ring width in microns. Defaults to `2`.
- **width_taper** (float) - MMI taper width in microns. Defaults to `2.424`.
- **length_taper** (float) - MMI taper length in microns. Defaults to `30`.
- **length_mmi** (float) - MMI body length in microns. Defaults to `30.424`.
- **width_mmi** (float) - MMI body width in microns. Defaults to `6.024`.
- **gap_mmi** (float) - MMI output gap in microns. Defaults to `0.675`.
- **radius** (float) - Ring radius in microns. Defaults to `99`.
- **gap** (float) - Ring coupling gap in microns. Defaults to `0.45`.
- **racetrack_len** (float) - Ring straight section length in microns. Defaults to `200`.
- **radius_outbend** (Any) - Output bend radius in microns. Defaults to `280`.
- **angle_outbend** (Any) - Output bend angle in degrees. Defaults to `110`.
- **total_lens** (Any) - Total routed length in microns. Defaults to `12000`.
- **offset** (Any) - Horizontal routing offset in microns. Defaults to `4000`.
- **pos_edge_coupler** (Any) - Edge coupler position in microns. Defaults to `3010`.
- **edge_coupler_len** (Any) - Edge taper length in microns. Defaults to `250`.
- **edge_coupler_width** (Any) - Edge coupler tip width in microns. Defaults to `0.15`.
- **buffer** (float) - Positive-resist buffer width in microns. Defaults to `3.0`.

**Returns:**

Component with routed optical ports.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback_with_curve_micro_heater`

```python
YanglabPDK.components.lasers.sagnet_feedback.sagnet_feedback_with_curve_micro_heater(radius_loop: float=75, length_loop: float=250, width: float | None=1, wg_width: float=0.8, short_width: float=0.8, long_width: float=2, width_taper: float=2.424, length_taper: float=30, length_mmi: float=30.424, width_mmi: float=6.024, gap_mmi: float=0.675, radius: float=99, gap: float=0.45, racetrack_len: float=200, radius_outbend=280, angle_outbend=110, total_lens=12000, offset=4000, pos_edge_coupler=3010, edge_coupler_len=250, edge_coupler_width=0.15, heater_length: float=500, heater_width: float=0.5, heater_offset: float=3000, buffer: float=3.0)
```

[source: `components/lasers/sagnet_feedback.py:250`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a curved Sagnac-feedback ring with a straight microheater.

**Parameters:**

- **radius_loop** (float) - Sagnac loop bend radius in microns. Defaults to `75`.
- **length_loop** (float) - Sagnac loop routing length in microns. Defaults to `250`.
- **width** (float | None) - Main waveguide width in microns. Defaults to `1`.
- **wg_width** (float) - Add-drop bus waveguide width in microns. Defaults to `0.8`.
- **short_width** (float) - Narrow ring width in microns. Defaults to `0.8`.
- **long_width** (float) - Wide ring width in microns. Defaults to `2`.
- **width_taper** (float) - MMI taper width in microns. Defaults to `2.424`.
- **length_taper** (float) - MMI taper length in microns. Defaults to `30`.
- **length_mmi** (float) - MMI body length in microns. Defaults to `30.424`.
- **width_mmi** (float) - MMI body width in microns. Defaults to `6.024`.
- **gap_mmi** (float) - MMI output gap in microns. Defaults to `0.675`.
- **radius** (float) - Ring radius in microns. Defaults to `99`.
- **gap** (float) - Ring coupling gap in microns. Defaults to `0.45`.
- **racetrack_len** (float) - Ring straight section length in microns. Defaults to `200`.
- **radius_outbend** (Any) - Output bend radius in microns. Defaults to `280`.
- **angle_outbend** (Any) - Output bend angle in degrees. Defaults to `110`.
- **total_lens** (Any) - Total routed length in microns. Defaults to `12000`.
- **offset** (Any) - Horizontal routing offset in microns. Defaults to `4000`.
- **pos_edge_coupler** (Any) - Edge coupler position in microns. Defaults to `3010`.
- **edge_coupler_len** (Any) - Edge taper length in microns. Defaults to `250`.
- **edge_coupler_width** (Any) - Edge coupler tip width in microns. Defaults to `0.15`.
- **heater_length** (float) - Heater length in microns. Defaults to `500`.
- **heater_width** (float) - Heater width in microns. Defaults to `0.5`.
- **heater_offset** (float) - Heater offset from the output routing in microns. Defaults to `3000`.
- **buffer** (float) - Positive-resist buffer width in microns. Defaults to `3.0`.

**Returns:**

Component with optical ports and heater metal geometry.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

## metals

### `YanglabPDK.components.metals.heater.microheater_arc_with_teeth`

```python
YanglabPDK.components.metals.heater.microheater_arc_with_teeth(R: float=30.0, w: float=0.5, theta0: float=30, theta1: float=30.0, lead_len: float=3, elef_taper_len: float=5.0, pad_size: tuple[float, float]=(11, 11), add_teeth: bool=False, tooth_len: float=3.0, tooth_w: float=1.2) -> gf.Component
```

[source: `components/metals/heater.py:99`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an arc-shaped microheater with pads and optional meander teeth.

**Parameters:**

- **R** (float) - Heater centerline radius in microns. Defaults to `30.0`.
- **w** (float) - Heater trace width in microns. Defaults to `0.5`.
- **theta0** (float) - Start angle in degrees. Defaults to `30`.
- **theta1** (float) - End angle in degrees. Defaults to `30.0`.
- **lead_len** (float) - Straight lead length in microns. Defaults to `3`.
- **elef_taper_len** (float) - Electrical taper length in microns. Defaults to `5.0`.
- **pad_size** (tuple[float, float]) - Electrical pad size `(x, y)` in microns. Defaults to `(11, 11)`.
- **add_teeth** (bool) - Whether to add meander teeth along the arc. Defaults to `False`.
- **tooth_len** (float) - Tooth length in microns. Defaults to `3.0`.
- **tooth_w** (float) - Tooth width along the tangent direction in microns. Defaults to `1.2`.

**Returns:**

Component with heater metal, pads, and electrical ports.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

## mmis

### `YanglabPDK.components.mmis.mmi1x2.mmi1x2`

```python
YanglabPDK.components.mmis.mmi1x2.mmi1x2(width: float | None=1, width_taper: float=1.0, length_taper: float=10.0, length_mmi: float=5.5, width_mmi: float=2.5, gap_mmi: float=0.25, buffer: float=3.0) -> gf.Component
```

[source: `components/mmis/mmi1x2.py:10`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

1x2 MultiMode Interferometer (MMI).

**Parameters:**

- **width** (float | None) - input and output straight width. Defaults to cross_section width. Defaults to `1`.
- **width_taper** (float) - interface between input straights and mmi region. Defaults to `1.0`.
- **length_taper** (float) - into the mmi region. Defaults to `10.0`.
- **length_mmi** (float) - in x direction. Defaults to `5.5`.
- **width_mmi** (float) - in y direction. Defaults to `2.5`.
- **gap_mmi** (float) - gap between tapered wg. Defaults to `0.25`.
- **buffer** (float) - Buffer width for positive tone resist Defaults to `3.0`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.mmis.mmi2x2.mmi2x2`

```python
YanglabPDK.components.mmis.mmi2x2.mmi2x2(width: float=1, width_taper: float=2, length_taper: float=20, length_mmi: float=125, width_mmi: float=15, gap_mmi: float=4, buffer: float=3) -> gf.Component
```

[source: `components/mmis/mmi2x2.py:21`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Mmi 2x2.

**Parameters:**

- **width** (float) - input and output straight width. Defaults to `1`.
- **width_taper** (float) - interface between input straights and mmi region. Defaults to `2`.
- **length_taper** (float) - into the mmi region. Defaults to `20`.
- **length_mmi** (float) - in x direction. Defaults to `125`.
- **width_mmi** (float) - in y direction. Defaults to `15`.
- **gap_mmi** (float) - (width_taper + gap between tapered wg)/2. Defaults to `4`.
- **buffer** (float) - buffer around the component. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## mzis

### `YanglabPDK.components.mzis.mzi_mmi.mzi_mmi`

```python
YanglabPDK.components.mzis.mzi_mmi.mzi_mmi(width: float | None=1, width_taper: float=1.0, length_taper: float=10.0, length_mmi: float=5.5, width_mmi: float=2.5, gap_mmi: float=0.25, bend_angle: float=30, straight_length: float=10.0, edge_length: float=500, buffer: float=3.0) -> gf.Component
```

[source: `components/mzis/mzi_mmi.py:12`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return an MZI built from two 1x2 MMI couplers.

**Parameters:**

- **width** (float | None) - Waveguide width in microns. Defaults to `1`.
- **width_taper** (float) - MMI taper width in microns. Defaults to `1.0`.
- **length_taper** (float) - MMI taper length in microns. Defaults to `10.0`.
- **length_mmi** (float) - MMI body length in microns. Defaults to `5.5`.
- **width_mmi** (float) - MMI body width in microns. Defaults to `2.5`.
- **gap_mmi** (float) - Gap between MMI output waveguides in microns. Defaults to `0.25`.
- **bend_angle** (float) - S-bend angle in degrees. Defaults to `30`.
- **straight_length** (float) - Length of the two interferometer arms in microns. Defaults to `10.0`.
- **edge_length** (float) - Length of the input and output access waveguides in microns. Defaults to `500`.
- **buffer** (float) - Positive-resist buffer width in microns. Defaults to `3.0`.

**Returns:**

Component with optical ports `o1` and `o2`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## reflectors

### `YanglabPDK.components.reflectors.sagnac_loop.sagnac_loop`

```python
YanglabPDK.components.reflectors.sagnac_loop.sagnac_loop(radius_loop: float=75, length_loop: float=250, width: float | None=1, width_taper: float=2.424, length_taper: float=30, length_mmi: float=30.424, width_mmi: float=6.024, gap_mmi: float=0.675, buffer: float=3.0)
```

[source: `components/reflectors/sagnac_loop.py:24`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a Sagnac loop reflector based on a 1x2 MMI.

**Parameters:**

- **radius_loop** (float) - Radius of the loop bend in microns. Defaults to `75`.
- **length_loop** (float) - S-bend routing length in microns. Defaults to `250`.
- **width** (float | None) - Waveguide width in microns. Defaults to `1`.
- **width_taper** (float) - MMI taper width in microns. Defaults to `2.424`.
- **length_taper** (float) - MMI taper length in microns. Defaults to `30`.
- **length_mmi** (float) - MMI body length in microns. Defaults to `30.424`.
- **width_mmi** (float) - MMI body width in microns. Defaults to `6.024`.
- **gap_mmi** (float) - MMI output gap in microns. Defaults to `0.675`.
- **buffer** (float) - Positive-resist buffer width in microns. Defaults to `3.0`.

**Returns:**

Component with one optical input port `o1`.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

## shapes

### `YanglabPDK.components.shapes.circles.angled_arc_with_port`

```python
YanglabPDK.components.shapes.circles.angled_arc_with_port(radius: float=50.0, angle: float=90.0, angle_resolution: float=0.1, buffer: float=3.0, port_width_in: float=1.0, port_width_out: float=0.8, port_gap_out: float=0.2, port_number_out: int=21) -> gf.Component
```

[source: `components/shapes/circles.py:228`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Generate a semicircle geometry (0° to 180°).

**Parameters:**

- **radius** (float) - radius of the semicircle. Defaults to `50.0`.
- **angle** (float) - No description available. Defaults to `90.0`.
- **angle_resolution** (float) - number of degrees per point. Defaults to `0.1`.
- **buffer** (float) - No description available. Defaults to `3.0`.
- **port_width_in** (float) - No description available. Defaults to `1.0`.
- **port_width_out** (float) - No description available. Defaults to `0.8`.
- **port_gap_out** (float) - No description available. Defaults to `0.2`.
- **port_number_out** (int) - No description available. Defaults to `21`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.shapes.circles.quarter_circle`

```python
YanglabPDK.components.shapes.circles.quarter_circle(radius: float=50.0, angle_resolution: float=0.1, layer: tuple=LAYER.NR) -> gf.Component
```

[source: `components/shapes/circles.py:53`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Generate a quarter circle geometry (0° to 90°).

**Parameters:**

- **radius** (float) - radius of the quarter circle. Defaults to `50.0`.
- **angle_resolution** (float) - number of degrees per point. Defaults to `0.1`.
- **layer** (tuple) - layer. Defaults to `LAYER.NR`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.shapes.circles.rowland_circle_with_port`

```python
YanglabPDK.components.shapes.circles.rowland_circle_with_port(radius: float=50.0, angle: float=75.0, angle_resolution: float=0.1, buffer: float=3.0, port_width_in: float=0.8, port_width_out: float=0.8, port_gap_out: float=0.2, port_number_out: int=21, port_number_in: int=8, port_gap_in: float=0.336) -> gf.Component
```

[source: `components/shapes/circles.py:311`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Generate a semicircle geometry (0° to 180°).

**Parameters:**

- **radius** (float) - radius of the semicircle. Defaults to `50.0`.
- **angle** (float) - No description available. Defaults to `75.0`.
- **angle_resolution** (float) - number of degrees per point. Defaults to `0.1`.
- **buffer** (float) - No description available. Defaults to `3.0`.
- **port_width_in** (float) - No description available. Defaults to `0.8`.
- **port_width_out** (float) - No description available. Defaults to `0.8`.
- **port_gap_out** (float) - No description available. Defaults to `0.2`.
- **port_number_out** (int) - No description available. Defaults to `21`.
- **port_number_in** (int) - No description available. Defaults to `8`.
- **port_gap_in** (float) - No description available. Defaults to `0.336`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.shapes.circles.semi_circle`

```python
YanglabPDK.components.shapes.circles.semi_circle(radius: float=50.0, angle_resolution: float=0.1, buffer: float=3.0) -> gf.Component
```

[source: `components/shapes/circles.py:85`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Generate a semicircle geometry (0° to 180°).

**Parameters:**

- **radius** (float) - radius of the semicircle. Defaults to `50.0`.
- **angle_resolution** (float) - number of degrees per point. Defaults to `0.1`.
- **buffer** (float) - No description available. Defaults to `3.0`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.shapes.circles.semi_circle_with_port`

```python
YanglabPDK.components.shapes.circles.semi_circle_with_port(radius: float=50.0, angle_resolution: float=0.1, buffer: float=3.0, port_width_in: float=1.0, port_width_out: float=0.8, port_gap_out: float=0.2, port_number_out: int=21) -> gf.Component
```

[source: `components/shapes/circles.py:130`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Generate a semicircle geometry (0° to 180°).

**Parameters:**

- **radius** (float) - radius of the semicircle. Defaults to `50.0`.
- **angle_resolution** (float) - number of degrees per point. Defaults to `0.1`.
- **buffer** (float) - No description available. Defaults to `3.0`.
- **port_width_in** (float) - No description available. Defaults to `1.0`.
- **port_width_out** (float) - No description available. Defaults to `0.8`.
- **port_gap_out** (float) - No description available. Defaults to `0.2`.
- **port_number_out** (int) - No description available. Defaults to `21`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

### `YanglabPDK.components.shapes.circles.single_semi_circle`

```python
YanglabPDK.components.shapes.circles.single_semi_circle(radius: float=50.0, angle_resolution: float=0.1, layer: tuple=LAYER.NR) -> gf.Component
```

[source: `components/shapes/circles.py:21`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Generate a semicircle geometry (0° to 180°).

**Parameters:**

- **radius** (float) - radius of the semicircle. Defaults to `50.0`.
- **angle_resolution** (float) - number of degrees per point. Defaults to `0.1`.
- **layer** (tuple) - layer. Defaults to `LAYER.NR`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell`

## spirals

### `YanglabPDK.components.spirals.spiral_double.spiral_double`

```python
YanglabPDK.components.spirals.spiral_double.spiral_double(min_bend_radius: float=10.0, separation: float=2.0, number_of_loops: float=3, npoints: int=1000, width: float=1, buffer: float=3)
```

[source: `components/spirals/spiral_double.py:7`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns a spiral double (spiral in, and then out).

**Parameters:**

- **min_bend_radius** (float) - inner radius of the spiral. Defaults to `10.0`.
- **separation** (float) - separation between the loops. Defaults to `2.0`.
- **number_of_loops** (float) - number of loops per spiral. Defaults to `3`.
- **npoints** (int) - points for the spiral. Defaults to `1000`.
- **width** (float) - waveguide width in um. Defaults to `1`.
- **buffer** (float) - buffer. Defaults to `3`.

**Returns:**

Component with the double spiral layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## tapers

### `YanglabPDK.components.tapers.taper.taper`

```python
YanglabPDK.components.tapers.taper.taper(length: float=10.0, width1: float=1, width2: float=1, buffer: float=3, is_buffer_aligned: bool=False) -> gf.Component
```

[source: `components/tapers/taper.py:22`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Linear taper, which tapers only the main cross section section.

**Parameters:**

- **length** (float) - taper length. Defaults to `10.0`.
- **width1** (float) - width of the west/left port. Defaults to `1`.
- **width2** (float) - width of the east/right port. Defaults to width1. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.
- **is_buffer_aligned** (bool) - No description available. Defaults to `False`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.tapers.taper.taper_buffer`

```python
YanglabPDK.components.tapers.taper.taper_buffer(length: float=10.0, width1: float=1, width2: float=1, buffer1: float=3, buffer2: float=3, is_buffer_aligned: bool=False) -> gf.Component
```

[source: `components/tapers/taper.py:52`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Linear taper, which tapers only the main cross section section.

**Parameters:**

- **length** (float) - taper length. Defaults to `10.0`.
- **width1** (float) - width of the west/left port. Defaults to `1`.
- **width2** (float) - width of the east/right port. Defaults to width1. Defaults to `1`.
- **buffer1** (float) - No description available. Defaults to `3`.
- **buffer2** (float) - No description available. Defaults to `3`.
- **is_buffer_aligned** (bool) - No description available. Defaults to `False`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## utils

### `YanglabPDK.components.utils.field.dicing_lane`

```python
YanglabPDK.components.utils.field.dicing_lane(size=(6500, 14000), orientation='X') -> gf.Component
```

[source: `components/utils/field.py:102`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns a dicing lane component with four rectangles on the edges of the die.

**Parameters:**

- **size** (Any) - Size of the die (width, height) in microns. The function places four rectangles (dicing marks) on the left, right, top, and bottom edges of the die area, using the CUT layer defined in LAYER.CUT. These marks are typically used to guide wafer dicing after fabrication. Defaults to `(6500, 14000)`.
- **orientation** (Any) - No description available. Defaults to `'X'`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.utils.field.die_marker_field`

```python
YanglabPDK.components.utils.field.die_marker_field(field_size=1000, die_size=(10000, 10000), mark_pair_num=3, calipers=None, expose_marker_list=None)
```

[source: `components/utils/field.py:11`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a die field grid with alignment markers and anchors.

**Parameters:**

- **field_size** (Any) - E-beam/write field size in microns. Defaults to `1000`.
- **die_size** (Any) - Die size `(width, height)` in microns. Defaults to `(10000, 10000)`.
- **mark_pair_num** (Any) - Number of marker pairs to place around the die. Defaults to `3`.
- **calipers** (Any) - Optional caliper component to place near the die edge. Defaults to `None`.
- **expose_marker_list** (Any) - Marker indices that should receive expose windows. Defaults to `None`.

**Returns:**

Component containing field boxes, markers, anchors, and optional calipers.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.utils.mark.cross`

```python
YanglabPDK.components.utils.mark.cross(outter_length: float=200, outter_width: float=5, inner_width: float=1, layer: Layer=LAYER.MK, text: str='1') -> gf.Component
```

[source: `components/utils/mark.py:8`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Return a hollow cross alignment marker with a text label.

**Parameters:**

- **outter_length** (float) - Outer cross length in microns. Defaults to `200`.
- **outter_width** (float) - Outer cross width in microns. Defaults to `5`.
- **inner_width** (float) - Subtracted inner cross width in microns. Defaults to `1`.
- **layer** (Layer) - Marker layer. Defaults to `LAYER.MK`.
- **text** (str) - Text label placed next to the marker. Defaults to `'1'`.

**Returns:**

Component containing the marker geometry and label.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

## waveguides

### `YanglabPDK.components.waveguides.straight.straight`

```python
YanglabPDK.components.waveguides.straight.straight(length: float=10, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/waveguides/straight.py:7`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns a Straight waveguide.

**Parameters:**

- **length** (float) - straight length (um). Defaults to `10`.
- **width** (float) - width of the waveguide. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist (um) Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`

### `YanglabPDK.components.waveguides.straight_heater_metal.straight_heater_metal_undercut`

```python
YanglabPDK.components.waveguides.straight_heater_metal.straight_heater_metal_undercut(length: float=320.0, length_undercut_spacing: float=6, length_undercut: float=30.0, length_straight_input: float=15, with_undercut: bool=True, heater_taper_length: float=5.0, heater_width: float=2, undercut_width: float=3, undercut_gap: float=3, width: float=1, buffer: float=3) -> gf.Component
```

[source: `components/waveguides/straight_heater_metal.py:9`]

**Preview:** unavailable - gdsfactory import failed: PermissionError: [WinError 5] Access is denied

Returns a thermal phase shifter. dimensions from https://doi.org/10.1364/OE.27.010456

**Parameters:**

- **length** (float) - of the waveguide. Defaults to `320.0`.
- **length_undercut_spacing** (float) - from undercut regions. Defaults to `6`.
- **length_undercut** (float) - length of each undercut section. Defaults to `30.0`.
- **length_straight_input** (float) - from input port to where trenches start. Defaults to `15`.
- **with_undercut** (bool) - isolation trenches for higher efficiency. Defaults to `True`.
- **heater_taper_length** (float) - minimizes current concentrations from heater to via_stack. Defaults to `5.0`.
- **heater_width** (float) - width of the heater. Defaults to `2`.
- **undercut_width** (float) - width of the undercut. Defaults to `3`.
- **undercut_gap** (float) - gap between the undercut and the waveguide. Defaults to `3`.
- **width** (float) - width of the waveguide. Defaults to `1`.
- **buffer** (float) - buffer width for positive tone resist. Defaults to `3`.

**Returns:**

Component with the generated layout.

**Return type:**

`gf.Component`

**Discovered by:** `gf.cell + __all__`
