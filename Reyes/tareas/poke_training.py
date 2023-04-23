import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/mewtwo"
res = requests.get (url)
res.raise_for_status ()
pokemon_data =json.loads (res.text)

moves = pokemon_data['moves']
for move in moves:
    version_groups_details = move['version_group_details']
    
    for version_group_details in version_groups_details:
        version_group = version_group_details['version_group']
        version_group_name = version_group["name"]
        print (version_group_name)
    
