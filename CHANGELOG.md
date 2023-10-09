## CHANGELOG: flake8-absolute-import -- flake8 plugin to require absolute imports

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project strives to adhere (mostly) to
[Semantic Versioning](http://semver.org/spec/v2.0.0.html).


### [1.0.0.2] - 2023-10-08

This is an administrative release, primarily to update officially supported
Python and flake8 versions. There should be no plugin behavior changes between
this version and v1.0.0.1.

#### Dependencies

- Support for Python 3.12 was officially added

- Support for Python 3.6 and 3.7 was officially removed, though the plugin
  should continue to work for Python 3.6+

- The minimum supported flake8 version is now 5.0

#### Administrative

- `MANIFEST.in` was augmented with the files needed to allow the test suite to
  run from an unpacked sdist.

- The build metadata was completely migrated from `setup.cfg` to
  `pyproject.toml`, and the maximum possible metadata is now drawn from
  `pyproject.toml` (all but `long_description`).

- The read of the project version and the load of the README contents in
  `setup.py` was modernized/improved.

#### Testing

- Python versions in the GitHub Actions and Azure Pipelines matrices were updated.

- An Azure Pipelines job was added to confirm that a built sdist carries all the
  files needed to allow the test suite to run.

- Obscure parameters/variables in some tests were given better names, and string
  formatting was upgraded to use f-strings.


### [1.0.0.1] - 2021-12-04

This is an administrative/metadata release, primarily to update officially
supported Python versions. There should be no behavior changes between 
this version and v1.0.0.

#### Dependencies

- Support for Python 3.10 and 3.11-dev was officially added.

- Support for Python 3.5 was officially removed, though the plugin should remain
  compatible.

#### Testing

- Support for running the `tox` matrix on Windows was removed (it doesn't seem
  to work right with the batch-files-in-bin-folder approach I use for multiple
  Pythons in development).

- Routine CI was switched from Travis CI to GitHub Actions.

- CI and `tox` versions were updated to focus on Python 3.10.

- `pytest` and `coverage` configs were revised to avoid `source`/`include`
  collision in `coverage`.

#### Administrative

- `setuptools` configuration has been mostly ported to `setup.cfg`, except for the
  pieces that still need to be defined dynamically.

- Built artifacts for distribution should now be created using `build`, which
  has been added to `requirements-dev.txt`.


### [1.0.0] - 2019-09-09

#### Features

- Detect any relative imports and report with error code ABS101.

