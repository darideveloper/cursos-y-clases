import random

# Generar numero aleatorio
ran_num = random.randrange(1, 10)
print (ran_num)


# Ciclo para solicitar respuesta
adinvinado = False
for _ in range(3):

    # Solicitar entrada al usuario
    valor_usuario = int(input ("escoje un numero del 1 al 9: "))
    
    # Verificar la entrada del usuario
    if valor_usuario == ran_num:
        print ("Felicidades, numero adivinado!")
        adinvinado = True
        break
    else:
        print ("Vulve a intentar")

if not adinvinado:
    print (f"Suerte para la proxima. El numero era {ran_num}")