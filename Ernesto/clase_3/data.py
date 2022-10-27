# INGORA EL CONTENIDO DE ESTE ARCHIVO
import os
import json

# Paths
current_folder = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_folder, 'data.json')

# Read data from json
with open (json_path) as file:
    data = json.load(file)
    
# Map data for get titles and texts
posts_titles = tuple(map(lambda post: post["title"], data))
posts_bodies = tuple(map(lambda post: post["body"], data))

print ()