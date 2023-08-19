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

    print (f"El promedio de {name} es {promedio}")

# Enviar TODOS los datos en orden personalizado
calcular_promedio (cal2=10, cal1=10, cal3=10, name="Maria")

# Enviar ALGUNOS datos en orden personalizado
calcular_promedio ("Maria", 10, cal3=10, cal2=10)