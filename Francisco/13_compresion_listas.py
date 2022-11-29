# For convencional
print ()
numeros_cuadrados = []
for numero in range(1, 11):
    numero_cuadrado = numero**2
    numeros_cuadrados.append (numero_cuadrado)
print (numeros_cuadrados)

# For comprimido / lista comprimida
numeros_cuadrados_2 = [numero**2 for numero in range(1, 11)]
print (numeros_cuadrados_2)