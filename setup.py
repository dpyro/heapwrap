#!/usr/bin/env python

from distutils.core import setup

def setup_package():
    setup(
        name = 'heapwrap',
        packages = ['heapwrap'],
        version = '1.0',
        description = 'min and max heap wrapping heapq',
        package_dir = {'': 'src'},
        author = 'Sumant Manne',
        author_email = 'sumant.manne@gmail.com',
        license = 'MIT',
        url = 'https://github.com/dpyro',
        keywords = ['heap', 'max', 'min'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3'
        ]
    )

if __name__ == '__main__':
    setup_package()
