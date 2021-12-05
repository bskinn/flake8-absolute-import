r"""*Main implementation file for* ``flake8-absolute-import``.

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

from flake8_absolute_import.version import __version__


ABS101 = "ABS101 Relative import found"


class Visitor(ast.NodeVisitor):
    """NodeVisitor to report relative imports."""

    def __init__(self):
        """Create a Visitor with empty errors list."""
        self.errors = []

    def visit_ImportFrom(self, node):  # noqa: N802
        """Implement check for relative import."""
        if node.level > 0:
            self.errors.append((node.lineno, node.col_offset, ABS101))

        self.generic_visit(node)


class Plugin:
    """Core plugin class for flake8-absolute-import."""

    name = "flake8-absolute-import"
    version = __version__

    def __init__(self, tree):
        """Create plugin instance from the provided AST."""
        self._tree = tree

    def run(self):
        """Traverse the AST and collect the errors."""
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
