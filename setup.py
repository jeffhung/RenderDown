from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name             = 'renderdown',
    version          = '0.2.0',
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
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url              = 'https://github.com/jeffhung/RenderDown',
    license          = 'MIT',
    classifiers      = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ]
)

