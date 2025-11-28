## flake8-absolute-import: flake8 plugin to require absolute imports

#### Current Development Version

[![GitHub Workflow Status][workflow badge]][workflow link target]

#### Most Recent Stable Release

[![PyPI Version][pypi badge]][pypi link target]
![Python Versions][python versions badge]

#### Info

[![MIT License][license badge]][license link target]
[![black formatted][black badge]][black link target]
[![PePY stats][pepy badge]][pepy link target]

----

### Don't like relative imports?

#### Lint 'em out!

`flake8-absolute-import` uses a direct check of the AST for each
`from x import y` statement to flag relative imports.
Specifically, it checks for a nonzero _level_ attribute on each
[`ImportFrom`] node.

Relative imports raise the `ABS101` error code:

```py
    from foo import bar   # OK
    from .foo import bar  # ABS101
```

----

Available on [PyPI][pypi link target] (`pip install flake8-absolute-import`).
`flake8` should automatically detect and load the plugin. `flake8`>=5.0 is
required.

Source on [GitHub][gh repo]. Bug reports and feature requests are welcomed at
the [Issues][gh issues] page there.

Copyright (c) Brian Skinn 2019-2023

The `flake8-absolute-import` documentation (currently docstrings and README) is
licensed under a [Creative Commons Attribution 4.0 International License][cc-by]
(CC-BY). The `flake8-absolute-import` codebase is released under the [MIT
License]. See [`LICENSE.txt`] for full license terms.

[`ImportFrom`]: https://docs.python.org/3/library/ast.html#ast.ImportFrom
[`LICENSE.txt`]: https://github.com/bskinn/flake8-absolute-import/blob/main/LICENSE.txt

[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black link target]: https://github.com/psf/black

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[gh issues]: https://github.com/bskinn/flake8-absolute-import/issues
[gh repo]: https://github.com/bskinn/flake8-absolute-import

[license badge]: https://img.shields.io/github/license/mashape/apistatus.svg
[license link target]: https://github.com/bskinn/flake8-absolute-import/blob/stable/LICENSE.txt

[MIT License]: https://opensource.org/licenses/MIT

[pepy badge]: https://pepy.tech/badge/flake8-absolute-import/month
[pepy link target]: https://pepy.tech/project/flake8-absolute-import

[pypi badge]: https://img.shields.io/pypi/v/flake8-absolute-import.svg?logo=pypi
[pypi link target]: https://pypi.org/project/flake8-absolute-import

[python versions badge]: https://img.shields.io/pypi/pyversions/flake8-absolute-import.svg?logo=python

[workflow badge]: https://img.shields.io/github/actions/workflow/status/bskinn/flake8-absolute-import/all_core_tests.yml?branch=main&logo=github
[workflow link target]: https://github.com/bskinn/flake8-absolute-import/actions
