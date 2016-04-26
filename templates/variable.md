<%
id_ = '{}.{}'.format(a_.name(ctx), a_.name(obj))
%>
<a name="${id_ | u}" href="#${id_ | u}">#</a>${ a_.name(ctx) }.**${ a_.name(obj) }**}
