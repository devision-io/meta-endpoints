#!/usr/bin/env python
from os import path

import setuptools


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


from metaendpoints import info

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

packages = [
    'metaendpoints',
    'metaendpoints.tools'
]

install_reqs = parse_requirements('requirements.txt')
reqs = install_reqs

setuptools.setup(
    name=info.__package_name__,
    version=info.__version__,

    description='Devision Meta Endpoints',
    long_description=long_description,

    url='https://github.com/devision-io/metaendpoints',

    author='Artur Geraschenko',
    author_email='arturgspb@gmail.com',

    license='MIT',

    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=reqs,
    packages=packages,
    package_data={
        '': ['LICENSE']
    },
    package_dir={'metaendpoints': 'metaendpoints'},
    include_package_data=True,
)
