# Contributing Guide

[![GitHub Issues](https://img.shields.io/github/issues/font-bakers/glaze.svg)](https://github.com/font-bakers/glaze/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/font-bakers/glaze.svg)](https://github.com/font-bakers/glaze/pulls)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/font-bakers/glaze/blob/master/CODE_OF_CONDUCT.md)

Happy baking!

## Set up development environment

```bash
git clone https://github.com/font-bakers/glaze.git
cd glaze/
make develop
source venv/bin/activate
# Do your work...
deactivate
```

## Before committing

```bash
make check
```

This will both lint the `glaze/` directory (with `black` and `pylint`), and run
test scripts. You may lint and test separately with `make lint` and `make test`,
respectively.

Make sure that all checks pass before committing: you should get several blue
success messages as each check passes.

Note that `glaze` uses a [pre-commit git
hook](https://github.com/font-bakers/glaze/blob/master/.githooks/pre-commit) to
format staged Python files in-place using `black`.

## Packaging and releasing `glaze`

First, ensure that the version number has been bumped appropriately:`glaze`
adopts the [Semantic Versioning
2.0.0](https://semver.org/#semantic-versioning-200) specification. This can be
done either by running

```bash
bumpversion --current-version CURRENT_VERSION PART glaze/__init__.py
```

or by directly editing the `__version__` variable in `glaze/__init__.py` (the
latter method is simpler and recommended for such a simple project as `glaze`).
For more information, see the [bumpversion
documentation](https://github.com/peritus/bumpversion#usage).

Then, run `make package`. It will package `glaze` and validate the resulting
[source archive](https://packaging.python.org/glossary/#term-source-archive) and
[built
distribution](https://packaging.python.org/glossary/#term-built-distribution).

Finally, upload the source archive and build distribution to PyPI. You will be
asked for a username and password for PyPI.

```bash
twine upload dist/*
```

For more information, refer to the [Python packaging
documentation](https://packaging.python.org/tutorials/packaging-projects/).

## Miscellaneous development details

* `glaze` adopts the [Semantic Versioning
  2.0.0](https://semver.org/#semantic-versioning-200) specification.

* `glaze` targets Python 3.5+ (specifically, 3.5.2+) compatibility.

* `glaze` uses `black` and `pylint` to format and lint code, respectively.
  * However, `black` requires Python 3.6+ to run. Thus, we test in Python 3.5
    but lint in Python 3.6. See our [Travis
    configuration](https://github.com/font-bakers/glaze/blob/master/.travis.yml)
    for more details.

* `glaze` is [unit
  tested](https://github.com/font-bakers/glaze/blob/master/glaze/tests/test_render.py)
  through `pytest`, and integration tested through the [`test_cli.sh`
  script](https://github.com/font-bakers/glaze/blob/master/glaze/tests/test_cli.sh).

* The `glaze` documentation is generated using `mkdocs`. See the
  [`mkdocs.yml`](https://github.com/font-bakers/glaze/blob/master/mkdocs.yml)
  configuration for more details.
