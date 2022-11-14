import requests

# Solicitar datos de la API
res = requests.get ("https://pokeapi.co/api/v2/pokemon/charizard")
res.raise_for_status()

# Extraer el json de la api
data = res.json()
movimientos = data["moves"]

# Mopstrar los movimientos del pokemon
print ("Los movimientos de harizard son:")

title_name = "Nombre".center (20)
title_power = "Poder".center (10)
title_type = "Tipo".center (15)
print (f"\n{title_name} {title_power} {title_type}\n")

for movimiento in movimientos:
    move_name = movimiento["move"]["name"]
    move_url = movimiento["move"]["url"]
    
    # Solicitar datos de la API
    res_move = requests.get (move_url)
    res_move.raise_for_status()
    data_move = res_move.json()
    
    move_power = data_move["power"]
    move_type = data_move["type"]["name"]
    
    # Fix power
    if move_power == None:
        move_power = 0
    
    # Format texts
    move_name_formatted = move_name.center(20)
    move_power_formated = str(move_power).center(10)
    move_type_formated = move_type.center(15)
    
    print (f"{move_name_formatted} {move_power_formated} {move_type_formated}")
    
    
