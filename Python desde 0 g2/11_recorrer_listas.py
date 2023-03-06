tareas = ["Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video", "estudiar"]
#               0                 1            2             3           4              5

# Recorrer elementos de una lista
for tarea in tareas: # "por cada tarea de mi lista de tareas, hazme lo siguiente:"
    print (tarea) # código a ejecutar por cada elemernto de mi lista
print ("\tFor terminado") # código a ejecutar después del for
print ()
    
# Hacer mas cosas dentro de un ciclo for
for tarea in tareas:
    print (f"Tengo la tarea pendiente: {tarea.upper()}") 
    print ("Pero me da flojera hacerla\n")
    
print ("\tFor terminado")
print ()

# Recorrer lista con contador
contador = 0
for tarea in tareas:
    # print (f"Contador: {contador}")
    
    # Utilizar contador
    print (f"{contador + 1}: {tarea}")
    
    # Incrementar contador
    # contador = contador + 1
    contador += 1
    
print ("\tFor terminado")
print ()

# Recorrer lista con index (solo utilizar en listas sin elementos repetidos)
for tarea in tareas:
    
    # Obtener la posición de un elemento
    index = tareas.index (tarea)
    
    # Utilizar index
    print (f"{index + 1}: {tarea}")
    
print ("\tFor terminado")
print ()