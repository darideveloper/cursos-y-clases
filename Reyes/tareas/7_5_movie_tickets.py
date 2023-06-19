# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

#mensaje para determinar el costo de un boleto para el cine, de acuerdo a la edad del usuario.
prompt = "Bienvenido, digita tu edad para determinar el costo tu boleto: "

#ciclo infinito
while True:
    user_age = input(prompt) #mostrar solicitud al usuario
    
    try:
        # Intentar convertir a entero
        user_age = int(user_age) #convirtiendo datos a enteros
    except:
        print ("Entrada no valida, intentalo de nuevo.")
        continue
        
    # en base a la edad del usuario, hacer cosas diferentes para determinar el costo de su boleto
    if user_age < 3:
        costo = 0
    elif user_age <= 12:
        costo = 10
    else:
        costo = 15
                
    print (f"El precio de tu boleto es {costo}")    
                 

    