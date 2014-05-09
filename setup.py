# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='switchcache',
    version='0.0.1',
    description='Utils for testing with/without cache',
    author='Shoji Ihara',
    author_email='shoji.ihara@gmail.com',
    url='http://github.com/shoz/switchcache',
    packages=find_packages(),
    license=open('LICENSE').read(),
    include_package_data=True,
    keywords=['memcached', 'test', 'testing', 'decorators'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
    tests_require=['nose'],
    test_suite = 'nose.collector'
)
