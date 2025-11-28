r"""*Main implementation file for* ``flake8-absolute-import``.

flake8 plugin to require absolute imports

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    6 Sep 2019

**Copyright**
    \(c) Brian Skinn 2019-2025

**Source Repository**
    http://github.com/bskinn/flake8-absolute-import

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import ast
from typing import Generator

from flake8_absolute_import.version import __version__

ABS101: str = "ABS101 Relative import found"


class Visitor(ast.NodeVisitor):
    """NodeVisitor to report relative imports."""

    def __init__(self) -> None:
        """Create a Visitor with empty errors list."""
        self.errors: list[tuple[int, int, str]] = []

    def visit_ImportFrom(self, node) -> None:  # noqa: N802
        """Implement check for relative import."""
        if node.level > 0:
            self.errors.append((node.lineno, node.col_offset, ABS101))

        self.generic_visit(node)


class Plugin:
    """Core plugin class for flake8-absolute-import."""

    name: str = "flake8-absolute-import"
    version = __version__

    def __init__(self, tree: ast.Module) -> None:
        """Create plugin instance from the provided AST."""
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type], None, None]:
        """Traverse the AST and collect the errors."""
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
