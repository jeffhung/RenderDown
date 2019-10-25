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
    setup_requires   = [ 'pytest-runner' ],
    tests_require    = [ 'pytest' ],
    author           = 'Jeff Hung',
    author_email     = 'jeff.cc.hung@gmail.com',
    description      = 'Generate Markdown text from templates.',
    url              = 'https://github.com/jeffhung/RenderDown',
    license          = 'MIT',
    classifiers      = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ]
)

