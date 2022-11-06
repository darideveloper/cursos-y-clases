import requests

pokemones = ["pikachu", "ditto", "charizard", "ninetales", "squirtle", "rayquaza"]

for pokemon in pokemones:
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/"
    
    # Solicitar datos de la API
    res = requests.get (url)
    res.raise_for_status()

    # Extraer el json de la api
    data = res.json()
    
    # Obtener datos
    shape = data["shape"]["name"]
    habitat = data["habitat"]["name"]
    
    
    print (f"{pokemon}, {shape}, {habitat}")