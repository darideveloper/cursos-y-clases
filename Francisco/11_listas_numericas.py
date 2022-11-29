# Crear listas numericas
numeros = list(range (1, 11))
print (numeros)

# realizar una acción cierto numero de veces
print ()
for numero in range(3):
    print ("Intentando guardar datos...")
    
# Ejemplo: Obtener cuadrados de numeros
print ()
numeros_cuadrados = []
for numero in range(1, 11):
    numero_cuadrado = numero**2
    numeros_cuadrados.append (numero_cuadrado)
    
print (numeros_cuadrados)
