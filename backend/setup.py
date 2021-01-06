import re

from setuptools import find_packages
from setuptools import setup

with open('orion/__init__.py', mode='rt', encoding='utf-8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

setup(name='orion',
      version=version,
      description='A simple IT asset management RESTful API backend.',
      url='https://github.com/sdg32/orion',
      author='sdg32',
      author_email='',
      packages=find_packages(exclude=['tests', 'tests.*', '*.tests',
                                      '*.tests.*']),
      include_package_data=True,
      zip_safe=False,
      python_requires='~=3.9.0',
      install_requires=[
          'fastapi~=0.63.0',
          'pydantic~=1.7.3',
          'python-dotenv~=0.15.0',
          'uvicorn~=0.13.3',
      ],
      tests_require=[
          'pytest',
          'pytest-cov',
      ],
      extras_require={})
