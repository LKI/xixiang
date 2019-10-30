from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup

import xixiang

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="xixiang",
    version=xixiang.__version__,
    description="unofficial xixiang python sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lirian Su",
    author_email="liriansu@gmail.com",
    url="https://github.com/LKI/xixiang",
    license="MIT License",
    packages=["xixiang"],
    install_requires=convert_deps_to_pip(Project(chdir=False).parsed_pipfile["packages"], r=False),
)
