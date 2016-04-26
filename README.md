# APIdown

Automatically generate API documentation with Markdown

Markdown templates are rendered with [Mako][]. For instance, the
[API documentation](APIdown.md) for APIdown was rendered from
[this template](APIdown-template.md) with the following command:

    $ python3 apidown.py APIdown-template.md > APIdown.md

The [templates](../../tree/master/templates) are defined for rendering
packages, modules, classes, methods, and functions in a fairly
generic way (inspired by [D3.js][]'s
[wiki](https://github.com/mbostock/d3/wiki) documentation), but they
can be reconfigured and specialized for individual projects.

## Requirements

- Python 3.3+
- [Mako][]

## License

MIT; see [LICENSE](LICENSE) for more information.

[Mako]: http://makotemplates.org/
[D3.js]: https://d3js.org/
