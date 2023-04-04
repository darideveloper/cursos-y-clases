# INSTALL REQUESTS
# python -m pip install requests 

# python: vamos a utllizar algo de python
# -m pip: vamos a utilizar la herramienta pip de python (para borrar o añadir cosas)
# install: añadir algo a python
# requests: nombre de lo que vamos a añadir

# Decirole a python que vamos a utilizar requests
import requests

# Decirle a python que vamos a utilizar json
import json

# Traer datos de un enlace
page = f"https://pokeapi.co/api/v2/pokemon/pikachu"
res = requests.get (page)

# Convertir respuesta en formato json a un diccionario
data = json.loads (res.text)

# Consultar información dentro del diccionario
experiencia_base = data["base_experience"]
print (experiencia_base)

# Mostrar el atributo "is_hidden" de la segunda habilidad del pokemon
is_hidden = data["abilities"][1]["is_hidden"]
print (is_hidden)

# Mostrar el enlace del sprite correspondiente a el arte oficial

art = data['sprites']['other']['official-artwork']['front_default']
print (art)

# Obtener el url del movimiento "headbutt"
print (data['moves'][6]['move']['url'])


# Obtener la lista de todos los movimientos
moves = data['moves']

# Recorrer la lista de movimientos
search_move_url = ''
search_move = "seiskbjldaskjas"
for move in moves:
    

    # obtener los datos del movimiento actual
    name = move['move']['name']
    url = move['move']['url']

    # Comprobar si el movimiento se llama "headbutt", para guardar el url y terminar el ciclo
    if name == search_move:
        search_move_url = url
        break

# Mostrar un mensaje diferente dependiendo si se encontró o no el url

if search_move_url != "":
    print (f'La url del movimiento "{search_move}" es: {search_move_url}')
else:
    print (f'Movimiento "{search_move}" no encontrado')    
