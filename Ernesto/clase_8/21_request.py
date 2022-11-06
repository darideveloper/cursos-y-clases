import requests

# PARTE 1: HABILIDADES DE POKEMON

# Lista de pokemones
pokemones = ["ditto", "pikachu", "charmander", "bulbasaur", "squirtle"]

# Recorrer cada pokemon
for pokemon in pokemones:

    # Obtener enlace para extraer la información
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    
    # Solicitard atos y convertirlos a json
    res = requests.get (url)
    json_data = res.json()
    
    # Obtener y mostrar la primer habilidad de cada pokemon
    habilidad = json_data["abilities"][1]["ability"]["name"]

    print (f"{pokemon}: {habilidad}")

# PARTE 2: POKEMONS DE UN COLOR

# Obtener la lista de pokemons de un color en específico
color = "green"
url = f"https://pokeapi.co/api/v2/pokemon-color/{color}/"
res = requests.get (url)
json_data = res.json()
pokemones = json_data["pokemon_species"]

# Recorrer cada pokemon de la lista
for pokemon in pokemones:
    
    # Obtener nombre y url del pokemon
    pokemon_nombre = pokemon["name"]
    pokemon_url = pokemon["url"]
    
    # Solicitar informaicón detallada del pokemon
    pokemon_res = requests.get (pokemon_url)
    pokemon_json_data = pokemon_res.json()
    habitad_dic = pokemon_json_data["habitat"]
    
    # Obtener el habitad o asignar un valor predeterminado si no existe
    if habitad_dic != None:
        habitad = habitad_dic["name"]
    else:
        habitad = "No tiene habitat"
        
    # Mostrar información del habitad
    print (f"{pokemon_nombre}: {habitad}")
    
    
    