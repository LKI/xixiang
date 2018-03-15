# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from setuptools import setup

import xixiang

with open('README.md', 'rb') as f:
    long_description = f.read().decode('utf-8')

with open('requirements.txt') as f:
    requirements = [_.strip() for _ in f.readlines() if _]

setup(
    name='xixiang',
    version=xixiang.__version__,
    description='xixiang order sdk',
    long_description=long_description,
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/hui-z/xixiang',
    license='MIT License',
    packages=['xixiang'],
    install_requires=requirements,
)
