#!/usr/bin/env python3

from setuptools import setup

setup(
    name="cb-psc-integration",
    version="0.0.1",
    url="https://developer.carbonblack.com/",
    license="MIT",
    author="Carbon Black",
    author_email="dev-support@carbonblack.com",
    description="Carbon Black PSC Integration Library",
    long_description=__doc__,
    packages=["cb.psc.integration"],
    package_dir={"": "src"},
    platforms="any",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        # TODO(ww): Replace with stable version once merged and released.
        "cbapi @ git+ssh://git@github.com/trailofbits/cbapi-python@tob-cbth-binaries#egg=cbapi",
        "Flask",
        "redis",
        "requests",
        "rq",
        "supervisor @ git+https://github.com/Supervisor/supervisor",
        "SQLAlchemy",
    ],
)
