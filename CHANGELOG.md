## CHANGELOG: flake8-absolute-import -- flake8 plugin to require absolute imports

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project follows an extension of [Semantic
Versioning](http://semver.org/spec/v2.0.0.html), adding a fourth `ADMIN` version
segment.

The plugin interface changes implied by bumps in these SemVer versions are
specific to the error codes emitted by the plugin as part of flake8 execution:

- **Major**
  - Any addition or removal of an error code emitted by the plugin.
  - Any change to the default behavior of the plugin with respect to an existing
    error code.
- **Minor**
  - Addition of new, configurable behavior of the plugin related to an existing
    error code, which is not expected to alter the error code emitting behavior
    of any existing user configurations.
- **Patch**
  - Bugfixes to align the plugin's actual behavior with its stated behavior with
    regard to error codes emitted.
- **Admin**
  - Releases with changes that are expected to have no effect on plugin
    behavior.


### [1.0.0.3] - 2025-11-27

This release contains significant changes, but none that should alter the
behavior of the plugin. Thus, it is being considered an administrative release
despite its scale.

#### Dependencies

- Add formal support for Python 3.13 and 3.14.

- Drop formal support for Python 3.8 and 3.9.

- Increase the minimum permitted Python version to install the package to Python
  3.10.

#### Internal

- Add types to the project code.

#### Administrative

- Upgrade `checkout` and `setup-python` actions.

- Convert Azure Pipelines jobs to GitHub Actions and remove Azure config.
  - The cross-platform auth/auth required to keep Pipelines working just wasn't
    worth the effort to put in place.
  - The cross-platform tests, sdist-install check, and test-dir coverage check
    now all run only on PRs to `stable`.
    - Credentials persistence was disabled for all.
    - All were implemented with pip caching.

- Convert core tests workflow to run on PR, not push, and modernize.
  - Cache pip.
  - Disable credentials persistence.
  - Advance Python versions.

- Remove CodeCov from workflows and requirements.
  - The project/team is far too small for it to be valuable.

- Update copyright end years.

- Convert `README` to Markdown.

- Modernize `pyproject.toml` and `setuptools` config.

- Add multiple `tox` envs:
  - `black`
  - `mypy`
  - `isort`
  - `check` (rollup of `isort`, `black`, `flake8`, `mypy`)
  - `build`


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

