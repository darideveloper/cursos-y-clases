estudiantes = ["juan", "alberto", "miguel", "maria", "gilberto", "joel", "alondra", "fernando"]
#                 0        1         2          3        4         5        6          7
#                                                                 -3       -2           -1

# Indicando el principio y el final
print (estudiantes[1:6]) # ['alberto', 'miguel', 'maria', 'gilberto', 'joel']
print (estudiantes[0:6]) # ['juan', 'alberto', 'miguel', 'maria', 'gilberto', 'joel']
print (estudiantes[2:-1]) # ['miguel', 'maria', 'gilberto', 'joel', 'alondra']
print (estudiantes[2:len(estudiantes)]) # ['miguel', 'maria', 'gilberto', 'joel', 'alondra', 'fernando']

# Indicando el final
print (estudiantes[:6]) # ['juan', 'alberto', 'miguel', 'maria', 'gilberto', 'joel']

# Indicando el principio
print (estudiantes[2:]) # ['miguel', 'maria', 'gilberto', 'joel', 'alondra', 'fernando']

print (estudiantes[:]) # ['juan', 'alberto', 'miguel', 'maria', 'gilberto', 'joel', 'alondra', 'fernando']
print ()

# Copiar listas
estudiantes = ["juan", "alberto", "miguel", "maria", "gilberto", "joel", "alondra", "fernando"]
estudiantes_prueba = estudiantes[:] # hacer un slice que incluya todos los elementos (una copia)
estudiantes_prueba.append ("juan")
estudiantes_prueba.append ("dari")
estudiantes_prueba.append ("miguel")
print ("estudiantes: " + str(estudiantes))
print ("estudiantes prueba: " + str(estudiantes_prueba))