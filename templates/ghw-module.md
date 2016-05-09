<%page args="name, index" />\
<%namespace file="ghw-base.md" import="*" />\
<%
data = index[name]
if data['__done__']:
    return STOP_RENDERING
index[name]['__done__'] = True

package, delim, module = data['fullname'].rpartition('.')
package += delim  # add . if there was one

docstring = data['docstring']

%>\
${ breadcrumb(['Home', 'API Reference'], module=name) }
% if docstring:

${ docstring }

% endif
% if data.get('modules'):
% with doc.section():
${ doc.header("Modules") }

% for mdata in map(index.__getitem__, data['modules']):
* [${ mdata['fullname'] }](${ doc.anchor(name=mdata['qualname'], page=mdata['module']) })
% endfor
% endwith

% endif

<% localdefs = data.get('classes', []) + data.get('functions', []) %>\
% if localdefs:
% with doc.section():
${ doc.header('Classes and Functions') }

% for objdata in map(index.__getitem__, localdefs):
${ doc.render('ghw-{}.md'.format(objdata['type']), name=objdata['fullname'], index=index) }
% endfor
% endwith
% endif