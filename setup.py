# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from setuptools import setup

import xixiang

with open('README.md', 'rb') as readme_file:
    long_description = readme_file.read().decode('utf-8')

with open('requirements.txt') as requirement_file:
    requirements = [_.strip() for _ in requirement_file.readlines() if _]

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
)
