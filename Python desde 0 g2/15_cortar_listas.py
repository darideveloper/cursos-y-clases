estudiantes = [
    "maria", 
    "pedro", 
    "josé", 
    "issac", 
    "heber", 
    "leydi", 
    "vladimir", 
    "adriana"
]

# Partir una lista indicando el principio y el final
estudiantes_test = estudiantes[1:5]
print (estudiantes_test) # ['pedro', 'josé', 'issac', 'heber']

# Partir una lista desde 0 hasta un determinado elemento
estudiantes_test = estudiantes[0:5] # ['maria', 'pedro', 'josé', 'issac', 'heber']
print (estudiantes_test)
estudiantes_test = estudiantes[:5] # ['maria', 'pedro', 'josé', 'issac', 'heber']
print (estudiantes_test)

# Partir una lista desde un determinado elemento hasta el último
estudiantes_test = estudiantes[5:len(estudiantes)]
print (estudiantes_test) # ['leydi', 'vladimir', 'adriana']
estudiantes_test = estudiantes[5:]
print (estudiantes_test) # ['leydi', 'vladimir', 'adriana']

# Indices negativos
estudiantes_test = estudiantes[-5:-1]
print (estudiantes_test) # ['issac', 'heber', 'leydi', 'vladimir']

# TODO: DE TAREA SOLUCIONAR ESTO: COPIAR UNA LISTA SIN MODIFICAR LA ORIGINAL
estudiantes = [
    "maria", 
    "pedro", 
    "josé", 
    "issac", 
    "heber", 
    "leydi", 
    "vladimir", 
    "adriana"
]

estudiantes_copia = estudiantes
estudiantes_copia.append ("Dari")

print (estudiantes)
print (estudiantes_copia)
