#!/usr/bin/env python

"""
Render Markdown from templates.
"""

from __future__ import print_function

import os
import re
from collections import defaultdict, OrderedDict
from contextlib import contextmanager
from io import StringIO

from mako.template import Template
from mako.runtime import Context
from mako.lookup import TemplateLookup
from mako.filters import url_escape

HOME = 'Home'
_default_module_template = 'ghw-api.md'

class RenderDownError(Exception):
    """Error class for RenderDown-specific problems."""
    pass

def md(text):
    """Basic filter for escaping text in Markdown."""
    return re.sub(r'([_*])', r'\\\1', text)

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

def github_sanitize_id(x):
    """
    Sanitize an ID by near-GitHub standards (see toc_filter.rb in
    https://github.com/jch/html-pipeline):
     * remove punctuation besides hyphens and underscores
     * change spaces to hyphens
     * downcase
    Note that it doesn't:
     * add unique suffixes (-1, -2, etc.)
    """
    return re.sub(r'[^-\w ]', '', x.lower(), re.U).replace(' ', '-')

def github_sanitize_filename(x):
    """
    Sanitize a filename by GitHub wiki conventions (see
    https://help.github.com/articles/adding-and-editing-wiki-pages-locally/#naming-wiki-files):

     * remove '\/:*?"<>|'
     * change spaces to hyphens
    """
    return re.sub(r'[\/:*?"<>|]', '', x, re.U).replace(' ', '-')

def sanitize_id(x):
    """
    Sanitize an ID similar to github_sanitize_id, but with the
    following differences:
     * no downcasing
     * dots (.) are replaced with hyphens (which helps Python module
       namespaces look better)
    """
    return re.sub(r'[^-\w ]', '', x.replace('.', '-'), re.U).replace(' ', '-')

class DocManager(object):
    """
    This class encapsulates the document formatting and management
    functions that are made available to all templates via the `doc`
    variable.
    """

    def __init__(self, top=HOME, directories=None, multifile=True):
        if directories is None:
            directories = []
        self._multifile = multifile
        self._anchors = defaultdict(dict)  # {page: {name: anchor_id}}
        self._page_anchors = defaultdict(set)  # {page: {anchor_id}}
        self._pages = OrderedDict([(top, StringIO())])
        self._page_stack = []
        self._level = defaultdict(int)

        self._lookup = TemplateLookup(
            directories=directories + ['templates'],
            preprocessor=preprocess_mako,
            strict_undefined=True,
            imports=['from renderdown import md']
        )

    @property
    def current_page(self):
        """The page name at the top of the page stack."""
        return self._page_stack[-1]

    @property
    def top_page(self):
        """The page name at the bottom of the page stack."""
        return self._page_stack[0]

    @property
    def level(self):
        """
        The current nesting level on the active page.

        The level corresponds to how deep a header will be displayed
        (i.e., how many hashes in an ATX-style header).
        """
        return self._level[self.current_page]

    def render(self, filename, page=None, *args, **kwargs):
        """
        Render template given by *filename*.

        If *page* is None, the rendered string is returned, otherwise
        it is written to the buffer assigned to *page*.
        """
        if page is not None:
            # ensure buffer exists (do before render for proper order)
            self._pages.setdefault(page, StringIO())
            self._page_stack.append(page)

        self._level[self.current_page] += 1

        t = self._lookup.get_template(filename)
        _kwargs = {'doc': self}
        _kwargs.update(**kwargs)
        text = t.render(*args, **_kwargs)

        self._level[self.current_page] -= 1

        if page is None:
            return text  # simple call, just return text
        else:
            # call to new page; manage stack and write to buffer
            last = self._page_stack.pop()
            assert page == last
            self.write(text, page=page)
            return ''

    def write(self, text, page=None):
        """
        Write *text* to the buffer of *page*; if *page* is None, write
        to the current page.
        """
        if page is None:
            page = self.current_page
        self._pages.setdefault(page, StringIO()).write(text)

    @property
    def pages(self):
        """Tuples of (pagename, contents) for all pages."""
        return [
            (name, buf.getvalue())
            for name, buf in self._pages.items()
        ]

    def register_anchor(self, name=None, page=None):
        """
        Find a unique, sanitized anchor for *name* using the name of *name*.
        If output is a single page, URIs are prepended with *page*.
        When *page* is `None`, the current page is used. The URI is
        registered to the id of *name* and then a tuple `(uri, page)`
        is returned. If the object has already been registered, the
        tuple for the original registration is returned and nothing
        else is done.
        """
        if page is None:
            page = self.current_page
        if name in self._anchors[page]:
            if name is None:
                msg = '"{}" in page "{}"'.format(name, page)
            else:
                msg = 'page "{}"'.format(page)
            raise RenderDownError(
                'An anchor for {} is already registered: #{}'
                .format(msg, self._anchors[page][name])
            )
        page_anchors = self._page_anchors[page]
        sanitized_name = (sanitize_id(name) + '-') if name else ''
        anchor, i = sanitized_name, 1
        while anchor in page_anchors:
            anchor = '%s%d' % (sanitized_name, i)
            i += 1
        anchor = anchor.rstrip('-')  # in case it was already unique
        page_anchors.add(anchor)
        self._anchors[page][name] = anchor
        return (anchor, page)

    def anchor(self, name=None, page=None):
        """
        Return the anchor for the given *name* and *page*.
        """
        if page is None:
            page = self.current_page
        if not (page in self._anchors and name in self._anchors[page]):
            self.register_anchor(name=name, page=page)
        anchor_id = self._anchors[page][name]
        if self._multifile:
            if page == self.current_page:
                anchor = '#%s' % (anchor_id,)
            elif anchor_id:
                anchor = '%s#%s' % (page, anchor_id)
            else:
                anchor = page
        else:
            anchor = ('#%s-%s'if anchor_id else '#%s%s') % (page, anchor_id)
        return anchor

    def header(self, text, level=None):
        """
        Return an ATX-style header at level *level* and header text
        *text*. If *level* is `None`, use the current level of page
        descent.
        """
        # register anchor?
        if level is None:
            level = self.level
        if level > 6:
            level = 6
        return '{} {}'.format('#' * level, text)

    @contextmanager
    def section(self):
        """
        A context manager that increases the nesting level.
        """
        self._level[self.current_page] += 1
        yield
        self._level[self.current_page] -= 1

    @staticmethod
    def blockquote(text):
        """
        Turn a block of text into a blockquote.
        """
        return '\n'.join('> ' + line for line in text.splitlines())

    @staticmethod
    def indent(text, columns=2):
        """
        Indent a block of text by *columns* spaces.
        """
        return '\n'.join(' ' * columns + line for line in text.splitlines())

    @staticmethod
    def listitem(text, body=None, bullet='*'):
        """
        Turn a block of text into a list-item.
        """
        li = '{} {}{}'.format(
            bullet,
            text.replace('\n', '\n  '),
            '' if body is None else '\n  \n' + DocManager.indent(body, columns=2)
        )
        return re.sub(r'(\n  ){3,}', r'\n  \n  ', li)


