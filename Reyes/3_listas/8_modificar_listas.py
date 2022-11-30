# Crear listas
autos = ['nissan', 'renault', 'vmw', 'honda', 'mercedes benz']
#           0          1         2      3            4
#          -5         -4        -3     -2           -1

# Modificar un valor
autos[0] = 'pointec'
print (autos)

# Añadir elemento (al final)
print ()
autos.append ('Dari')
print (autos)
# ['pointec', 'renault', 'vmw', 'honda', 'mercedes benz', 'Dari']
#    0          1        2       3            4            5

# Insertar elementos
print ()
autos.insert (1, 'GMC')
print (autos)
# ['pointec', 'GMC', 'renault', 'vmw', 'honda', 'mercedes benz', 'Dari']

# Borrar elementos por index
print ()
del autos[-1]
print (autos)
['pointec', 'GMC', 'renault', 'vmw', 'honda', 'mercedes benz']

# Borrar elementos por nombre
print ()
autos.remove ('vmw')
print (autos)
['pointec', 'GMC', 'renault', 'honda', 'mercedes benz']


# Lista de tareas
tareas_pendientes = ["Estudiar python", "Lavar los platos", "Tareas de matemáticas"]

# Cortar / mover un elemento afiera de una lista
print ()
ultima_tarea = tareas_pendientes.pop ()
print (f"Ya hice la tarea: {ultima_tarea.upper()}")
print (tareas_pendientes)


