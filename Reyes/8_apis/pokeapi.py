import json
import requests

# Lista de pokemones a consultar
pokemones = ["pikachu", "charmander", "bulbasaur", "squirtle", "ditto"]

# Recorrer lista de pokemones
for pokemon in pokemones:
    
    print (f"\nPokemon: {pokemon.upper()}")
    
    # Obtener datos del pokemon
    page = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" # URL dinamica de la api
    res = requests.get (page)
    res.raise_for_status () # Si no hay error, detener el programa
    pokemon_data = json.loads (res.text) # Convierte el texto en un diccionario

    # Consultar datos del pokemon
    altura_pokemon = pokemon_data["height"]
    print (f"\tAltura: {altura_pokemon}")

    habilidad_1 = pokemon_data["abilities"][0]["ability"]["name"]
    print (f"\tHabilidad: {habilidad_1}")

    movimiento_1 = pokemon_data["moves"][0]["move"]["name"]
    print (f"\tAtaque: {movimiento_1}")

    sprite = pokemon_data["sprites"]["front_default"]
    print (f"\tImagen: {sprite}")

# Final del programa
print ("Terminado")