mensaje = "Bienvenido a python. Escribe 'quit' para salir\n"

# Ciclo infinito
while (True):
    
    # Mostrar mensaje y pedir respuesta
    res = input (mensaje)
    
    # Limpiar respuesta del usuario
    res = res.strip().lower() # strip() quita espacios en blanco al inicio y al final de la cadena, lower() convierte la cadena a minúsculas
    
    # Detener el ciclo si el usuario escribe "quit"
    if res == "quit":
        break