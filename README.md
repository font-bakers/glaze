<p align="center">
<img src="https://raw.githubusercontent.com/font-bakers/glaze/master/docs/img/logo.png" alt="Glaze logo" title="Glaze logo" align="center"></img>
</p>

[![Build Status](https://travis-ci.com/font-bakers/glaze.svg?branch=master)](https://travis-ci.com/font-bakers/glaze)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-352/)

---

`glaze` is a Python library and command line tool for rendering
algorithmically-generated fonts and typefaces.

## Table of Contents

* [Demo](#Demo)
* [Installation](#Installation)
* [Usage](#Usage)
* [Documentation](#Documentation)
* [Contributing](#Contributing)
* [License](#License)

## Demo

```python
>>> import matplotlib.pyplot as plt
>>> from glaze import read_json, render
>>>
>>> font = read_json("data/Georgia.json")
>>> font_name, glyph_name, glyph = font[0]
>>> render(glyph)
>>> plt.show()
```

<img src="https://raw.githubusercontent.com/font-bakers/glaze/master/docs/img/Georgia.g_lower.png" alt="Rendered glyph (lowercase g)" title="Rendered glyph" align="center"></img>

## Installation

The latest release of `glaze` can be installed from PyPI:

```bash
pip install glaze
```

## Usage

To use `glaze` as a library:

```python
import matplotlib.pyplot as plt
from glaze import render

fig = render(contours)  # Render one glyph
```

To run `glaze` on the command line:

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

1. However, should you want to render only a few files, you can use the
   `--files` flag, which must be one of:
    * a path to a `.json` file (again, such as those produced by `knead`),
    * a comma-separated list of such paths, or
    * a regex matching the path(s) to one or more `.json` files.

  Renders will be saved in the present working directory (unless [the `--output`
  flag](https://font-bakers.github.io/glaze/quickstart/#optional-flags) is
  passed).

Refer to our [quickstart](https://font-bakers.github.io/glaze/quickstart/) for
more information on how to use `glaze`.

## Documentation

Please refer to our [full documentation](https://font-bakers.github.io/glaze/).

## Contributing

Contributions are always welcome! Please see our [issue
tracker](https://github.com/font-bakers/glaze/issues) for outstanding issues,
[code of
conduct](https://github.com/font-bakers/glaze/blob/master/CODE_OF_CONDUCT.md)
for community guidelines, and our [contributing
guide](https://font-bakers.github.io/glaze/contributing/) for details on how to
make a contribution.

## License

`glaze` is licensed under the [MIT
license](https://github.com/font-bakers/glaze/blob/master/LICENSE).
