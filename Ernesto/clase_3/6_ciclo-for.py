# Ciclos en base a listas

# usuarios = ["maria@gmail.com", "pedro@gmail.com", "josé@gmail.com", "maria@gmail.com", "pedro@gmail.com", "josé@gmail.com"]

# print ("Inicio del programa")

# for usuario in usuarios:
#     usuario_fomatted = usuario.title()
#     print (f"enviado correo a: {usuario_fomatted}...")

# print ("final del programa")


# Ciclo un numero determinado de veces
# for numero in range(3):
#     print ("Intentando conectar a base de datos...")
    
# # Generar lista de numeros
# numeros = list(range(5, 10))
# print (numeros)

# Ciclos con operadores
# cuadrados = []
# for num in range (1,21):
#     cudrado = num ** 2
#     cuadrados.append (cudrado)
    
# ventas = [100, 200, 300, 1400, 500, 600, 100, 900, 900]
# comisiones = []
# for venta in ventas:
#     comisiones.append (venta * 0.1)
# print (comisiones)

# Funciones estadisticas
# ventas = [100, 200, 300, 1400, 500, 600, 100, 900, 900]
# print(f"El minimo de ventas es: {min (ventas)}")
# print(f"El maximo de ventas es: {max (ventas)}")
# print(f"La suma de ventas es: {sum (ventas)}")
# print(f"El numero de ventas es: {len (ventas)}")

# promedio = sum (ventas) / len (ventas)
# print(f"El promedio de ventas es: {promedio}")

# Compesión de listas
cuadrados = [ num**2 for num in range (1,21) ]
print (cuadrados)
