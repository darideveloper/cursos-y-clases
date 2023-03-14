#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers_locations = {
    'rio bravo': 'mexico',
    'rio amazonas': 'brasil',
    'rio misisipi': 'estados unidos',
}
#recorriendo los pares clave/valor y agregando una oracion
for river, location in rivers_locations.items():
    print (f'The {river.title()} runs through {location.title()}')
print ()

#recorriendo las llaves del diccionario    
for river in rivers_locations.keys():
    print (river.title())    
print ()

#recorriendo los valores del diccionario
for location in rivers_locations.values():
    print (location.title())