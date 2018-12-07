from setuptools import setup, find_packages
from glob import glob

setup(
    name="pydrm",
    version="0.1",
    packages=find_packages(),
    scripts=['clock27.py', 'CounterDemo.py']
)
