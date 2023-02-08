#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import extended_settings

# description
long_description = open('README.md').read()

# setup
setup(
    name='django-extended-settings',
    version=extended_settings.__version__,

    packages=find_packages(exclude=('tests.*', 'tests', 'example')),

    author="MickBad",
    author_email="prog@mickbad.com",
    description="Extended Settings for Django Project with settings.d/",

    long_description=long_description,
    long_description_content_type='text/markdown',

    install_requires=[
        "Django>=2.0",
    ],

    python_requires=">=3.5",

    # activate MANIFEST.in
    include_package_data=True,

    # github source
    url='https://github.com/mickbad/django-extended-settings',
    download_url='https://pypi.org/project/django-extended-settings/',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],

    license="BSD",

    keywords="django development tools settings",
)
