import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = "-n auto"

    def run_tests(self):
        import shlex
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

here = os.path.abspath(os.path.dirname(__file__))

version_contents = {}
with open(os.path.join(here, "voipms", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

setup(
    name="voipms-python",
    version=version_contents["VERSION"],
    description="Python wrapper for the voip.ms REST API",
    author="Daniel Tesfai",
    author_email="danielmtesfai@gmail.com",
    url="https://github.com/dtesfai/voipms-python",
    license="MIT",
    keywords="voipms api",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"'
    ],
    python_requires=">=3.4",
    tests_require=[
        "pytest >= 4.6.2, < 4.7",
        "pytest-mock >= 1.10.4",
        "pytest-xdist >= 1.28.0",
        "pytest-cov >= 2.7.1",
        # coverage 5.0 pre-releases don't work, and setuptools doesn't ignore
        # pre-releases (cf. https://github.com/pypa/setuptools/issues/855)
        "coverage >= 4.5.3, < 5",
    ],
    cmdclass={"test": PyTest},
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