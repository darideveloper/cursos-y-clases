# Opèraciones básicas
print (2 + 4) # 6 # suma
print (2 - 4) # -2 # resta
print (2 * 4) # 8 # multiplicación
print (2 / 4) # 0.5 # división
print ()

# Extras de python
print (2 ** 3) # 2 * 2 * 2 = 8 # potencia
print (5 // 3) # 1 # división de piso o división entera
print (5 % 3) # 2 # modulador o residuo
print ()

# Jerarquía de los signos
# 1. potencias y raices
# 2. Multiplicaciones y divisiones
# 3. Sumas y restas
print (1 + 2 * 3) # 1 + 6 = 7 
print ((1 + 2) * 3) # 3 * 3 = 9 
print ()

# Floats
print (0.2 + 0.1)
print (3 * 0.1)
print ()

# Concatenar numeros y texto
nombre = "dari"
apellido = "developer"
edad = 30
nombre_completo = f"{nombre} {apellido} {edad}"
print (nombre_completo)

nombre_completo = nombre + " " + apellido + " " + str(edad)
print (nombre_completo)