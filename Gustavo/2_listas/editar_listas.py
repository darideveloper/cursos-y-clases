estudiantes = ["juan", "alberto", "miguel", "maria"]

# Actualizar
estudiantes[0] = "gilberto"

# Añadir nuevos valores
estudiantes.append ("Filemon")
print (estudiantes)

# Borrar un elemento por posición
del estudiantes[-2]
print (estudiantes)

# Borrar un elemento por valor
estudiantes.remove ("miguel")
print (estudiantes)

# Insetar elementos
estudiantes.insert (2, "dari")
print (estudiantes)

# Cortar
# ultimo_estudiante = estudiantes[-1]
# print (f"Hola, {ultimo_estudiante}")
# del estudiantes[-1]
# print (estudiantes)
ultimo_estudiante = estudiantes.pop (-1)
print (f"Hola, {ultimo_estudiante}")
print (estudiantes)
print ()

# Consultar tamaño de listas
print(len (estudiantes))