# We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.

import random

# data
pets_types = ["dog", "cat", "bird", "fish"]
names = ["elias", "dari", "roberto", "josué"]

# creando una lista vacia para guardar mascotas.
pets = []

# creando 30 mascotas
for pet_number in range(30):
    
    # get random pet type
    pet_type = random.choice(pets_types)
    
    # get random name
    name = random.choice(names)
    
    # Guardar la mascota en la lista
    new_pet = {'type': pet_type, 'owner': name}
    pets.append (new_pet)
    
# recorriendo la lista con las 30 mascotas    
for pet in pets:
    print (pet) 
            
# mostrando las mascotas creadas.    
print (len(pets))    