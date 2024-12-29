# setup.py
from setuptools import setup, find_namespace_packages

setup(
    name="home_automation",
    version="0.1",
    packages=find_namespace_packages(include=["server_code.*"]),
    package_dir={"": "."},
)
