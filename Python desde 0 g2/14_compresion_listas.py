# Calcular el cubo de numeros (forma de tradicional) 
numeros_cubos = []
for numero in range (1, 11): 
    numeros_cubos.append (numero ** 3)
print (numeros_cubos)

# Calcular el cubo de numeros (forma comprimida) 
numeros_cubos = [numero ** 3 for numero in range (1, 11)]
print (numeros_cubos)