
### apidown



#### Classes {#apidown-classes}

<a name="ApiDown" href="#ApiDown">#</a> **ApiDown**

This class encapsulates the functions that are made available to all
templates via the `a_` variable.


<a name="ApiDown.blockquote" href="#ApiDown.blockquote">#</a> ApiDown.**blockquote**(text)

Turn a block of text into a blockquote.

<a name="ApiDown.classes" href="#ApiDown.classes">#</a> ApiDown.**classes**(obj, **kwargs)

Return the classes defined in *obj*.
Optional keyword arguments are used to define a filter (see
ApiDown.make_filter()).

<a name="ApiDown.context" href="#ApiDown.context">#</a> ApiDown.**context**(obj)

Return the containing context of *obj* (e.g. a module's package,
a class's module, etc.).

<a name="ApiDown.docstring" href="#ApiDown.docstring">#</a> ApiDown.**docstring**(obj)

Return the docstring of *obj*.

<a name="ApiDown.functions" href="#ApiDown.functions">#</a> ApiDown.**functions**(obj, **kwargs)

Return the functions defined in *obj*.
Optional keyword arguments are used to define a filter (see
ApiDown.make_filter()).

<a name="ApiDown.incontext" href="#ApiDown.incontext">#</a> ApiDown.**incontext**(obj, context)

Return `True` if the value of ApiDown(*obj*) is in *context*.

<a name="ApiDown.isprivate" href="#ApiDown.isprivate">#</a> ApiDown.**isprivate**(obj)

Return `True` if *obj*'s name begins with `_` but doesn't match
ApiDown.isspecial(*obj*).

<a name="ApiDown.isspecial" href="#ApiDown.isspecial">#</a> ApiDown.**isspecial**(obj)

Return `True` if *obj*'s name begins and ends with `__`.

<a name="ApiDown.make_filter" href="#ApiDown.make_filter">#</a> ApiDown.**make_filter**(context=None, exclude=None, isprivate=False, isspecial=False)

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

<a name="ApiDown.members" href="#ApiDown.members">#</a> ApiDown.**members**(obj, predicate=None, filter=None)

Return all member objects in *obj* that match *predicate* and
are not filtered by *filter*. This is a wrapper for Python's
`inspect.getmembers()` with the addition of the filter function.

<a name="ApiDown.methods" href="#ApiDown.methods">#</a> ApiDown.**methods**(obj, **kwargs)

Return the methods defined in *obj*.
Optional keyword arguments are used to define a filter (see
ApiDown.make_filter()).

<a name="ApiDown.modules" href="#ApiDown.modules">#</a> ApiDown.**modules**(obj, **kwargs)

Return the modules in the package *obj*.
Optional keyword arguments are used to define a filter (see
ApiDown.make_filter()).

<a name="ApiDown.name" href="#ApiDown.name">#</a> ApiDown.**name**(obj)

Return the name of *obj*.

<a name="ApiDown.packages" href="#ApiDown.packages">#</a> ApiDown.**packages**(obj, **kwargs)

Return the non-module packages in *obj*.
Optional keyword arguments are used to define a filter (see
ApiDown.make_filter()).

<a name="ApiDown.render" href="#ApiDown.render">#</a> ApiDown.**render**(template, *args, **kwargs)

Render *template* and return the resulting string.

<a name="ApiDown.signature" href="#ApiDown.signature">#</a> ApiDown.**signature**(obj)

Return the Signature object for callable *obj*. This an instance
of Python's `inspect.Signature` class.


#### Functions {#apidown-functions}

<a name="is_method_or_function" href="#is_method_or_function">#</a> **is_method_or_function**(obj)

Return `True` if *obj* is either a bound method or a function.

<a name="main" href="#main">#</a> **main**(args)



<a name="preprocess_mako" href="#preprocess_mako">#</a> **preprocess_mako**(text)

Mako template rendering treats line-initial /##+/ as comments that
get ignored, but these are important for Markdown. Replace them with
a substitution ${ s } where s is the hash sequence.

<a name="process" href="#process">#</a> **process**(f)

Print the rendered result of file *f*, which is a Markdown template.


