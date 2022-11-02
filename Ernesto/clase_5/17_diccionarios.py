# Crear un diccionario
ventas = {
    "miercoles": 40,
    "martes": 20,
    "viernes": 50,
    "lunes": 10,
    "sábado": 10,
    "jueves": 120,
    "domingo": 5,
}

# # Consultar datos de un diccionario
# print (ventas["lunes"])

# # Modificar valores
# ventas["lunes"] = 100
# print (ventas)

# # Borrar valores
# del ventas["lunes"]
# print (ventas)

# # Agregar valores
# ventas["x"] = 0
# print (ventas)

# # Consultar si elemento existe
# venta_enero = ventas.get ("enero", "valor predeterminado si no se encuntra el key")
# print (venta_enero)

# # Operaciones con vaklores
# ventas_x = ventas["domingo"] + ventas["martes"]
# print (ventas_x)

# # Ciclos con diccionarios

# Recorrer los keys
# for dia in ventas.keys():
#     print (dia.upper())
    
# # Ordenar keys de un diccionario
# dias = list (ventas.keys())
# dias.sort ()
# for dia in dias:
#     print (dia.title ())

# recorrer los values
# total_numero_ventas = 0
# for numero_ventas in ventas.values ():
#     print (numero_ventas)
#     total_numero_ventas += numero_ventas
# print (f"El total de de numero de ventas fue: {total_numero_ventas}")

# Recorrer keys y values
# for key, value in ventas.items():
#     print (f"El día {key} se realizaron {value} de ventas")
    