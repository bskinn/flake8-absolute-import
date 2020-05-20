import re
from pathlib import Path
from setuptools import find_packages, setup


with Path("src", "flake8_absolute_import", "version.py").open() as f:
    exec(f.read())

NAME = "flake8-absolute-import"


version_override = None


def readme():
    with open("README.rst", "r") as f:
        content = f.read()

    new_ver = version_override if version_override else __version__

    # Helper function
    def content_update(content, pattern, sub):
        return re.sub(pattern, sub, content, flags=re.M | re.I)

    # Docs reference updates to current release version, for PyPI
    # This one gets the badge image
    content = content_update(
        content, r"(?<=/readthedocs/{0}/)\S+?(?=\.svg$)".format(NAME), "v" + new_ver
    )

    # This one gets the RtD links
    content = content_update(
        content, r"(?<={0}\.readthedocs\.io/en/)\S+?(?=/)".format(NAME), "v" + new_ver
    )

    return content


setup(
    name=NAME,
    version=__version__,
    description="flake8 plugin to require absolute imports",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    url="https://github.com/bskinn/flake8-absolute-import",
    license="MIT License",
    author="Brian Skinn",
    author_email="bskinn@alum.mit.edu",
    packages=find_packages("src"),
    package_dir={"": "src"},
    provides=["flake8_absolute_import"],
    python_requires=">=3.4",
    requires=["flake8 (>=3.7)"],
    install_requires=["flake8>=3.7"],
    classifiers=[
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Quality Assurance",
        "Development Status :: 5 - Production/Stable",
    ],
    entry_points={"flake8.extension": ["ABS1 = flake8_absolute_import:Plugin"]},
)
