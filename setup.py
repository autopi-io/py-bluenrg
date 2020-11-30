#!/bin/env python

from setuptools import setup, find_packages

setup(
    name="bluenrg",
    version="0.1.0",
    description=("ACI for BlueNRG"),
    author="AutoPi.io",
    author_email="hello@autopi.io",
    url="http://autopi.io",
    license="Copyright 2020 AutoPi.io - All Rights Reserved",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["pyserial==3.*"],
)