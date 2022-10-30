# Listas anidadas (matriz)
ventas = [
    [123123,123,123,123,123,123,124335464256,],
    [123123,123,123,123,123,123,124335464256,],
    [123123,123,123,123,123,123,124335464256,],
    [123123,123,123,123,123,123,124335464256,],
    [123123,123,123,123,123,123,124335464256,],
    [123123,123,123,123,123,123,124335464256,],    
]

# Recorrer listas anidadas
total_ventas = 500

# Ciclo por cada fila de datos
for ventas_del_día in ventas:
    
    # Ciclo por cada dato (celda)
    for venta in ventas_del_día:

        # Sumnmetar ventas
        total_ventas += 200 
        