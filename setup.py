#!/usr/bin/env python
# -*- encoding: utf-8

import os
import json
from setuptools import setup, find_packages

PROJ_NAME = "py4bio"
PACKAGE_NAME = "py4bio"

PROJ_METADATA = "%s.json" % PROJ_NAME

here = os.path.abspath(os.path.dirname(__file__))
proj_info = json.loads(open(os.path.join(here, PROJ_METADATA), encoding="utf-8").read())
README = open(os.path.join(here, "README.md"), encoding="utf-8").read()

setup(
    name=proj_info["name"],
    version=proj_info["version"],
    author=proj_info["author"],
    author_email=proj_info["author_email"],
    license=proj_info["license"],
    description=proj_info["description"],
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    test_suite="tests",
    platforms="Linux",
    include_package_data=True,
    classifiers=proj_info["classifiers"],
    entry_points={"console_scripts": proj_info["console_scripts"]},
)
