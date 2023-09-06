# Ordenar a la A-Z permanente
estudiantes = ["juan", "alberto", "miguel", "maria"]
estudiantes.sort ()
print (estudiantes) # ['alberto', 'juan', 'maria', 'miguel']
print ()

# Ordenar a la A-Z temporzal
estudiantes = ["juan", "alberto", "miguel", "maria"]
estudiantes_ordenados = sorted(estudiantes)
print (estudiantes) # ["juan", "alberto", "miguel", "maria"]
print (estudiantes_ordenados) # ['alberto', 'juan', 'maria', 'miguel']
print ()

# Ordenar a la Z-A permanente
estudiantes = ["juan", "alberto", "miguel", "maria"]
estudiantes.sort (reverse=True)
print (estudiantes) # ['miguel', 'maria', 'juan', 'alberto']
print ()

# Ordenar a la Z-A temporzal
estudiantes = ["juan", "alberto", "miguel", "maria"]
estudiantes_ordenados = sorted(estudiantes, reverse=True)
print (estudiantes) # ["juan", "alberto", "miguel", "maria"]
print (estudiantes_ordenados) # ['miguel', 'maria', 'juan', 'alberto']
print ()

# Invertir orden de lista permanente
estudiantes = ["juan", "alberto", "miguel", "maria"]
estudiantes.reverse()
print (estudiantes) # ['maria', 'miguel', 'alberto', 'juan']
estudiantes.reverse()
print (estudiantes) # ["juan", "alberto", "miguel", "maria"]
