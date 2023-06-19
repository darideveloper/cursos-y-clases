# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

#mostar opciones sobre el menu para el usuario
prompt ="\nWhich pizza topping would you like? \n(Type 'quit' to stop adding toppings) "

#ciclo infinito 
while True:
    #solicitar una opcion al usuario
    topping = input(prompt) # Peperoni
    #limpiando respuesta del usuario
    topping = topping.strip()# quitar espacios en blanco al inicio y al final
    topping = topping.lower()# convertir a minusculas peperoni
    # romper el ciclo/detener
    if topping == "quit":
        break 
    else:
        print (f"Adding '{topping}' to your pizza!")
