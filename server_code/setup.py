# server_code/setup.py

"""
This setup.py file is used to package the nest_monitor module for github Actions
to run as a scheduled job.
"""

from setuptools import setup, find_namespace_packages

setup(
    name="nest_monitor",
    version="0.1",
    package_dir={"": "server_code"},
    packages=find_namespace_packages(where="server_code"),
)
