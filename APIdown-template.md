<% import apidown %>\
# APIdown


APIdown renders Markdown templates with convenient access to Python's
code introspection tools, which makes it useful for automatically
producing API documentation. The code introspection is not required,
so it could also be used for general-purpose Markdown generation.
For more information on the templating functions, see Mako's
[documentation](http://docs.makotemplates.org/en/latest/). Note that
APIdown disables Mako's double-hash (`##`) comments, since those are
important for Markdown.

> **Basic Usage**
> 
> Create a Markdown template to start the process. The `a_` variable
> allows access to APIdown's code inspection and formatting functions.
> Import a Python module and iterate its members:
> 
> ```<%text>
> <% import mymodule %>
> ${ a_.render("module.md", obj=mymodule) }
> ```</%text>
> 
> The `module.md` template may then iterate classes, functions, etc.:
> 
> ```<%text>
> # ${ a_.name(obj) }
> 
> ${ a_.docstring(obj) }
> 
> % for f in a_.functions(obj, exclude=['main']):
> ${ a_.render("function.md", obj=f) }
> % endfor
> ```</%text>

## Classes

${ a_.listitem(a_.render("class.md", obj=apidown.ApiDown)) }

## Functions

% for f in a_.functions(apidown, exclude=['main']):
${ a_.listitem(a_.render("function.md", obj=f)) }

% endfor
