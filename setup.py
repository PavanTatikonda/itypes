#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys


def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open('itypes.py').read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version()


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='itypes',
    version=version,
    url='http://github.com/PavanTatikonda/itypes',
    license='BSD',
    description='Simple immutable types for python.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Tom Christie',
    author_email='tom@tomchristie.com',
    py_modules=['itypes'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
