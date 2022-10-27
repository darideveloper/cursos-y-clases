import time
from tracemalloc import StatisticDiff

# Cortas listas / slice
correos = [
    "maria1@gmail.com", 
    "pedro1@gmail.com", 
    "josé1@gmail.com", 
    "maria2@gmail.com", 
    "pedro2@gmail.com", 
    "josé2@gmail.com"
]
print(correos[0:3])  # Desde el 0 al 3
print(correos[:3])  # desde el incio al 3
print(correos[3:])  # desde el 3 hasta el final
print(correos[:-2])  # desde el primero hasta el penultimo

# Ciclos con slices
correos = [
    "maria1@gmail.com",
    "pedro1@gmail.com",
    "josé1@gmail.com",
    "maria2@gmail.com",
    "pedro2@gmail.com",
    "josé2@gmail.com"
]

for correo in correos[0:2]:
    print(f"Enviando correo a: {correo}...")

    # Añadir tiempo de despera después de cada mensaje
    time.sleep(4)

# Copiar listas
usuarios1 = ["Maria", "Pedro", "José"]
usuarios2 = usuarios1[:]  # Copiar de la lista
usuarios2.append("Alberto")

print(usuarios1)
print(usuarios2)
