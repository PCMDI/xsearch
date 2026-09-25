from setuptools import find_packages, setup

version = '0.1.0'

packages = find_packages(include=['xsearch'])

setup(
    name="xsearch",
    version=version,
    author="@pochedls",
    description="xsearch search utility",
    url="https://github.com/PCMDI/xsearch",
    packages=packages,
)

