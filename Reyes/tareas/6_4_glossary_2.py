# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

python_glossary = {
    'listas': 'secuencias ordenadas que guardan una variedad de tipos de objetos',
    'tuplas': 'son similares a las listas, sin embargo, tienen una diferencia: son inmutables',
    'diccionarios': 'mapeos desordenados para guardar objetos',
    'ciclos for': 'ejecutar un bloque de codigo en cada iteracion',
    'declaraciones if, elif': 'usamos las declaraciones para controlar el flujo de nuestra aplicacion',
}
for word, summary in python_glossary.items():
    print (f'\nWord: {word.title()}')
    print (f'Summary: {summary}')
    
python_glossary['Django'] = 'framework muy popular de python para el backend'
python_glossary['indentacion'] = 'espacios en blanco, sangria, muy importante y es lo que separa a python del resto de lenguajes'
python_glossary['valores booleanos'] = 'permiten declarar verdadero o falso, importantes para la logica de programacion'
python_glossary['cadenas'] = 'secuencia de caracteres entre comillas'
python_glossary['listas de comprension'] = 'manera unica de crear una lista de python rapidamente'

for word, summary in python_glossary.items():
    print (f'\nWord: {word.title()}')
    print (f'Summary: {summary}')
    