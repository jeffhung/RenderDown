# RenderDown

[![Build Status](https://travis-ci.com/jeffhung/RenderDown.svg?branch=master)](https://travis-ci.com/jeffhung/RenderDown)

Generate Markdown text from templates; that is, the result of
rendering is Markdown text, not HTML. This is useful for
generating documents published on a Markdown platform like
[GitHub Wikis](https://help.github.com/articles/about-github-wikis/).

## Usage

The simplest way to use RenderDown is to invoke it from the
commandline:

    renderdown.py TEMPLATE [--assign KEY=VALUE] [--outdir OUTDIR]

The required *TEMPLATE* argument is the path to a template file.
Simple variables may be passed to the template with the `--assign`
option. If the `--outdir` option is set, multi-file documents can be
created, written to files in the output directory; if unset, the
multiple pages are appended together and printed to stdout.

RenderDown can also be used as a library. The [API.md](API.md) file
(generated using RenderDown and [CartogrAPI][]) is a reference of
RenderDown's API.

## Templates

Templates are rendered with [Mako][]. A `doc` variable is added to the
namespace of all templates (see [API.md](API.md#renderdown-DocManager)
for a description of the functions on `doc`). For example, if
`mytemp.mako` is a template defined as follows:

```
# ${title}

Here are two bullet points:
${ doc.listitem("the first point") }
${ doc.listitem("note how wrapped lines\nare indented") }

${ doc.blockquote(
    "the same is true for blockquotes, except the > character is\n"
    "repeated on the wrapped lines.")
}
```

The the following call the RenderDown will render the template:

```
$ python renderdown.py example.md --assign title="Hello World"
# Hello World

Here are two bullet points:
* the first point
* note how wrapped lines
  are indented

> the same is true for blockquotes, except the > character is
> repeated on the wrapped lines.
```

The original use case for rendering Markdown is for publishing Python
API documentation on GitHub Wikis, so the default
[templates](templates) target that platform.

The [templates](../../tree/master/templates) are defined for rendering
packages, modules, classes, methods, and functions in a fairly
generic way (inspired by  documentation), but they
can be reconfigured and specialized for individual projects.

## Requirements

- Python 3.3+
- [Mako][]

## How to Test

Run the following command to test:

```console
$ pip install -r requirements.txt   # install dependencies
$ pip install -e .                  # to import in tests
$ python setup.py test              # run the test cases
```

## License

MIT; see [LICENSE](LICENSE) for more information.

## Project History

This project was created by Michael Wayne Goodman
([@goodmami](https://github.com/goodmami)) and is now owned and maintained by
Jeff Hung ([@jeffhung](https://github.com/jeffhung)).

## Links

- [Mako](http://makotemplates.org/) - templating engine
- [D3.js][]'s [wiki](https://github.com/mbostock/d3/wiki) - provided
  aesthetic inspiration for the wiki organization
- [CartogrAPI][] - used to map out Python APIs
- Related Software:
    + [doc2md](https://github.com/coldfix/doc2md)
    + [pdoc](https://github.com/BurntSushi/pdoc)
    + [Sphinx AutoAPI](https://github.com/rtfd/sphinx-autoapi)

[Mako]: http://makotemplates.org/
[D3.js]: https://d3js.org/
[CartogrAPI]: https://github.com/goodmami/cartograpi