"""
1. Store a person’s name, and include some whitespace (' ', "\n", "\t") characters at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once.
2. Print the name once, so the whitespace around the name is displayed.
3. Then print the name using each of the three stripping functions, lstrip(),
4. rstrip(), 
5. and strip().
"""

nombre = "\n  Francisco \t  "
print ("--" + nombre + "--")
print ("--" + nombre.rstrip() + "--")
print ("--" + nombre.lstrip() + "--")
print ("--" + nombre.strip() + "--")

