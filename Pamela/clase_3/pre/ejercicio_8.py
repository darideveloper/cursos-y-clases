mascotas = [
    {
        'animal': 'perro', 
        'tamaño': 'XL', 
        'color': 'negro'
    },
    {
        'animal': 'gato', 
        'tamaño': 'M', 
        'color': 'naranja'
    },
    {
        'animal': 'conejo', 
        'tamaño': 'S', 
        'color': 'blanco'
    }
]



# Mostrar diccionario original
print (f"El diccioarnio original es: {mascotas}")

# OPCIÓN A

# Obetener y ordenar lista de colores, manualmente
colores = []
for mascota in mascotas:
    color = mascota['color']
    colores.append (color)
colores = sorted(colores)

# Opción A: Ordenar diccionario mmanualmente
nuevas_mascotas = []
for color in colores:
    for mascota in mascotas:
        if color == mascota['color']:
            nuevas_mascotas.append (mascota)
            break
print (f"El diccioarnio original es: {nuevas_mascotas}")


# OPCIÓN B

# Obetener y ordenar lista de colores, con map y lambda
colores = list(map(lambda mascota: mascota['color'], mascotas))
colores = sorted(colores)

# Ordenar diccionario con funcion lambda
mascotas.sort(key=lambda mascota:colores.index(mascota['color']))
print (f"El diccioarnio original es: {mascotas}")

