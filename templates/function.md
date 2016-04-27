<%
sig = a_.signature(obj)
id_ = a_.name(obj)
%>\
**${ a_.name(obj) }**${str(sig)}
<a name="${id_ | u}" href="#${id_ | u}">#</a>

${ a_.docstring(obj) }