import os

from setuptools import setup, find_packages

if os.environ.get('USER', '') == 'vagrant':
  del os.link


setup(
  name='tvbuff',
  version='0.0.9',
  description='TV buff is a command line guide that helps you track your favorite shows',
  long_description=open('README.rst').read(),
  author='gs0510',
  author_email='gs051095@gmail.com',
  license='MIT',
  keywords=['tv-guide', 'command line', 'cli', 'tvmaze'],
  url='https://github.com/gs0510/tvbuff',
  packages=find_packages(exclude=['contrib', 'docs', 'tests']),
  install_requires=[
    'docopt>=0.6.2',
    'requests>=2.8.0',
    'tabulate==0.7.5'
  ],
  entry_points={
    'console_scripts': [
        'tvbuff = tvbuff.tvbuff:main'
    ],
  }
)