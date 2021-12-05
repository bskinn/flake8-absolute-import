Credits
=======

`flake8-absolute-import` is authored and maintained by Brian Skinn ([Blog](https://bskinn.github.io)) ([Twitter](https://twitter.com/btskinn)). The skeleton of the AST-based implementation used for this plugin was shamelessly swiped from [`flake8-2020`](https://github.com/asottile/flake8-2020) by [Anthony Sottile](https://github.com/asottile).

While there is disagreement about the upsides and downsides of relative imports in Python, as best this author can tell there are numerous projects and developers out there who desire to hold strictly to absolute imports in their code. The goal of this flake8 plugin is to simplify enforcement of this policy.

v1.0 provides a single catch-all error, `ABS101`, raised on any relative imports found.
