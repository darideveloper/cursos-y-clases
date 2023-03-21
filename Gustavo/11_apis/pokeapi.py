import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

# Obtener datos de la api
res = requests.get(url)
res.raise_for_status()

# Convertir datos a diccionario
data = json.loads(res.text)

# Extraer dato en especifico
ability_name = data["abilities"][0]["ability"]["name"]
print (ability_name)
print(data["moves"][0]["move"]["name"])


url_specie = data["species"]["url"]
res = requests.get(url_specie)
res.raise_for_status()

# Convertir datos a diccionario
data = json.loads(res.text)

print (data)
