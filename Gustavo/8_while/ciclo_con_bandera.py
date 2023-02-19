running = True

# Ciclo infinito
while running:
    
    # Mostrar menu
    print ()
    print ("1. Enviar correo a usuario\n2. Consultar DB de usuarios\n3. Dar de alta a cliente en sistema\n4. salir\n")
    opcion = input ("¿Que necesitas?")
    
    # Hacer ciartas acciones cuando se selecciona una opción
    # ....
    
    # Condición para detener el ciclo
    if opcion == "4":
        print ("Bye")
        running = False
        
print ("Final del programa")