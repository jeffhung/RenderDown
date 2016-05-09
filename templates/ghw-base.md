<%def name="a(data)">\
<% name = doc.anchor(name=data['qualname'], page=data['module']) %>\
<a name="${name.rpartition('#')[2]}" href="${name}">`#`</a>\
</%def>

<%def name="signature(data)">\
% if data.get('signature'):
(_${', '.join(data.get('signature', []))}_)\
% else:
()\
% endif
</%def>

<%def name="breadcrumb(parts, module=None)">\
<%
parts = [(p, None) for p in parts]
if module:
    modparts = module.split('.')
    for i in range(len(modparts)):
        parts.append((modparts[i], '.'.join(modparts[:i+1])))
crumbs = []
for p, a in parts[:-1]:
    if a is None:
        crumbs.append('[[{}]]'.format(p))
    else:
        crumbs.append('[{}]({})'.format(p, a))
crumbs.append('**{}**'.format(parts[-1][0]))
%>\
> ${' \u25b8 '.join(crumbs) }\
</%def>