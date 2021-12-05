## CHANGELOG: flake8-absolute-import -- flake8 plugin to require absolute imports

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project strives to adhere (mostly) to
[Semantic Versioning](http://semver.org/spec/v2.0.0.html).


### [1.0.0.1] - ####-##-##

This is an administrative/metadata release, primarily to update officially
supported Python versions. There should be no behavior changes between 
this version and v1.0.0.

#### Dependencies

- Support for Python 3.10 and 3.11-dev was officially added

- Support for Python 3.5 was officially removed, though the plugin should
  remain compatible

#### Testing

- Support for running the `tox` matrix on Windows was removed (it doesn't
  seem to work right with the batch-files-in-bin-folder approach I use for
  multiple Pythons in development)

- Routine CI switched from Travis CI to GitHub Actions

- CI and `tox` versions updated to focus on Python 3.10

- `pytest` and `coverage` configs revised to avoid `source`/`include` collision
  in `coverage`

#### Administrative

- `setuptools` configuration has been mostly ported to `setup.cfg`, except for the
  pieces that still need to be defined dynamically

- Built artifacts for distribution should now be created using `build`, which
  has been added to `requirements-dev.txt`


### [1.0.0] - 2019-09-09

#### Features

- Detect any relative imports and report with error code ABS101

