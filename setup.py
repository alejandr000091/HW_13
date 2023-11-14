#work
from setuptools import setup, find_namespace_packages

setup(name = "book_helper",
      version = "0.1.17",
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['book_helper = hw_12.hw12:main']})