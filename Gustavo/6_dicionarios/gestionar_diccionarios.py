nombres = ["juan", "maria", "pedro"]
calificaciones = [9, 8, 6]

# Crear diccionario de alumnos y calificaciones
estudiantes = {
    "juan": 9,
    "maria": 8,
    "pedro": 6
}

# Accder a datos de un diccionario
print("La calificación de juan es: " + str(estudiantes["juan"]))

# Añadir valores a un diccionario
estudiantes["ana"] = 10

# actualizar valores de un diccionario
estudiantes["pedro"] = 10

# Empezar con un diccionario vacío / y estructura de datos
estadisticas = {}
estadisticas["dari"] = [10, 561241, 5412, 42135213]
estadisticas["abel"] = [23, 213, 321, 31223]
"""
{
    "dari": [10, 561241, 5412, 42135213], 
    "abel": [23, 213, 321, 31223]
}
"""
print (estadisticas)

# Diccionarios dentro de diccionario
estadisticas = {}
estadisticas["dari"] = {
    "viwers": 100,
    "comentarios": 200,
    "likes": 300
}
estadisticas["abel"] = {
    "viwers": 1213,
    "comentarios": 213523,
    "likes": 1235
}
print (estadisticas)
print ()

# Remover elementos de un diccionario
del estadisticas["abel"]
print (estadisticas)
print ()

# Actualizar valores anidados
estadisticas["dari"]["viwers"] = "10000"
print (estadisticas)