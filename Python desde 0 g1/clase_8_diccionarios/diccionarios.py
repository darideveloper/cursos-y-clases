# Crear diccionario
usuarios_contraseñas = {
    "dari": "12345**",
    "alberto": "wfjhkavdfnkjvdf",
    "emmanuel": "SEFSDFSFDSFD",
    "josé": "adfsgdafdrgas",
}

nombres = ["Maria", "Pedro", "José"]

# Modificar
usuarios_contraseñas["dari"] = "000000"
# print (usuarios_contraseñas)

# Eliminar
del usuarios_contraseñas["dari"]
# print (usuarios_contraseñas)

# Agregar
usuarios_contraseñas["administrador"] = "12345"
# print (usuarios_contraseñas)

# Buscar elemento
contraseña_paquito = usuarios_contraseñas.get ("paquito") # None
# if contraseña_paquito != None:
#     print ("Paquita si está en el sistema")
    
# Obtener dato de un diccionario
contraseña_paquito = usuarios_contraseñas["paquito"] # Error
# print (contraseña_paquito)

# # Recorrer valores
for contraseña in usuarios_contraseñas.values ():
    print (contraseña)

# Recorre keys
for usuario in usuarios_contraseñas.keys ():
    print (usuario)

# Recorrer valores y keys
for usuario, contraseña in usuarios_contraseñas.items():
    print (f"El usuario {usuario}, tiene la contrsela {contraseña}")

# Diccionario con string en las llaves y lista en los valores
registro_ventas = {
    "lunes": [2, 2, 2],
    "martes": [2, 2, 2],
    "miercoles": [123,456,457,465],
    "jueves": [546,4567,876]
}

# Variuable para almecanr las ventas totales
ventas_semana = 0

# Recorriendo datos
for dia, ventas in registro_ventas.items():
    
    ventas_dia = 0
    
    
    print (f"Las ventas del día {dia} fueron: {ventas}")
    
    # Calcularf ventas del día
    for ventas in ventas:
        ventas_dia += 0
    
    print (f"Y se vendieron un total de {ventas_dia}")
    
    # Sumar ventas de la semana
    ventas_semana += ventas_dia
    
print (f"\nLas ventas totales de la semana fueron: {ventas_semana}")

# Ejemplo de inventario (lista de diccionarios)
items = [
    {
        "nombre": "espada",
        "habilidades": "",
        "peso": "",
    },
    {
        "nombre": "pistola",
        "habilidades": "",
        "peso": "",
    },
]

# Ejemplo de glosario
glosario = {
    "comer": "coqwejhfsfdjkdjhf",
    "prgrammar": "asdfsdaf"
}