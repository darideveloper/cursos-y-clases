# Ordenar alfabeticamente y permanentemente
autos = ['renault', 'vmw', 'honda', 'mercedes benz']
autos.sort ()
print (autos) # ['honda', 'mercedes benz', 'renault', 'vmw']

# Ordenar alfabeticamente y permanentemente en orden inverso
autos = ['renault', 'vmw', 'honda', 'mercedes benz']
autos.sort (reverse=True)
print (autos) # ['vmw', 'renault', 'mercedes benz', 'honda']

# Ordenar alfabeticamente y temporalmente
autos = ['renault', 'vmw', 'honda', 'mercedes benz']
autos_ordenados = sorted(autos)
print (autos) # ['renault', 'vmw', 'honda', 'mercedes benz']
print (autos_ordenados) # ['honda', 'mercedes benz', 'renault', 'vmw']

# Ordenar alfabeticamente y temporalmente
autos = ['renault', 'vmw', 'honda', 'mercedes benz']
autos_ordenados = sorted(autos, reverse=True)
print (autos) # ['renault', 'vmw', 'honda', 'mercedes benz']
print (autos_ordenados) # ['vmw', 'renault', 'mercedes benz', 'honda']

# invertir el orden de una lista
ventas = ["maria", "pedro", "josé", "alberto"]
ventas.reverse() # ['alberto', 'josé', 'pedro', 'maria']
print (ventas)
ventas.reverse() # ['maria', 'pedro', 'josé', 'alberto']
print (ventas)

# Contar la cantidad de elementos de una lista
autos = ['renault', 'vmw', 'honda', 'mercedes benz']
numero_autos = len (autos) # 4
print (f"hay un total de: {numero_autos} autos")
print ("hay un total de: " + str(numero_autos) + " autos")
print (len(autos))
