# Write a program that polls users about their dream vacation. Write a prompt similar to "If you could visit one place in the world, where would you go?" Include a block of code that prints the results of the poll.

#diccinario vacio para almacenar las respuestas
responses = {}

polling_active = True # variable activa/bandera para controlar la duracion del bucle

while polling_active:
    # preguntando por el nombre de la persona y haciendo pregunta.
    name = input("\nWhat is your name? ")
    place = input("Where in the world would be your dream vacation? ")

    responses[name] = place # guardando respuestas en el diccionario
    
    # condicional para averiguar si alguien mas hace la encuesta.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower().strip() == "no":
        polling_active = False # variable bandera para salir del bucle
        
# imprimiendo todos los resultados usando un bucle For.
print ("This is a polling results:")
for name, place in responses.items():
    print (f'{name} dream vacation is in {place}')