# Definir una tupla
usuarios = ('usuario1', 'admin', 'editor', 'visitante', 'usuario2')
#               0         1        2          3          4
# Consultar elementos
print (usuarios[2]) # editor

# Preguntar numero de elementos
print ()
print (len(usuarios))

# Indice fuera de rango
# print (usuarios[99]) # error

# Modificar una tupla
# usuarios[-2] = "Francisco" # error

# Sobreescribir la variable
usuarios = ('editor', 'admin')
print ()
print (usuarios)

# Ordenar de forma permentente alfabeticamente A-Z
# usuarios.sort () # Error

# Ordenar de forma temporalmente alfabeticamente A-Z
usuarios_ordenados = sorted(usuarios)
print(usuarios_ordenados)