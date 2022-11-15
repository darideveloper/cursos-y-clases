# Modulo (obtener el rediuo de una división)
while True:
    entrada_usuario = input ("Escribe un numero: ")

    try:
        numero = int(entrada_usuario)
    except:
        print ("Entrada incorrecta")
    else:
        residuo = numero % 2
        
        if residuo == 0:
            print ("Es par")
        else:
            print ("Es impar")