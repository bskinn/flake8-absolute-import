r"""*Core tests file for* ``flake8-absolute-import``.

flake8 plugin to require absolute imports

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    6 Sep 2019

**Copyright**
    \(c) Brian Skinn 2019-2021

**Source Repository**
    http://github.com/bskinn/flake8-absolute-import

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import ast
from textwrap import dedent

import pytest

from flake8_absolute_import import Plugin


def is_relative(import_source):
    """Indicate if a given 'from {source}' import location is a relative import."""
    return import_source.startswith(".")


def format_id(id_):
    """Provide parametrization id formatting for the given id."""
    return f"{id_} (expect {'' if is_relative(id_) else 'no '}error)"


@pytest.mark.parametrize("code", ["import sys", "import flake8_absolute_import"])
def test_module_import(code):
    """Confirm no error found on module import."""
    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize(
    "code",
    [
        "from sys import argv",
        "from flake8_absolute_import import Plugin",
        "from flake8_absolute_import.core import Plugin",
    ],
)
def test_absolute_import(code):
    """Confirm no error found on absolute member import."""
    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize(
    "code", ["from .core import Plugin", "from .version import __version__"]
)
@pytest.mark.xfail
def test_relative_import(code):
    """Confirm error *IS* found on relative member import."""
    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.xfail
def test_multiple_relative_imports():
    """Confirm multiple errors are found on multiple relative member imports."""
    code = "from .core import Plugin\nfrom .version import __version__"

    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


def test_correct_relative_import_linenos():
    """Confirm the multiple errors are reported on the correct lines."""
    code = dedent(
        """\
    from .core import Plugin
    from f8_absolute_import.core import Visitor
    from .version import __version__
    """
    )

    tree = ast.parse(code)
    assert {t[0] for t in Plugin(tree).run()} == {1, 3}


@pytest.mark.xfail
def test_multilevel_relative_import():
    """Confirm error is found with a multi-dot relative import."""
    code = "from ..foo import bar"

    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize("impfrom", ["mod", ".mod"], ids=format_id)
def test_func_imports(impfrom):
    """Confirm plugin works for imports in functions."""
    code = dedent(
        f"""
    def func():
        from {impfrom} import foo
    """
    )

    tree = ast.parse(code)
    assert (len(list(Plugin(tree).run())) == 1) == (impfrom.startswith("."))


@pytest.mark.parametrize("impfrom", ["mod", ".mod"], ids=format_id)
def test_class_imports(impfrom):
    """Confirm plugin works for imports in class bodies."""
    code = dedent(
        f"""
    class Bar:
        from {impfrom} import foo
    """
    )

    tree = ast.parse(code)
    assert (len(list(Plugin(tree).run())) == 1) == (impfrom.startswith("."))


@pytest.mark.parametrize("impfrom", ["mod", ".mod"], ids=format_id)
def test_method_imports(impfrom):
    """Confirm plugin works for imports in class methods."""
    code = dedent(
        f"""
    class Bar:
        def baz(self):
            from {impfrom} import foo
    """
    )

    tree = ast.parse(code)
    assert (len(list(Plugin(tree).run())) == 1) == (impfrom.startswith("."))
