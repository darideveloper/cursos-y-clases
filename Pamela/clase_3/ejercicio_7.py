listas_numeros = [
    [0, 3, 4, 7, 9],
    [3, 5, 7, 13],
    [1, 2, 3, 7]
]

def primo (numero):
    # Verificar si un numero es primo
    
    # Si el numero es 0 o 1, decir que no es primo
    if numero == 0 or numero == 1:
        return False
    
    # Verificar si es disivible entre cualquiera de los numeros anteriores
    for numero_anterior in range(2, numero):
        residuo = numero % numero_anterior
        if residuo == 0:
            return False
    
    # Decir que es primo, si no es diovisbles  
    return True

# recorrer listas
contador_listas = 1
for lista_numeros in listas_numeros: 
        
    # Recorer numeros
    todos_son_primos = True
    for numero in lista_numeros:
        es_primo = primo (numero)
        
        if not es_primo:
            todos_son_primos = False
            break 
        
    if todos_son_primos:
        resultado = "Todos los números son primos"
    else:
        resultado = "Alguno no es primo"
    
    print (f"La lista {contador_listas} es: {lista_numeros} y el resultado es: {resultado}")
    
    # Aumentar contador
    contador_listas += 1
    