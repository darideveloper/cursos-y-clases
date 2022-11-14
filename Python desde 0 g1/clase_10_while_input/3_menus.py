while True:
    print ("\nMENU:")
    print ("1. Consultar pokemon")
    print ("2. Consultar ataques")
    print ("3. Contar habitad")
    print ("4. Salir")
    option_menu = input ("Escribe una opción: ")

    if option_menu == "1":
        
        while True:
            print ("\nTipos disponibles")
            print ("1. Agua")
            print ("2. Fuego")
            print ("3. Planta")
            print ("4. Salir")
            option_tipo = input ("Escribe una opción: ")
            
            if option_tipo == "1":
                print ("Los pokemon de tipo agua son:")
            elif option_tipo == "2":
                print ("Los pokemon de tipo fuego son:")
            elif option_tipo == "3":
                print ("Los pokemon de tipo planta son:")  
            elif option_tipo == "4":
                break
            else:
                print ("Opción invalida.") 
        
    elif option_menu == "2":
        print ("Los ataques disponibles son: ...")
    elif option_menu == "3":
        print ("Las habitads disponibles son: ...")
    elif option_menu == "4":
        break
    else:
        print ("Opción invalida. Intenta otra vez")
        
print ("Terminado")