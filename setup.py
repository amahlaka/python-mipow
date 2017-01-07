#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = 0.1

setup(
    name='mipow',
    version=0.1,
    author='Arttu Mahlakaarto',
    author_email='Arttu.mahlakaarto@gmail.com',
    url='http://github.com/amahlaka/python-mipow',
    packages=find_packages(),
    download_url='https://github.com/amahlaka/python-mipow/tarball/0.1',
    scripts=[],
    description='Python API for controlling Mipow Smart LED bulbs',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
