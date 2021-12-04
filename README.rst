flake8-absolute-import
======================

*flake8 plugin to require absolute imports*

**Current Development Version:**

.. image:: https://img.shields.io/github/workflow/status/bskinn/flake8-absolute-import/ci-tests?logo=github
    :alt: GitHub Workflow Status
    :target: https://github.com/bskinn/flake8-absolute-import/actions

.. image:: https://codecov.io/gh/bskinn/flake8-absolute-import/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/bskinn/flake8-absolute-import

**Most Recent Stable Release:**

.. image:: https://img.shields.io/pypi/v/flake8-absolute-import.svg?logo=pypi
    :target: https://pypi.org/project/flake8-absolute-import

.. image:: https://img.shields.io/pypi/pyversions/flake8-absolute-import.svg?logo=python

**Info:**

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://github.com/bskinn/flake8-absolute-import/blob/stable/LICENSE.txt

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

----

*Don't like relative imports?*

Lint 'em out!

``flake8-absolute-import`` uses a simple check of the AST for each
``from x import y`` statement to flag relative imports.
Specifically, it checks for a nonzero *level* attribute on each
|ImportFrom|_ node.

Relative imports raise the ``ABS101`` error code:

.. code:: python

    from foo import bar   # OK
    from .foo import bar  # ABS101

----

Available on `PyPI <https://pypi.python.org/pypi/flake8-absolute-import>`__
(``pip install flake8-absolute-import``).  ``flake8`` should automatically
detect and load the plugin. ``flake8``>=3.0 is required.

Source on `GitHub <https://github.com/bskinn/flake8-absolute-import>`__.  Bug reports
and feature requests are welcomed at the
`Issues <https://github.com/bskinn/flake8-absolute-import/issues>`__ page there.

Copyright (c) Brian Skinn 2019-2020

License: The MIT License. See `LICENSE.txt <https://github.com/bskinn/flake8-absolute-import/blob/main/LICENSE.txt>`__
for full license terms.

.. _ImportFrom: https://greentreesnakes.readthedocs.io/en/latest/nodes.html#ImportFrom
.. |ImportFrom| replace:: ``ImportFrom``
