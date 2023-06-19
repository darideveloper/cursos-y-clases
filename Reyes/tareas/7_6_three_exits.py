# Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once: 
# • Use a conditional test in the while statement to stop the loop. 
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

#mensaje para determinar el costo de un boleto para el cine conforme a la edad del usuario
# prompt = """
# Bienvenido, digita tu edad para determinar el costo de tu boleto
# (Introduce 'quit' para terminar): 
# """

prompt = "Bienvenido, digita tu edad para determinar el costo de tu boleto"
prompt += "\n(Introduce 'quit' para terminar): "


active = True # variable activa para controlar la duracion del bucle/bandera.

#bucle infinito
while active:
    user_input = input(prompt) #peticion al usuario
    
    #salir de ciclo/romper
    if user_input == 'quit':
        active = False #variable activa cambia False
    else:
        
        try:
            # Intentar convertir a entero
            user_age = int(user_input) #convirtiendo datos a enteros
        except:
            print ("Entrada no valida, intentalo de nuevo.")
            continue
        
        #en base a la edad del usuario hacer cosas diferentes para determinar costo del boleto
        if user_age < 3:
            costo = 0
        elif user_age <= 12:
            costo = 10
        else:
            costo = 15
            
        print (f"El precio de tu boleto es {costo}")