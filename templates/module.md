### ${ a_.name(obj) }

${ a_.docstring(obj) }

#### Classes

% for c in a_.classes(obj):
${ a_.render("class.md", obj=c) }

% endfor

#### Functions

% for f in a_.functions(obj):
${ a_.render("function.md", obj=f) }

% endfor
