# Ordernar lista de manera permnente y de A - Z
tareas_pendientes = [4,56,3,2,365,6,2,6,2,34,4,68,4356]
tareas_pendientes.sort ()
print (tareas_pendientes)

# Ordernar lista de manera permnente y Z - A
tareas_pendientes = [4,56,3,2,365,6,2,6,2,34,4,68,4356]
tareas_pendientes.sort (reverse=True)
print (tareas_pendientes)

# Lista en reversa
tareas_pendientes = [4,56,3,2,365,6,2,6,2,34,4,68,4356]
tareas_pendientes.reverse ()
print (tareas_pendientes)

# Ordenar temporalmente de la A - Z
tareas_pendientes = ["limpiar", "cocinar", "estudiar", "mandar correo"]
print (sorted (tareas_pendientes))
print (tareas_pendientes)

# Ordenar temporalmente de la Z - A
tareas_pendientes = ["limpiar", "cocinar", "estudiar", "mandar correo"]
print (sorted (tareas_pendientes, reverse=True))
print (tareas_pendientes)

# Contar elementos dentro de una lista
tareas_pendientes = ["limpiar", "cocinar", "estudiar", "mandar correo", "enviar proyecto"]
print(len(tareas_pendientes))

# Error al consultar elementos de una lista
tareas_pendientes = ["limpiar", "cocinar", "estudiar", "mandar correo", "enviar proyecto"]
print (tareas_pendientes[20])