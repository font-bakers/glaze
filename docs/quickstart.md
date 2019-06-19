# Quickstart

## Installation

The latest release of `glaze` can be installed from PyPI:

```bash
pip install glaze
```

The bleeding edge development branch of `glaze` can be installed from GitHub:

```bash
pip install git+https://github.com/font-bakers/glaze.git
```

## Usage

### In Python

```python
>>> import matplotlib.pyplot as plt
>>> from glaze import read_json, render
>>>
>>> font = read_json("data/Georgia.json")  # Returns a list of 3-tuples
>>> font_name, glyph_name, glyph = font[0]
>>> render(glyph)  # Renders one glyph
>>> plt.show()
```

For more information, see the docstrings for [the `read_json`
function](https://github.com/font-bakers/glaze/blob/master/glaze/utils.py) and
[the `render`
function](https://github.com/font-bakers/glaze/blob/master/glaze/render.py).
(Note that while `glaze` does contain other modules and functions, the only
things of any practical value are the `render` and `read_json` functions).

### On the command line

```bash
glaze --input PATH/TO/INPUT
```

`--input` is a `.json` file (such as those produced by `knead`), or a directory
containing such `.json` files.

For more information on optional flags, refer to [the section
below](#optional-flags).

In the event of a fatal error during rendering, `glaze` will simply catch the
exception and write the error message (along with a stack trace) to a
`glaze.log` file.

## Optional Flags

1. `--output`: Path to the desired location of the output renders. Defaults to
   the present working directory.

2. `--num_points`: Number of points to sample per Bezier curve. Defaults to 32.

3. `--lim`: x and y limits of the rendered glyph. This flags is passed as
   comma-separated values, e.g. `glaze --input MyFont.json --lim -0.2,1.3`.
   Defaults to [-0.3, 1.2].

4. `--grid`: If True, overlays the axes and gridlines on the rendered glyph.
   Defaults to False.
