
import os
import re
from inspect import (
    getmembers,
    getdoc,
    ismodule,
    isclass,
    ismethod,
    isfunction,
    signature
)
import pkgutil
import importlib

from mako.template import Template
from mako.lookup import TemplateLookup


def preprocess_mako(text):
    """
    Mako template rendering treats line-initial /##+/ as comments that
    get ignored, but these are important for Markdown. Replace them with
    a substitution ${ s } where s is the hash sequence.
    """
    return re.sub(
        r'(^|(?<=\n))(?P<lead>\s*)(?P<hash>#+)(?P<trail>\s*)',
        r'\g<lead>${"\g<hash>"}\g<trail>',
        text
    )

lookup = TemplateLookup(
    directories=['templates'],
    preprocessor=preprocess_mako,
    strict_undefined=True
)

a_ = None  # prevent NameError

# Python2 and Python3 differ on whether Class.function is a method
def is_method_or_function(obj):
    """
    Return `True` if *obj* is either a bound method or a function.
    """
    return ismethod(obj) or isfunction(obj)

class ApiDown(object):
    """
    This class encapsulates the functions that are made available to all
    templates via the `a_` variable.
    """

    @staticmethod
    def members(obj, predicate=None, filter=None):
        """
        Return all member objects in *obj* that match *predicate* and
        are not filtered by *filter*. This is a wrapper for Python's
        `inspect.getmembers()` with the addition of the filter function.
        """
        return list(
            __builtins__.filter(
                filter,
                [x for _, x in getmembers(obj, predicate)]
            )
        )

    @staticmethod
    def make_filter(
            context=None,
            exclude=None,
            isprivate=False,
            isspecial=False):
        """
        Make a function for filtering results from `ApiDown.members()`.
        Below, *x* is the object to be filtered.

        Args:
            context: if not None, test that the value of
                     `ApiDown.context(x)` is equal to *context*
            exclude: if not None, test that *x* is in *exclude*;
                     *exclude* must be a collection
            isprivate: if not None, test that the value of
                       `ApiDown.isprivate(x)` is equal to *isprivate*
            isspecial: if not None, test that the value of
                       `ApiDown.isspecial(x)` is equal to *isspecial*
        Returns:
            A function that returns `True` if all conditions are
            satisfied, or `False` if any condition fails.
        """
        def filterfunc(x):
            if exclude is not None and x.__name__ in exclude:
                return False
            if context is not None and not ApiDown.incontext(x, context):
                return False
            priv = None if isprivate is None else ApiDown.isprivate(x)
            spec = None if isspecial is None else ApiDown.isspecial(x)
            if not ((priv==isprivate and spec==isspecial)
                    or priv==isprivate==True
                    or spec==isspecial==True):
                return False
            return True
        return filterfunc

    @staticmethod
    def isspecial(obj):
        """
        Return `True` if *obj*'s name begins and ends with `__`.
        """
        name = obj.__name__
        return name[:2]=='__' and name[-2:]=='__'

    @staticmethod
    def isprivate(obj):
        """
        Return `True` if *obj*'s name begins with `_` but doesn't match
        ApiDown.isspecial(*obj*).
        """
        return obj.__name__[:1] == '_' and not ApiDown.isspecial(obj)

    @staticmethod
    def incontext(obj, context):
        """
        Return `True` if the value of ApiDown(*obj*) is in *context*.
        """
        return ApiDown.context(obj) == context

    @staticmethod
    def context(obj):
        """
        Return the containing context of *obj* (e.g. a module's package,
        a class's module, etc.).
        """
        return getattr(obj, '__package__', getattr(obj, '__module__', None))

    @staticmethod
    def packages(obj, **kwargs):
        """
        Return the non-module packages in *obj*.
        Optional keyword arguments are used to define a filter (see
        ApiDown.make_filter()).
        """
        pkg = obj.__name__
        print('packages for', pkg)
        f = ApiDown.make_filter(pkg, **kwargs)
        mods = []
        for _, name, ispkg in pkgutil.iter_modules(obj.__path__):
            print(name, ispkg)
            if ispkg:
                mod = importlib.import_module('.' + name, package=pkg)
                mod.__package__ = pkg
                mods.append(mod)
                print('imported', ApiDown.name(mods[-1]))
                print('context', ApiDown.context(mods[-1]))
        return list(filter(f, mods))

    @staticmethod
    def modules(obj, **kwargs):
        """
        Return the modules in the package *obj*.
        Optional keyword arguments are used to define a filter (see
        ApiDown.make_filter()).
        """
        f = ApiDown.make_filter(obj.__name__, **kwargs)
        return ApiDown.members(obj, ismodule, f)

    @staticmethod
    def classes(obj, **kwargs):
        """
        Return the classes defined in *obj*.
        Optional keyword arguments are used to define a filter (see
        ApiDown.make_filter()).
        """
        f = ApiDown.make_filter(obj.__name__, **kwargs)
        return ApiDown.members(obj, isclass, f)

    @staticmethod
    def methods(obj, **kwargs):
        """
        Return the methods defined in *obj*.
        Optional keyword arguments are used to define a filter (see
        ApiDown.make_filter()).
        """
        f = ApiDown.make_filter(obj.__module__, **kwargs)
        return ApiDown.members(obj, is_method_or_function, f)

    @staticmethod
    def functions(obj, **kwargs):
        """
        Return the functions defined in *obj*.
        Optional keyword arguments are used to define a filter (see
        ApiDown.make_filter()).
        """
        f = ApiDown.make_filter(obj.__name__, **kwargs)
        return ApiDown.members(obj, is_method_or_function, f)

    @staticmethod
    def name(obj):
        """Return the name of *obj*."""
        return obj.__name__

    @staticmethod
    def docstring(obj):
        """Return the docstring of *obj*."""
        return getdoc(obj) or ''

    @staticmethod
    def signature(obj):
        """
        Return the Signature object for callable *obj*. This an instance
        of Python's `inspect.Signature` class.
        """
        return signature(obj)

    @staticmethod
    def render(template, *args, **kwargs):
        """
        Render *template* and return the resulting string.
        """
        t = lookup.get_template(template)
        _kwargs = {'a_': a_}
        _kwargs.update(**kwargs)
        return t.render(*args, **_kwargs)

    @staticmethod
    def blockquote(text):
        """
        Turn a block of text into a blockquote.
        """
        return '\n'.join('> ' + line for line in text.splitlines())

    @staticmethod
    def indent(text, columns=2):
        """
        Turn a block of text into a blockquote.
        """
        return '\n'.join(' ' * columns + line for line in text.splitlines())

    @staticmethod
    def listitem(text, bullet='*'):
        """
        Turn a block of text into a list-item.
        """
        return bullet + ' ' + text.replace('\n', '\n  ')


a_ = ApiDown()

def process(f):
    """
    Print the rendered result of file *f*, which is a Markdown template.
    """
    t = Template(
        filename=f,
        preprocessor=preprocess_mako,
        strict_undefined=True
    )
    print(t.render(a_=a_))

def main(args):
    process(args.template)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Generate Python API documentation in Markdown.'
    )
    parser.add_argument('template', help='The top-level markdown template.')
    args = parser.parse_args()
    main(args)
