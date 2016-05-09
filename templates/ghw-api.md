<%page args="index" />
<%
import json
index = json.load(open(index))
for name, data in index.items():
    data['__done__'] = False
%>\
<%namespace file="ghw-base.md" import="*" />\
${ breadcrumb(['Home', 'API Reference']) }

# Index

% for fullname, data in sorted(index.items()):
% if data['type'] in ('module', 'class', 'function'):
* [${ fullname | md }](${ doc.anchor(name=data['qualname'], page=data['module']) })
% endif
% if data['type'] == 'module':
${ doc.render('ghw-module.md', name=fullname, index=index, page=fullname) }\
% endif
% endfor