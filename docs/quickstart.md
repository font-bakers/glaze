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
# Recommended usage
glaze --directory PATH/TO/DATA/

# Alternative usage
glaze --files FILES
```

1. The `--directory` must have the following structure:

   ```bash
   data
   ├── json
   │   ├── Georgia.json
   │   └── ...
   └── ...
   ```

   where the `.json` files are those produced by `knead`. Renders will be saved
   in a directory `data/renders-TTTT-DD-MM/`, where `TTTT` is military time.

   _In other words, `--directory` is not the directory containing the `.json`
   files. It is a directory that contains a subdirectory (called `json`)
   containing the `.json` files._

   Using this flag is the recommended way to use `glaze`, as it preserves the
   same data model that `knead` does. That is, each directory contains only
   subdirectories with the same data in various different data formats. In this
   way, each directory can be semantically associated with a single data set,
   irrespective of its data format.

1. However, should you want to render only a few files, you can use the
   `--files` flag, which must be one of:
  * a path to a `.json` file (again, such as those produced by `knead`),
  * a comma-separated list of such paths, or
  * a regex matching the path(s) to one or more `.json` files.

  Renders will be saved in the present working directory (unless [the `--output`
  flag](https://font-bakers.github.io/glaze/quickstart/#optional-flags) is
  passed).

For more information on optional flags, refer to [the section
below](#optional-flags).

In the event of a fatal error during rendering, `glaze` will simply catch the
exception and write the error message (along with a stack trace) to a
`glaze.log` file.

## Optional Flags

1. `--output`: Path to the desired location of the output renders. Defaults to
   the present working directory. Only used if `--files` is passed.

1. `--num_points`: Number of points to sample per Bezier curve. Defaults to 32.

1. `--lim`: x and y limits of the rendered glyph. This flags is passed as
   comma-separated values, e.g. `glaze --input MyFont.json --lim -0.2,1.3`.
   Defaults to [-0.3, 1.2].

1. `--grid`: If True, overlays the axes and gridlines on the rendered glyph.
   Defaults to False.
