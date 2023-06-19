# Variable de contral
is_running = True

# Ciclo infinito con menú
while (is_running):

    # Mostrar menu
    print ("\nMENU: ")
    print ("1. Consultar cliente")
    print ("2. Consultar producto")
    print ("3. Consultar factura")
    print ("4. Salir")

    # Colisitar una opción al usuario
    option = input ("Elige una opción: ")

    # Hacer cosas diferentes en base a la opción elegida
    if option == "1":
        print ("\tCliente")
    elif option == "2":
        print ("\tProducto")
    elif option == "3":
        print ("\tFactura")
    elif option == "4":
        
        # Detener el ciclo
        print ("\tHasta luego")
        is_running = False

# Código después del ciclo
print ("hola")