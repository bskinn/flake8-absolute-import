import re
from pathlib import Path
from setuptools import find_packages, setup


exec_ns = {}
exec(
    Path("src", "flake8_absolute_import", "version.py").read_text(encoding="utf-8"),
    exec_ns,
)
__version__ = exec_ns["__version__"]

NAME = "flake8-absolute-import"
version_override = None


def readme():
    content = Path("README.rst").read_text()

    new_ver = version_override if version_override else __version__

    # Helper function
    def content_update(content, pattern, sub):
        return re.sub(pattern, sub, content, flags=re.M | re.I)

    # Docs reference updates to current release version, for PyPI
    # This one gets the badge image
    content = content_update(
        content, rf"(?<=/readthedocs/{NAME}/)\S+?(?=\.svg$)", "v" + new_ver
    )

    # This one gets the RtD links
    content = content_update(
        content, rf"(?<={NAME}\.readthedocs\.io/en/)\S+?(?=/)", "v" + new_ver
    )

    return content


setup(
    long_description=readme(),
    long_description_content_type="text/x-rst",
)
