<%page args="name, index" />\
<%namespace file="ghw-base.md" import="*" />\
<%
data = index[name]
if data['__done__']:
    return STOP_RENDERING
index[name]['__done__'] = True

mod, _, method = name.rpartition('.')
%>\
${ a(data) }
${ '%s.**%s**' % (mod, method) }${ signature(data) }
% if data.get('docstring'):

${ data['docstring'] }
% endif