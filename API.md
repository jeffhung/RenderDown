
> [[Home]] ▸ **API Reference**

# Index

* [renderdown](#renderdown)
* [renderdown.DocManager](#renderdown-DocManager)
* [renderdown.RenderDownError](#renderdown-RenderDownError)
* [renderdown.github\_sanitize\_filename](#renderdown-github_sanitize_filename)
* [renderdown.github\_sanitize\_id](#renderdown-github_sanitize_id)
* [renderdown.main](#renderdown-main)
* [renderdown.md](#renderdown-md)
* [renderdown.preprocess\_mako](#renderdown-preprocess_mako)
* [renderdown.sanitize\_id](#renderdown-sanitize_id)



-----

# renderdown


> [[Home]] ▸ [[API Reference]] ▸ **renderdown**

Render Markdown from templates.


## Classes and Functions

<a name="renderdown-RenderDownError" href="#renderdown-RenderDownError">`#`</a>
renderdown.**RenderDownError**(_?_)

Error class for RenderDown-specific problems.


<a name="renderdown-DocManager" href="#renderdown-DocManager">`#`</a>
renderdown.**DocManager**(_top='Home', directories=None, multifile=True_)

This class encapsulates the document formatting and management
functions that are made available to all templates via the `doc`
variable.


* <a name="renderdown-DocManager-render" href="#renderdown-DocManager-render">`#`</a>
  DocManager.**render**(_filename, page=None, *args, **kwargs_)
  
  Render template given by *filename*.
  
  If *page* is None, the rendered string is returned, otherwise
  it is written to the buffer assigned to *page*.
  
* <a name="renderdown-DocManager-write" href="#renderdown-DocManager-write">`#`</a>
  DocManager.**write**(_text, page=None_)
  
  Write *text* to the buffer of *page*; if *page* is None, write
  to the current page.
  
* <a name="renderdown-DocManager-register_anchor" href="#renderdown-DocManager-register_anchor">`#`</a>
  DocManager.**register_anchor**(_name=None, page=None_)
  
  Find a unique, sanitized anchor for *name* using the name of *name*.
  If output is a single page, URIs are prepended with *page*.
  When *page* is `None`, the current page is used. The URI is
  registered to the id of *name* and then a tuple `(uri, page)`
  is returned. If the object has already been registered, the
  tuple for the original registration is returned and nothing
  else is done.
  
* <a name="renderdown-DocManager-anchor" href="#renderdown-DocManager-anchor">`#`</a>
  DocManager.**anchor**(_name=None, page=None_)
  
  Return the anchor for the given *name* and *page*.
  
* <a name="renderdown-DocManager-header" href="#renderdown-DocManager-header">`#`</a>
  DocManager.**header**(_text, level=None_)
  
  Return an ATX-style header at level *level* and header text
  *text*. If *level* is `None`, use the current level of page
  descent.
  
* <a name="renderdown-DocManager-section" href="#renderdown-DocManager-section">`#`</a>
  DocManager.**section**()
  
  A context manager that increases the nesting level.
  
* <a name="renderdown-DocManager-blockquote" href="#renderdown-DocManager-blockquote">`#`</a>
  DocManager.**blockquote**(_text_)
  
  Turn a block of text into a blockquote.
  
* <a name="renderdown-DocManager-indent" href="#renderdown-DocManager-indent">`#`</a>
  DocManager.**indent**(_text, columns=2_)
  
  Indent a block of text by *columns* spaces.
  
* <a name="renderdown-DocManager-listitem" href="#renderdown-DocManager-listitem">`#`</a>
  DocManager.**listitem**(_text, body=None, bullet='*'_)
  
  Turn a block of text into a list-item.
  

<a name="renderdown-md" href="#renderdown-md">`#`</a>
renderdown.**md**(_text_)

Basic filter for escaping text in Markdown.

<a name="renderdown-preprocess_mako" href="#renderdown-preprocess_mako">`#`</a>
renderdown.**preprocess_mako**(_text_)

Mako template rendering treats line-initial /##+/ as comments that
get ignored, but these are important for Markdown. Replace them with
a substitution ${ s } where s is the hash sequence.

<a name="renderdown-github_sanitize_id" href="#renderdown-github_sanitize_id">`#`</a>
renderdown.**github_sanitize_id**(_x_)

Sanitize an ID by near-GitHub standards (see toc_filter.rb in
https://github.com/jch/html-pipeline):
 * remove punctuation besides hyphens and underscores
 * change spaces to hyphens
 * downcase
Note that it doesn't:
 * add unique suffixes (-1, -2, etc.)

<a name="renderdown-github_sanitize_filename" href="#renderdown-github_sanitize_filename">`#`</a>
renderdown.**github_sanitize_filename**(_x_)

Sanitize a filename by GitHub wiki conventions (see
https://help.github.com/articles/adding-and-editing-wiki-pages-locally/#naming-wiki-files):

 * remove '\/:*?"<>|'
 * change spaces to hyphens

<a name="renderdown-sanitize_id" href="#renderdown-sanitize_id">`#`</a>
renderdown.**sanitize_id**(_x_)

Sanitize an ID similar to github_sanitize_id, but with the
following differences:
 * no downcasing
 * dots (.) are replaced with hyphens (which helps Python module
   namespaces look better)

<a name="renderdown-main" href="#renderdown-main">`#`</a>
renderdown.**main**(_args_)


