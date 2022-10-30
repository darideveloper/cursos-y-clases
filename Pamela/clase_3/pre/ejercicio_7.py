listas_numeros = [
    [0, 3, 4, 7, 9],
    [3, 5, 7, 13],
    [1, 2, 3, 7],
]

def es_primo (numero):   
    
    # Indicar que los numeros 0 y 1 no son primos
    if numero == 0 or numero == 1:
        return False
        
    # Verificar si el humero actual es divisble entre algunos de sus anteriores
    for numero_anterior in range (2, numero):
        if numero % numero_anterior == 0:
            return False
        
    # Si no se encontro ningun divisor, el numero es primo
    return True

# Ciclo por cada lista de numero
for lista_numeros in listas_numeros:
    
    # Contador de lista
    contador_lista = listas_numeros.index (lista_numeros)
    
    # Ciclo por cada numero
    no_primo = False
    for numero in lista_numeros:
        
        # Consultar si el numero actual es primo
        no_primo = not es_primo (numero)
        
        # Detener ciclo si el numero no es primo
        if no_primo:
            break
    
    # Mostrar resultado
    message = ""
    if no_primo:
        message = "Alguno no es primo"
    else:
        message = "Todos lo numeros son primos"
    print (f"La lista {contador_lista} es: {lista_numeros} y el resultado es: {message}")
        
        
        
        
    
    
    