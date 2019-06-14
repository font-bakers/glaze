# Quickstart

## Installation

The latest release of `glaze` can be installed from PyPI:

```bash
pip install glaze
```

The bleeding edge development branch of `glaze` can be cloned from GitHub:

```bash
git clone https://github.com/font-bakers/glaze/
cd glaze/
pip install -r requirements.txt
pip install -e .
```

## Usage

To use `glaze` as a library:

```python
import matplotlib.pyplot as plt
from glaze import render

render(contours)  # Visualize a vector glyph
```

For more information, see the documentation for the `render` function.

To run `glaze` on the command line:

```bash
glaze --input INPUT [--output OUTPUT_PATH --format FORMAT]
```

`--input` must be one of:

- a `.json` file (such as those produced by `knead`)
- a `.npy` file,
- a directory containing such files.

`--output` is the path to the desired location of the output images. If
`--output` is not specified, it defaults to the present working directory.

`--format` is the format in which the image should be saved. Must be one of
`jpg`, `png` or `pdf`.
