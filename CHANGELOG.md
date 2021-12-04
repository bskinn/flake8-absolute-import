## CHANGELOG: flake8-absolute-import -- flake8 plugin to require absolute imports

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project strives to adhere to
[Semantic Versioning](http://semver.org/spec/v2.0.0.html).


### Unreleased Changes

#### Added

- Support for Python 3.10 and 3.11-dev was officially added

#### Removed

- Support for Python 3.5 was officially removed (the plugin may remain compatible,
  but this is not guaranteed)

#### Testing

- Support for running the `tox` matrix on Windows was removed (it doesn't
  seem to work right with the batch-files-in-bin-folder approach I use for
  multiple Pythons in development)

- Routine CI switched from Travis CI to GitHub Actions

- CI and `tox` versions updated to focus on Python 3.10


### [1.0.0] - 2019-09-09

#### Features

- Detect any relative imports and report with error code ABS101

