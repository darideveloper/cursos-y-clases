# Lista original
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]

# Copiar lista
alumnos_copia = alumnos[:]

# Hacer cambios en copia
alumnos_copia.append ("Francisco")
alumnos_copia.remove ("Ana")
del alumnos_copia[0]

print (alumnos)
print (alumnos_copia)
