# For comprimido de texto
comidas = ["pizza", "hamburgesas", "enchiladas", "camarones", "chilaquiles"]

# Forma normal
comidas_mensajes_1 = []
for comida in comidas:
    menesaje = f"A mi me gusta comer: {comida}"
    comidas_mensajes_1.append (menesaje)
print (comidas_mensajes_1) # ['A mi me gusta comer: pizza', 'A mi me gusta comer: hamburgesas', 'A mi me gusta comer: enchiladas', 'A mi me gusta comer: camarones', 'A mi me gusta comer: chilaquiles']
    
# For comprimido
comidas_mensajes_2 = [f"A mi me gusta comer: {comida}" for comida in comidas] # ['A mi me gusta comer: pizza', 'A mi me gusta comer: hamburgesas', 'A mi me gusta comer: enchiladas', 'A mi me gusta comer: camarones', 'A mi me gusta comer: chilaquiles']

# For comprimido de numeros
numeros = range (1, 11)

# Forma normal
numeros_cuadrados_1 = []
for numero in numeros:
    cuadrado = numero ** 2
    numeros_cuadrados_1.append (cuadrado)
print (numeros_cuadrados_1) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numeros_cuadrados_2 = [numero**2 for numero in numeros]
print (numeros_cuadrados_2) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]