# Crear una lista
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]
            #0       1        2       3       4
          #-5       -4        -3       -2       -1
print (alumnos) # ["Juan", "Maria", "Pedro", "Ana", "Jose"]

# Acceder a elementos de la lista
print ()
print (alumnos[4].upper()) # JOSÉ

# Acceder al ultiumo elemento de la lista
print ()
print (alumnos[-1]) # Alberto

# Utiliza un valor de una lista
print ()
mensaje = f"Hola {alumnos[3]}!, cómo estás?" # Hola Ana!, cómo estás?
print (mensaje)

# Contar cuantos elementos hay en una lista
print ()
cantidad_alumnos = len (alumnos)
print (cantidad_alumnos)

# Concular elementos inexistentes
print ()
print (alumnos[100]) # IndexError: list index out of range



