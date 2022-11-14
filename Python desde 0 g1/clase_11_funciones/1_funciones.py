# nombres = ["Maria", "Pedro", "Juan"]

# print(f"Hola, como has estado, {nombres[0]}")

# print(f"Hola, ¿qué tal la familia {nombres[1]}")

# print(f"Hola, te gusta pokemon, {nombres[2]}")

# Definir una función
def saludar ():
    """ Mostrar un saludo
    """
    print ("Hola, como estás?")

# Fuinción con variable
def saludar_2 (nombre:str):
    """ Mostrar un saludo personalizado

    Args:
        nombre (str): nombre de la persona a saludar
    """
    print (f"Hola, como estás {nombre}?")
    
def suma (numero_a:int, numero_b:int):
    """ Realizar y mostrar suma de dos numeros

    Args:
        numero_a (int): primero numero a sumar
        numero_b (int): segundo numero a sumar
    """
    resultado = numero_a + numero_b
    print (f"El resultado de la suma es: {resultado}")
    
# Variables opcionale
def saludar_3 (nombre:str="Usuario"):
    """ saludar a un usuario por su nombre, con valor por defecto

    Args:
        nombre (str, optional): nombre del usuario. Defaults to "Usuario".
    """
    print (f"Hola, como estás {nombre}?")
    
def suma (numero_a:int=10, numero_b:int=20):
    """ Sumar dos numeros con valores por defecto

    Args:
        numero_a (int, optional): primero numero a sumar. Defaults to 10.
        numero_b (int, optional): segundo numero a sumar. Defaults to 20.
    """
    resultado = numero_a + numero_b
    print (f"El resultado de la suma es: {resultado}")


# Retornar valores
def calcular_promedio (cal1, cal2, cal3):
    """ Calcular el promedio de tres calificaciones

    Args:
        nombre (str): nombre del estudiante
        col1 (int): primera calificación
        col2 (int): segunda calificación
        cal3 (int): tercera calificación
    """
    
    promedio = (cal1 + cal2 + cal3) / 3
    return promedio

prom = calcular_promedio ("Juanito", 10, 8, 6)

# retornar dos o mas valores
def calcular_promedio (nombre, cal1, cal2, cal3):
    """ Calcular el promedio de tres calificaciones

    Args:
        nombre (str): nombre del estudiante
        col1 (int): primera calificación
        col2 (int): segunda calificación
        cal3 (int): tercera calificación
    """
    
    promedio = (cal1 + cal2 + cal3) / 3
    return {"nombre": nombre, 
            "promedio": promedio}

nombre, promedio = calcular_promedio ("Juanito", 10, 8, 6)
print (nombre)

# Pasar listas