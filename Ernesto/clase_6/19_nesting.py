# Nesting de lista en diccionarios
ventas = {
    "miercoles": [500, 270, 80, 1234],
    "martes": [600, 270, 80, 1234],
    "viernes": [700, 270, 80, 1234],
    "lunes": [800, 270, 80, 1234],
    "sábado": [900, 270, 80, 1234],
    "jueves": [1000, 270, 80, 1234],
    "domingo": [1100, 270, 80, 1234],
}

for dia, registro_ventas in ventas.items():
    
    total_venta = 0
    for venta in registro_ventas:
        total_venta += venta
        
    
    # print (f"El día {dia} se vendieron un total de: {total_venta}")
    
# Nestring de diccionarios en listas
estudiantes = [
    {
        "nombre": "juanito", 
        "edad": 22, 
        "carrera": "systemas"
    },
    {"nombre": "alberto", "edad": 22, "carrera": "systemas"},
    {"nombre": "josé", "edad": 22, "carrera": "systemas"},
    {"nombre": "juan", "edad": 22, "carrera": "systemas"},
    {"nombre": "maría", "edad": 22, "carrera": "systemas"},
]

for estudiante in estudiantes:
    
    nombre = estudiante["nombre"]
    # print (f"Hola, como estás {nombre.title()}")
    
# Nesting de listas en listas
numeros = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
]

# Nesting de diccionarios en diccionarios
ventas = {
    "miercoles": {
        "juan": 10,
        "alberto": 500,
        "josé": 100
    },
    "martes": {
        "juan": 200,
        "alberto": 100,
        "josé": 100
    },
}

# Acceder a un valor en específico
# print (ventas["martes"]["juan"])

# Recorrer
for dia, datos_venta in ventas.items ():
    
    print (f"\nDia actual: {dia.upper()}")
    
    print ("Ventas realizadas: ")
    
    for nombre, venta in datos_venta.items():
        print (f"\tEl vendedor {nombre} realizó {venta} ventas")
