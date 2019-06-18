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

To use `glaze` as a library:

```python
import matplotlib.pyplot as plt
from glaze import render

fig = render(contours)  # Render one glyph
```

For more information, see [the docstring for the `render`
function](https://github.com/font-bakers/glaze/blob/master/glaze/render.py).
(Note that while `glaze` does contain other modules and functions, the only
thing of any practical value is the `render` function).

To run `glaze` on the command line:

```bash
glaze --input INPUT [--output OUTPUT]
```

`--input` is a `.json` file (such as those produced by `knead`), or a directory
containing such `.json` files.

`--output` is the path to the desired location of the output images. If
`--output` is not specified, it defaults to the present working directory.

In the event of a fatal error during rendering, `glaze` will simply catch the
exception and write the error message (along with a stack trace) to a
`glaze.log` file.
