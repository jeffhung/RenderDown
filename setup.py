from setuptools import setup, find_packages
import os

setup(
    name             = 'renderdown',
    version          = '0.1.0',
    py_modules       = [ 'renderdown' ],
    entry_points     = {
        'console_scripts': [ 'renderdown=renderdown:main' ],
    },
    install_requires = [ 'mako' ],
    author           = 'Michael Wayne Goodman',
    author_email     = 'goodman.m.w@gmail.com',
    description      = 'Generate Markdown text from templates.',
    url              = 'https://github.com/goodmami/RenderDown',
    license          = 'MIT',
    classifiers      = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ]
)

