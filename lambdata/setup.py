# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-mudesir",
    version="1.0",
    author="Mudesir Suleyman",
    author_email="nunasuleyman@gmail.com",
    description="This python modules, packages, enviroment, OOP codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mudesir/lambdata-mudesir",
    packages=find_packages()
)
