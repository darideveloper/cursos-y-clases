clientes = ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
print (clientes)
print ()

# Ordenar listas de forma PERMANENTE (A-Z)
clientes = ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
clientes.sort ()
print (clientes) # ['Alberto', 'Juan', 'Maria', 'dari', 'feRnaNdO']
print ()

# Ordenar listas de forma PERMANENTE INVERSA (Z-A)
clientes = ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
clientes.sort (reverse=True) 
print (clientes) # ['feRnaNdO', 'dari', 'Maria', 'Juan', 'Alberto']
print ()

# Ordenar listas de forma TEMPORAL (A-Z)
clientes = ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
clientes_sort = sorted (clientes)
print (clientes) # ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
print (clientes_sort) # ['Alberto', 'Juan', 'Maria', 'dari', 'feRnaNdO']
print ()

# Ordenar listas de forma TEMPORAL INVERSA (Z-A)
clientes = ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
clientes_sort = sorted (clientes, reverse=True)
print (clientes) # ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
print (clientes_sort) # ['feRnaNdO', 'dari', 'Maria', 'Juan', 'Alberto']
print ()

# Invertir el orden de una lista PERMANENTE
tareas = ["Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video"]
print (tareas) # ["Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video"]
tareas.reverse ()
print (tareas) # ['editar video', 'dar clase', 'proyecto', 'estudiar', 'Lavar los platos']
tareas.reverse () # regresar lista al orden original
print (tareas) # ["Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video"]
print ()

# Preguntar por el tamaño de una lista
tareas = ["Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video", "Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video", "Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video", "Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video", "Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video"]
print (len (tareas))
print ()

tareas = ["Lavar los platos", "estudiar", "proyecto", "dar clase", "editar video"]
num_tareas = len(tareas)
print (f"Tengo {num_tareas} pendientes")