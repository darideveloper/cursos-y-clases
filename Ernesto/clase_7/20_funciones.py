# Crear una función que recibe un parametro / dato
def saludo (nombre:str):
    """ Función que imprime un saludo

    Args:
        nombre (str): nombre de la persona a saludar
    """
    
    # Imprimir un mensaje de saludo personalizado
    print ("Hola, bienvenido")
    print (f"usuario {nombre}")
    print ("como estás?")
    print ()
    
# Utilizar la función ya creada, enviando un datos diferentes
saludo ("Juan")
saludo ("maria")
saludo ()

# Función con varios parametros
def suma_dos_numeros (num_a:int, num_b:int):
    # Imprimir la suma de los dos numeros y un mensaje
    suma = num_a+num_b
    print (f"El resultado de la suma es: {suma}")
    
suma_dos_numeros (2, 3)
suma_dos_numeros (5, 6)
suma_dos_numeros (10, 20)

# Devolver valores
def suma_dos_numeros (num_a:int, num_b:int):
    """ Función para sumar dos numeros enteros

    Args:
        num_a (int): primer numero a sumar
        num_b (int): segundo numero a sumar

    Returns:
        int: el resultado de la suma
    """

    # Devolver la suma de los dos numeros, para poder usarlos afuera de la función
    return num_a+num_b

# Llamar a la función y almacenar el valor que devuelve
resultado_suma = suma_dos_numeros (2, 3)

print (resultado_suma)
print (f"La función devolció lo siguiente: {resultado_suma}")


# Valores por defecto
def peniultimo_mayusculas (nombres:list = ["maria", "pedro", "juan", "alberto"]):
    # Función para obtener el peniultimo elemento de una lista, en mayusculas.
    # Si la función no recibe la variable "nombres", esta ya cuenta con una lista por defecto
        
    peniultimo = nombres[-2]
    penultimo_mayus = peniultimo.upper()
    
    return penultimo_mayus

# Llamar a la función enviando una lista de valores
nombres = ["maria", "pedro", "juan", "alberto", "josé"]
penultimo_nombre_mayusculas = peniultimo_mayusculas (nombres)
print (penultimo_nombre_mayusculas)

# Llamar a la función usando los valores por defecto (sin enviar nada)
penultimo_nombre_mayusculas = peniultimo_mayusculas ()
print (penultimo_nombre_mayusculas)

# Key arguments
def suma_dos_numeros (num_a:int = 10, num_b:int = 20):
    print (f"El resultado de la suma es: {num_a+num_b}")
    
# Enviar un dato a la función, pero en un orden diferente
suma_dos_numeros (num_b=10)