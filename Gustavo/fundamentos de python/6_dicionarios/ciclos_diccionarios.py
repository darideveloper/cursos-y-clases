estudiantes = {
    "juan": 9,
    "maria": 8,
    "pedro": 6,
    "dari": 8,
    "gilberto": 6
}

# Recorrer claves
for nombre_estudiante in estudiantes.keys():
    print (nombre_estudiante)
print ()
    
# Recorrer claves
for cal_estudiante in estudiantes.values():
    print (cal_estudiante)
print ()

# Recorrer claves y valores
for nombre_estudiante, cal_estudiantes in estudiantes.items():
    print (f"El estudiante {nombre_estudiante} obtuvo {cal_estudiantes}")
print ()

# Recorrer diccionarios anidados / nesting
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

for nombre, datos in estadisticas.items():
    for dato_nombre, dato_valor in  datos.items():
        print (f"El dato {dato_nombre} del usuario {nombre} es {dato_valor}")


{
    'col_1': [3, 2, 1, 0], 
    'col_2': ['a', 'b', 'c', 'd']
}