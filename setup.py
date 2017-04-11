#!/usr/bin/env python

from distutils.core import setup

from io import open

def read_long_description():
    with open('README.rst', encoding='utf-8') as readme_file:
        readme_file.read()

def setup_package():
    setup(
        name = 'heapwrap',
        packages = ['heapwrap'],
        version = '1.0',
        description = 'min and max heap wrapping heapq',
        long_description = read_long_description(),
        package_dir = {'': 'src'},
        author = 'Sumant Manne',
        author_email = 'sumant.manne@gmail.com',
        license = 'MIT',
        url = 'https://github.com/dpyro',
        keywords = ['heap', 'max', 'min'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ]
    )

if __name__ == '__main__':
    setup_package()
