def calcular_promedio (name:str, cal1:float=0, 
                       cal2:float=0, cal3:float=0):
    
    """ Calcula el promedio de 3 calificaciones y lo imprime en pantalla

    Args:
        name (str): Nombre de la persona
        cal1 (float, optional): Calificación del primer examen. Defaults to 0.
        cal2 (float, optional): Calificación del segundo examen. Defaults to 0.
        cal3 (float, optional): Calificación del tercer examen. Defaults to 0.
    """
    
    
    # Calcular promedio multiplicando por 100, convirtiendo a entero y dividiendo entre 100
    promedio = (cal1 + cal2 + cal3) / 3 * 100
    promedio = int (promedio)
    promedio = promedio / 100

    print (f"El promedio de {name} es {promedio}")

# Enviar TODOS los datos en orden personalizado
calcular_promedio (cal2=10, cal1=10, cal3=10, name="Maria")

# Enviar ALGUNOS datos en orden personalizado
calcular_promedio ("Maria", 10)

# Error: no se envio ningún dato
# calcular_promedio ()

# se envian datos pero no el obligatorio
calcular_promedio (cal1=10, cal2=10, cal3=10)

