animales = [
    {
        'animal':'perro', 
        'tamaño': 'XL', 
        'color':'negro'
    },
    {
        'animal':'gato', 
        'tamaño': 'M', 
        'color':'naranja'
    }, 
    {
        'animal':'conejo', 
        'tamaño': 'S', 
        'color':'blanco'
    }
]

# OPCIÓN A

# # Obtener lista de colores
# colores = []
# for animal in animales:    
#     color = animal["color"]
#     colores.append (color)
    

# # Ordenar los colores
# colores = sorted(colores)

# # recorrer lista de colores ya ordenada
# animales_ordenados = []
# for color in colores:
        
#     # Recorrer lista de animales, para encontrar el del color correcto
#     for animal in animales:
                
#         # Obtener color del animal actual
#         color_animal = animal["color"]
        
#         # validar el el animal tiene el color corerecto
#         if color_animal == color:
            
#             # Guadar información del animal encontrado
#             animales_ordenados.append (animal)
            
#             # Dejar de buscar en esa vuelta
#             break
        
# print (f"El diccionario original es: {animales}")
# print (f"El diccionario ordenado por color de la mascota es: {animales_ordenados}")
        
# OPCIÓN B

# Obtener lista de colores
colores = list(map(lambda aniamal:aniamal["color"], animales))

# Ordenar los colores
colores = sorted(colores)

# MNostrar valores originales de la lista
print (f"El diccionario original es: {animales}")

# Genrar el nuevo diccionario ordenado
animales.sort(key=lambda animal: colores.index(animal['color']))

# Mostrar valores ordenados
print (f"El diccionario ordenado por color de la mascota es: {animales}")