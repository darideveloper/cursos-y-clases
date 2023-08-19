def calcular_promedio (name:str, cal1:float, cal2:float, cal3:float):
    """ Calcular y mostrar el promedio semestral de un alumno

    Args:
        name (str): Nombre del alumno
        cal1 (float): calificación primer examen
        cal2 (float): calificación segundo examen
        cal3 (float): calificación tercer examen
    """
    
    # Calcular promedio multiplicando por 100, convirtiendo a entero y dividiendo entre 100
    promedio = (cal1 + cal2 + cal3) / 3 * 100
    promedio = int (promedio)
    promedio = promedio / 100
    
    # Calcular promedio con la función round
    # promedio = (cal1 + cal2 + cal3) / 3
    # promedio = round (promedio, 2)
    
    # Calcular promedio como texto
    # promedio = (cal1 + cal2 + cal3) / 3
    # promedio = str (promedio)[0:4]
    
    print (f"El promedio de {name} es {promedio}")

# Enviar datos en el orden correcto
calcular_promedio ("Maria", 10, 10, 10)
calcular_promedio ("Dari", 9, 9, 9)
calcular_promedio ("José", 8, 9, 10)
calcular_promedio ("Juan", 4, 9, 9)