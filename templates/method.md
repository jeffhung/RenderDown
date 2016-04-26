<%
sig = a_.signature(obj)
id_ = '{}.{}'.format(a_.name(cls), a_.name(obj))
%>
<a name="${id_ | u}" href="#${id_ | u}">#</a> ${ a_.name(cls) }.**${ a_.name(obj) }**${str(sig)}

${ a_.docstring(obj) }