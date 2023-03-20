# Crear una tupla
estudiantes = ("maria", "pedro", "josé", "issac", "heber", "Xavier")

print (estudiantes[0:2])

for estudiante in estudiantes:
    print (estudiante)
print ()

# Consultar datos
print (estudiantes[-1] + " me cae bien") 

# # Actualizar datos # TypeError: 'tuple' object does not support item assignment
# estudiantes[2] = "Francisco"
# print (estudiantes)

# Consultar lontitud
print (len(estudiantes)) # 5

# Añadir elementos# AttributeError: 'tuple' object has no attribute 'append'
# estudiantes.append ("Ocegueda") 

print (sorted(estudiantes, reverse=True))

# letras = ["a", "b", "c"]
# print (letras.reverse())