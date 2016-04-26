# ${ a_.name(obj) }

${ a_.docstring(obj) }

## Packages and Modules
% for m in sorted(a_.packages(obj) + a_.modules(obj), key=a_.name):
${ a_.name(m) }
% endfor

## Classes {#${ a_.name(obj) + '-classes' | u }}
% for c in a_.classes(obj):
${ a_.render("class.md", obj=c) }
% endfor

## Functions {#${ a_.name(obj) + '-functions' | u }}
% for f in a_.functions(obj):
${ a_.render("function.md", obj=f) }
% endfor
