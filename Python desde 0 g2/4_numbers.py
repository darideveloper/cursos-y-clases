# Operaciones aritméticas básicas
print (10.5 + 2) # 12
print (10 - 2) # 8
print (10.5 * 2) # 20
print (10.5 / 2) # 5.0
print ()

# operaciones complejas
print (10 ** 2) # 10 * 10 = 100
print (10 // 3) # 3 (sobran 1)
print (10.5 % 3) # 1
print ()

# jerarquia de operaciones
print (10 * (5 + 2) ** 2)
print (10 * 5 + 2 ** 2)
print ()

# numeros grandes
segundos = 2_147_612_398
print (segundos / 10)
print ()

# Combinar numeros y texto
nombre = "Juanito"
edad = 35
print (nombre + " tienes " + str(edad)) # Juanito tienes 35
print (f"{nombre} tienes {edad}") # Juanito tienes 35