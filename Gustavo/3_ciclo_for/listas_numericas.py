# Hacer un ciclo un cierto numero de veces
for contador in range(10): # [0, 1, 2, 4, 5, 6, 7, 8, 9]
    print (f"({contador + 1 }) Intentando conectar a db...")
print ()

# Crear una lista numerica
numeros = list(range(100)) # [0, 1, 2, 3 ... 99]
print (numeros)
print ()

# Crear una lista numerica, indicando inciio y final (desde, hasta antes de)
numeros = list(range(10, 31))
print (numeros)
print ()

# Crear una lista numerica, indicando inciio y final, e indicando numeros salteados
numeros = list(range(3, 100, 3))
print (numeros)
print ()

# Crear una lista numerica, indicando inciio y final, e indicando numeros salteados (numeros negativos)
numeros = list(range(10, 1, -1))
print (numeros)
print ()

# Obtener los primeros 10 cubos
cubos = []
for numero in range (1, 11):
    numero_cubo = numero ** 3
    cubos.append (numero_cubo)
print (cubos)