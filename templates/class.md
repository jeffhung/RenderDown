<% name = a_.name(obj) %>\
**${name}**
<a name="${name | u}" href="#${name | u}">#</a>

${ a_.docstring(obj) }

% for f in a_.methods(obj):
${ a_.listitem(a_.render("method.md", obj=f, cls=obj)) }

% endfor