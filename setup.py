import os
import sys
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="voipms-python",
    version="0.0.2",
    description="Python wrapper for the voip.ms REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Tesfai",
    author_email="danielmtesfai@gmail.com",
    url="https://github.com/dtesfai/voipms-python",
    license="MIT",
    keywords="voipms api",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.4",
    project_urls={
        "Bug Tracker": "https://github.com/dtesfai/voipms-python/issues",
        "Source Code": "https://github.com/dtesfai/voipms-python",
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)