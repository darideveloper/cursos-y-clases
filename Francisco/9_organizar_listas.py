
# Ordenar de forma alfabetica (permanente) A-Z
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]
alumnos.sort () # ['Alberto', 'Ana', 'Jose', 'Juan', 'Maria', 'Pedro']
print (alumnos)

# Ordenar de forma alfabetica inversa (permanente) Z-A
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]
print ()
alumnos.sort (reverse=True) # ['Alberto', 'Ana', 'Jose', 'Juan', 'Maria', 'Pedro']
print (alumnos)

# Ordenar de formas alfabetica (temporal) A-Z
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]
print ()
alumnos_ordenados = sorted (alumnos) # ['Alberto', 'Ana', 'Jose', 'Juan', 'Maria', 'Pedro']
print (alumnos_ordenados)
print (alumnos) # ['Juan', 'Maria', 'Pedro', 'Ana', 'Jose', 'Alberto']

# Ordenar de formas alfabetica (temporal) Z-A
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]
print ()
alumnos_ordenados = sorted (alumnos, reverse=True)
print (alumnos_ordenados) # ['Pedro', 'Maria', 'Juan', 'Jose', 'Ana', 'Alberto']
print (alumnos) # ['Juan', 'Maria', 'Pedro', 'Ana', 'Jose', 'Alberto']

# Invertir orden (permanente)
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]
print ()
alumnos.reverse () # ['Alberto', 'Jose', 'Ana', 'Pedro', 'Maria', 'Juan']
print (alumnos)
alumnos.reverse () # ['Juan', 'Maria', 'Pedro', 'Ana', 'Jose', 'Alberto']
print (alumnos)

