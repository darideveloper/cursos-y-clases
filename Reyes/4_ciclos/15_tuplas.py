# Crear tuplas
nombres = ("Juan", "Pedro", "Maria", "Luisa")

# Consultar elementos de una tupla
print(nombres[0])
print()

# Atualizar elementos, agregar elementos, eliminar
# elementos: NO SE PUEDE HACER

# nombres.append ("Gilberto") # error
# nombres[0] = "Roberto" # error

# Slice
sub_nombres = nombres[1:3]
print(sub_nombres)
print()

# Recorrer tuplas
for nombre in nombres:
    print(nombre)
