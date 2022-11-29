# Lista inicial
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]

# Modificar elemento de lista
alumnos[-2] = "Francisco"
print (alumnos) # ['Juan', 'Maria', 'Pedro', 'Ana', 'Francisco', 'Alberto']

# Añadir elementos a una lista
print ()
alumnos.append ('Dari') # ['Juan', 'Maria', 'Pedro', 'Ana', 'Francisco', 'Alberto', 'Dari']
print (alumnos)

# Insertar elementos en una lista
print ()
alumnos.insert (-3, 'Gilberto') # ['Juan', 'Maria', 'Pedro', 'Ana', 'Gilberto', 'Francisco', 'Alberto', 'Dari']
print (alumnos)

# Eliminar por indice
print ()
del alumnos[0] # ['Maria', 'Pedro', 'Ana', 'Gilberto', 'Francisco', 'Alberto', 'Dari']
print (alumnos)

# Eliminar por valor
print ()
alumnos.remove ('Ana') # ['Maria', 'Pedro', 'Gilberto', 'Francisco', 'Alberto', 'Dari']
print (alumnos) 

# Nueva lista
peliculas_pendientes = ['El rey leon', 'Montecarlo', 'Wally']

# Cortar (copiar un elemento y eliminarlo de la lista original).
# Mover un elemento fuera de la lista
print ()
ultima_pelicula = peliculas_pendientes.pop () # ['El rey leon', 'Montecarlo']
print (f"Acabo de ver la película '{ultima_pelicula}'")
print (peliculas_pendientes)