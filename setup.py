#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


# monkey patch os.link to force using symlinks
import os
del os.link

setup(name='appname',
    url='https://github.com/michalbachowski/pysyncserver',
    version='0.1.0',
    description='Description',
    license='MIT',
    author='Michał Bachowski',
    author_email='michal@bachowski.pl',
    packages=['appname'],
    package_dir={'': 'src'})
