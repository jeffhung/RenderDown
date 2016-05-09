<%page args="name, index" />\
<%namespace file="ghw-base.md" import="*" />\
<%
data = index[name]
if data['__done__']:
    return STOP_RENDERING
index[name]['__done__'] = True

mod, _, cls = data['fullname'].rpartition('.')
%>\
${ a(data) }
${ mod }.**${cls}**${ signature(data) }
% if data.get('docstring'):

${ data['docstring'] }

% endif
% if data.get('methods'):

% for mdata in map(index.__getitem__, data['methods']):
${ doc.listitem(
    doc.render("ghw-method.md", name=mdata['fullname'], index=index)
)}
% endfor
% endif