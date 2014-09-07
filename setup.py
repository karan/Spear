#!/usr/bin/env python

from setuptools import setup

setup(
  name='spear-cli',
  version='0.0.3',
  description='Product Hunt for Hackers.',
  author='Karan Goel',
  license='MIT',
  keywords = "product hunt product hunt feed rss tool cli",
  author_email='karan@goel.im',
  url='http://github.com/karan/Spear',
  scripts=['spear.py'],
  install_requires=[
    "click==2.1",
    "requests==2.4.0",
  ],
  entry_points = {
    'console_scripts': [
        'hunt = spear:main'
    ],
  }
)
