# # Datos de ejemplo como listas
calificaciones = [10, 8, 10, 4, 8]
nombres = ["Maria", "Pedro", "José", "Alberto"]

# # Datos de ejemp0lo como dirección
# calificaciones_alumnos = {
#     "Maria": 10,
#     "Pedro": 8,
#     "José": 10,
#     "Alberto": 4
# }

# print(calificaciones_alumnos["Pedro"])

cantidades = {
    'playera': 25,
    'pantalon': 10, 
    'short': 2, 
    'sudadera': 5, 
    'bufanda': 0
}

precios = {
    'playera': 50,
    'pantalon': 100, 
    'short': 75, 
    'sudadera': 150,
    'bufanda': 25
}

# Nuevo diccionario
ganancias = {}

for producto in cantidades.keys():
    
    # Obtener datos
    precio = precios[producto]
    cantidad = cantidades[producto]
    
    # Calcular ganancia
    ganancia = precio * cantidad
    
    # Almacenar resultado
    ganancias[producto] = ganancia