def main(args):
    multifile = (args.outdir is not None)
    kwargs = {}
    dirs = []

    if args.assignments:
        for a in args.assignments:
            key, value = a.split('=', 1)
            kwargs[key] = value

    if os.path.isfile(args.template):
        t = os.path.basename(args.template)
        dirs.append(os.path.dirname(args.template))
    else:
        t = args.template

    doc = DocManager(directories=dirs, multifile=multifile)
    doc.render(t, page=HOME, **kwargs)

    if args.outdir:
        if not os.path.isdir(args.outdir):
            os.mkdir(args.outdir)
        for name, text in doc.pages:
            gh_name = github_sanitize_filename(name)
            with open(os.path.join(args.outdir, gh_name + '.md'), 'w') as out:
                print(text, file=out)
    else:
        pages = doc.pages
        if pages:
            print(pages[0][1])
        for name, text in pages[1:]:
            print('\n\n-----\n\n# {}\n\n'.format(name))
            print(text)
    if args.list_anchors:
        for page, name_anchor in doc._anchors.items():
            for name, anchor in name_anchor.items():
                print('{}\t{}\t{}'.format(anchor, page, name))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Generate Markdown from templates.'
    )
    parser.add_argument(
        'template', help='the template to render'
    )
    parser.add_argument(
        '-a', '--assign',
        action='append', dest='assignments',
        help='assign a variable to be passed to the template '
             '(e.g., `--assign title="Hello World"`)'
    )
    parser.add_argument(
        '-o', '--outdir',
        help='the output directory for generated files; if not given, '
             'all pages are joined and printed to stdout'
    )
    parser.add_argument(
        '--list-anchors',
        action='store_true',
        help='list the generated anchors at the end.'
    )

    args = parser.parse_args()

    if not (args.template or args.module):
        raise RenderDownError('Either --template or --module must be specified.')

    main(args)
