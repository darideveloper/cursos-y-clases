# Obtener los primeros 10 cubos
cubos = []
for numero in range (1, 11):
    cubos.append(numero ** 3)
print (cubos)

# Lista comprimida
cubos2 = [numero**3 for numero in range (1, 11)]
print (cubos2)