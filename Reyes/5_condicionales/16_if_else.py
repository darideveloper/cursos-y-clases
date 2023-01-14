edad = 30

# If con una pregunta (condición, condición lógica)
if edad >= 18:
    # Linea que se va a ajecutar cuando la condición se cumple
    print ("Eres mayor, puedes entrar")
else:
    # Linea que se va a ejecutar cuando la condición NO se cumple
    print ("Eres menor, no puedes entrar")

print ("---------------------")

# Notas de los estudiantes
notes = [10, 8, 7, 6, 8, 3, 4, 5, 8, 9, 2]

# contador de estudiantes
estuidiante_num = 1

# Recorrer las notas
for note in notes:
    
    # Verificar si el estudiante esta aprobado o reprobado
    estatus = ""
    if note >= 6:
        estatus = "Aprobado"
    else:
        estatus = "Reprobado"
    
    # Imprimir mensaje con información del estudiante
    print (f"El estudiante {estuidiante_num}, obtuvo un {note}: {estatus}")
    
    # aumentar el contador
    estuidiante_num += 1