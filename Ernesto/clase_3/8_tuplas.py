# Crear tuplas
usuarios = ("Maria", "Pedro", "José")

# Añadir elementos a una typla
usuarios.append ("Alberto") # Error

# Modificar elementos de una tupla
usuarios[0] = "Juan" # Error
usuarios.insert (2, 666) # Error 

# Operaciones de consulta
print (usuarios[0])
print (len(usuarios))

# Convertir tupla a lista
usuarios_2 = list(usuarios)
usuarios_2.append ("Alberto")

# Convertir una lista a tupla
usuarios = ["Maria", "Pedro", "José"]
usuarios_tupla = tuple(usuarios)
usuarios_tupla.append ("hola") # error

# Ciclos en tuplas
usuarios = ("Maria", "Pedro", "José")
for usuario in usuarios:
    print (usuario)

# Tipo de datos
print (type("hola mundo")) # Devolver el tipo de datos de una variable