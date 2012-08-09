from setuptools import setup, find_packages
import os

version = '0.1.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='djb.headerproxy',
      version=version,
      description="Paste proxies with the ability to proxy to a location based upon an incoming header",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='proxy paste headers http',
      author='David Beitey',
      author_email='python@davidjb.com',
      url='http://github.com/davidjb/djb.headerproxy/',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['djb'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=[
          'setuptools-git',
      ],
      install_requires=[
          'setuptools',
          'Paste',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = djb.headerproxy:make_header_proxy
      header_proxy = djb.headerproxy:make_header_proxy
      """,
      )
