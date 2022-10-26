# Arreglo, Array, Listas

ventas = [ 10000, 200, 300, 500, 660 ]
#           0    1    2    3    4
#           -5  -4   -3   -2    -1

# Acceder a elementos de una lista
primera_venta = ventas[0] # acceder al primer elemento
comision_venta = 0.1

# Utilizar elemento de una lista
comision = primera_venta*comision_venta
print (comision)

# Acceder al último elemento de una lista
ultima_venta = ventas[-2]
print (ultima_venta)

# Actualizar los elementos de una lista
ventas[0] = 1000
print (ventas)

# Añadir elemento al final de una lista
ventas.append (25)
ventas.append (35)

# Añadir elemento en cualquier parte de una lista
ventas.insert (2, 666)
ventas.insert (4, "hola")
print (ventas)

# Borrar elemento de una lista por index
del ventas[0]
print (ventas)

# Borrar elemento por valor
ventas.remove (500)
print (ventas)

ventas.remove ("hola")
print (ventas)

# Eliminar y utilizar elemento
tareas_pendientes = ["limpiar", "cocinar", "estudiar", "mandar correo"]
tareas_concluidas = []

tarea_actual = tareas_pendientes.pop () # cortar el ultimo elemento de la lista
print (f"Estoy realizando la tarea: {tarea_actual}")

tareas_concluidas.append (tarea_actual) # pegar copia del elemento en la lista

print (tareas_pendientes)
print (tareas_concluidas)