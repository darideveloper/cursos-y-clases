# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.


# Este es un diccionario de python con algunas palabras clave.
python_glossary = {
    'listas': 'secuencias ordenadas que guardan una variedad de tipos de objetos',
    'tuplas': 'son similares a las listas, sin embargo, tienen una diferencia: son inmutables',
    'diccionarios': 'mapeos desordenados para guardar objetos',
    'ciclos for': 'ejecutar un bloque de codigo en cada iteracion',
    'declaraciones if, elif': 'usamos las declaraciones para controlar el flujo de nuestra aplicacion',
}
print (f'listas: {python_glossary["listas"]}\n')
print (f'tuplas: {python_glossary["tuplas"]}\n')
print (f'diccionarios: {python_glossary["diccionarios"]}\n')
print (f'ciclos FOR: {python_glossary["ciclos for"]}\n')
print (f'declacaciones IF, ELIF: {python_glossary["declaraciones if, elif"]}\n')
print ()

for palabra, descripcion in python_glossary.items():
    print (f"{palabra}: {descripcion}\n")