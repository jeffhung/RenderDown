### ${ a_.name(obj) }

${ a_.docstring(obj) }

#### Classes {#${ a_.name(obj) + '-classes' | u }}
% for c in a_.classes(obj):
${ a_.render("class.md", obj=c) }
% endfor

#### Functions {#${ a_.name(obj) + '-functions' | u }}
% for f in a_.functions(obj):
${ a_.render("function.md", obj=f) }
% endfor
