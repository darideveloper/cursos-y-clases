alumnos = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Alberto"]

# Recorrer cada alumno de mi lista
for alumno in alumnos:
    
    # Preguntar si el alumno actual se llama Maria
    if alumno == "Maria": # Igual a
        # Decirle a maria que está reprobada
        print (f"{alumno} estas reprobado")
    # Si es cualquier otro alumno...
    else:
        print (f"{alumno} pasaste")
        