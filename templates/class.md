<% name = a_.name(obj) %>
<a name="${name | u}" href="#${name | u}">#</a> **${name}**

${ a_.docstring(obj) }

% for f in a_.methods(obj):
${ a_.render("method.md", obj=f, cls=obj) }
% endfor