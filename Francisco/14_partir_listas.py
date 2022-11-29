alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]

# Slicing/cortando una lista
alumnos_favoritos = alumnos[0:3]
for alumno in alumnos_favoritos:
    print (alumno)
    
print ()
alumnos_favoritos = alumnos[1:-2]
for alumno in alumnos_favoritos:
    print (alumno)
    
# Omitir el cero
print ()
alumnos_favoritos = alumnos[:3]
for alumno in alumnos_favoritos:
    print (alumno)
    
# Omirir el último elemento
print ()
alumnos_favoritos = alumnos[4:]
for alumno in alumnos_favoritos:
    print (alumno)
