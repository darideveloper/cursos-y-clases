# Almacenar datos parecidos en diferentes variables: NO HACER
cliente_1 = "Juan"
cliente_2 = "Fernando"
cliente_3 = "Alberto"

# Esttucurada de datos: listas o arreglos
clientes = ["Juan", "Maria", "feRnaNdO", "Alberto", "dari"]
#              0       1         2            3       4
#             -5      -4        -3           -2      -1

# Consultar datos de listas
print (clientes[0] + " me cae bien") # Juan me cae bien
print (clientes[2].title())
print ()

# Consultar el último dato
print (clientes[-1].title())
print ()

# Actualizar datos de una lista
clientes[2] = "Francisco"
print (clientes)
print ()
# ['Juan', 'Maria', 'Francisco', 'Alberto', 'dari']

# Añadir elementos al final de una lista
clientes.append ("Ocegueda")
print (clientes)
print ()
# ['Juan', 'Maria', 'Francisco', 'Alberto', 'dari', 'Ocegueda']
#    0        1          2           3         4         5    
#   -6        -5        -4          -3        -2        -1    

# Insertar un dato en una posición específica de la lista
clientes.insert (-3, "Román")
print (clientes)
print ()
# ['Juan', 'Maria', 'Francisco', 1245621, 'Alberto', 'dari', 'Ocegueda']
#    0        1

# Borrar datos por posición
del clientes[0]
print (clientes)
print ()
# ['Maria', 'Francisco', 'Román', 'Alberto', 'dari', 'Ocegueda']

# Borrar datos por valor
clientes.remove ("Román")
print (clientes)
print ()
# ['Maria', 'Francisco', 'Alberto', 'dari', 'Ocegueda']

# Consultar y eliminar un dato de la lista
tareas = [
    "Lavar los platos", 
    "aliementare al perro", 
    "entregarle el proyecto al cliente", 
    "estudiar"
]

#       Método manual
# tarea = tareas[-1]
# print(f"Ya terminé la tarea '{tarea}'") 
# tareas.remove (tarea)
# print (tareas)

#       Utilizando pop
tarea = tareas.pop() # = tareas.pop(-1)
print(f"Ya terminé la tarea '{tarea}'") 
print (tareas)



