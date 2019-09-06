r"""*Core tests file for* ``flake8-absolute-import``.

flake8 plugin to require absolute imports

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    6 Sep 2019

**Copyright**
    \(c) Brian Skinn 2019

**Source Repository**
    http://www.github.com/bskinn/flake8-absolute-import

**Documentation**
    http://flake8-absolute-import.readthedocs.io

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import ast

import pytest

from flake8_absolute_import import Plugin


@pytest.mark.parametrize("line", ["import sys", "import flake8_absolute_import"])
def test_module_import(line):
    """Confirm no error found on module import."""
    tree = ast.parse(line)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize(
    "line",
    [
        "from sys import argv",
        "from flake8_absolute_import import Plugin",
        "from flake8_absolute_import.core import Plugin",
    ],
)
def test_absolute_import(line):
    """Confirm no error found on absolute member import."""
    tree = ast.parse(line)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize(
    "line", ["from .core import Plugin", "from .version import __version__"]
)
def test_relative_import(line):
    """Confirm error *IS* found on relative member import."""
    tree = ast.parse(line)
    assert len(list(Plugin(tree).run())) == 1


def test_multiple_relative_imports():
    """Confirm multiple errors are found on multiple relative member imports."""
    line = "from .core import Plugin\nfrom .version import __version__"

    tree = ast.parse(line)
    assert len(list(Plugin(tree).run())) == (line.count("\n") + 1)


def test_multilevel_relative_import():
    """Confirm error is found with a multi-dot relative import."""
    line = "from ..foo import bar"

    tree = ast.parse(line)
    assert len(list(Plugin(tree).run())) == 1
