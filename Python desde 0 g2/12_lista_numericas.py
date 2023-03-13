# Crear una lista de numeros de forma utomatica

# Contar de 5 en 5 comenzando en el 0 y hasta antes del 101
numeros = list(range (0, 101, 5))
#                numero inicial, antes de el numero final, numeros a saltarse
print (numeros)
print ()

# contar numeros del 5 al 100 
numeros = list(range (5, 101))
print (numeros)
print ()

numeros = list(range (101))
print (numeros)
print ()

# For con listas numericas
for _ in range (3):
    # Simular concetar con base de datos
    print ("Conectando con db...")
    
# Similar que la conexión fue exitosa
print ("Conetado!")
print ()

# 1 - 10

# Calcular el cubo de numeros 
numeros_cubos = []
for numero in range (1, 11): 
    numeros_cubos.append (numero ** 3)
print (numeros_cubos)