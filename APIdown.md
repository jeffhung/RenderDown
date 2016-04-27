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
> ```
> <% import mymodule %>
> ${ a_.render("module.md", obj=mymodule) }
> ```
> 
> The `module.md` template may then iterate classes, functions, etc.:
> 
> ```
> # ${ a_.name(obj) }
> 
> ${ a_.docstring(obj) }
> 
> % for f in a_.functions(obj, exclude=['main']):
> ${ a_.render("function.md", obj=f) }
> % endfor
> ```

## Classes

* **ApiDown**
  <a name="ApiDown" href="#ApiDown">#</a>
  
  This class encapsulates the functions that are made available to all
  templates via the `a_` variable.
  
  * ApiDown.**blockquote**(text)
    <a name="ApiDown.blockquote" href="#ApiDown.blockquote">#</a>
    
    Turn a block of text into a blockquote.
  
  * ApiDown.**classes**(obj, **kwargs)
    <a name="ApiDown.classes" href="#ApiDown.classes">#</a>
    
    Return the classes defined in *obj*.
    Optional keyword arguments are used to define a filter (see
    ApiDown.make_filter()).
  
  * ApiDown.**context**(obj)
    <a name="ApiDown.context" href="#ApiDown.context">#</a>
    
    Return the containing context of *obj* (e.g. a module's package,
    a class's module, etc.).
  
  * ApiDown.**docstring**(obj)
    <a name="ApiDown.docstring" href="#ApiDown.docstring">#</a>
    
    Return the docstring of *obj*.
  
  * ApiDown.**functions**(obj, **kwargs)
    <a name="ApiDown.functions" href="#ApiDown.functions">#</a>
    
    Return the functions defined in *obj*.
    Optional keyword arguments are used to define a filter (see
    ApiDown.make_filter()).
  
  * ApiDown.**incontext**(obj, context)
    <a name="ApiDown.incontext" href="#ApiDown.incontext">#</a>
    
    Return `True` if the value of ApiDown(*obj*) is in *context*.
  
  * ApiDown.**indent**(text, columns=2)
    <a name="ApiDown.indent" href="#ApiDown.indent">#</a>
    
    Turn a block of text into a blockquote.
  
  * ApiDown.**isprivate**(obj)
    <a name="ApiDown.isprivate" href="#ApiDown.isprivate">#</a>
    
    Return `True` if *obj*'s name begins with `_` but doesn't match
    ApiDown.isspecial(*obj*).
  
  * ApiDown.**isspecial**(obj)
    <a name="ApiDown.isspecial" href="#ApiDown.isspecial">#</a>
    
    Return `True` if *obj*'s name begins and ends with `__`.
  
  * ApiDown.**listitem**(text, bullet='*')
    <a name="ApiDown.listitem" href="#ApiDown.listitem">#</a>
    
    Turn a block of text into a list-item.
  
  * ApiDown.**make_filter**(context=None, exclude=None, isprivate=False, isspecial=False)
    <a name="ApiDown.make_filter" href="#ApiDown.make_filter">#</a>
    
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
  
  * ApiDown.**members**(obj, predicate=None, filter=None)
    <a name="ApiDown.members" href="#ApiDown.members">#</a>
    
    Return all member objects in *obj* that match *predicate* and
    are not filtered by *filter*. This is a wrapper for Python's
    `inspect.getmembers()` with the addition of the filter function.
  
  * ApiDown.**methods**(obj, **kwargs)
    <a name="ApiDown.methods" href="#ApiDown.methods">#</a>
    
    Return the methods defined in *obj*.
    Optional keyword arguments are used to define a filter (see
    ApiDown.make_filter()).
  
  * ApiDown.**modules**(obj, **kwargs)
    <a name="ApiDown.modules" href="#ApiDown.modules">#</a>
    
    Return the modules in the package *obj*.
    Optional keyword arguments are used to define a filter (see
    ApiDown.make_filter()).
  
  * ApiDown.**name**(obj)
    <a name="ApiDown.name" href="#ApiDown.name">#</a>
    
    Return the name of *obj*.
  
  * ApiDown.**packages**(obj, **kwargs)
    <a name="ApiDown.packages" href="#ApiDown.packages">#</a>
    
    Return the non-module packages in *obj*.
    Optional keyword arguments are used to define a filter (see
    ApiDown.make_filter()).
  
  * ApiDown.**render**(template, *args, **kwargs)
    <a name="ApiDown.render" href="#ApiDown.render">#</a>
    
    Render *template* and return the resulting string.
  
  * ApiDown.**signature**(obj)
    <a name="ApiDown.signature" href="#ApiDown.signature">#</a>
    
    Return the Signature object for callable *obj*. This an instance
    of Python's `inspect.Signature` class.
  
  

## Functions

* **is_method_or_function**(obj)
  <a name="is_method_or_function" href="#is_method_or_function">#</a>
  
  Return `True` if *obj* is either a bound method or a function.

* **preprocess_mako**(text)
  <a name="preprocess_mako" href="#preprocess_mako">#</a>
  
  Mako template rendering treats line-initial /##+/ as comments that
  get ignored, but these are important for Markdown. Replace them with
  a substitution ${ s } where s is the hash sequence.

* **process**(f)
  <a name="process" href="#process">#</a>
  
  Print the rendered result of file *f*, which is a Markdown template.


