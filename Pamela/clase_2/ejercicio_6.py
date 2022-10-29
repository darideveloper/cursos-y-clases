listas_numeros = [
    [1, 1, 3, 4, 4, 5, 6, 7, 0],
    [-4, 5, -8, 9, -6, 10],
]

for lista_numeros in listas_numeros:

    numeros_resultado = []

    numero_anterior = 0

    for numero in lista_numeros:
        
        # resta de numeros
        resta = numero - numero_anterior
        
        # Guardar resultado
        if numero_anterior != 0:
            numeros_resultado.append (resta)
            
        # Sustituir numero anterior
        numero_anterior = numero

    print (f"La lista original: {lista_numeros}")
    print (f"La lista de diferencias: {numeros_resultado}")
    print ()