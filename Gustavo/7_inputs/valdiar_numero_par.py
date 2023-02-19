# Pedir la edad al usuario
print ("Ingresa tu edad ")
edad_str = input()

# Validar si la edad es numerica
if edad_str.isnumeric():
  
    # Convertir edad a numero entero
    edad = int (edad_str)

    # validar si es par
    edad_par = edad % 2 == 0
    
    # responder si la edad es par o impar
    if (edad_par):
        print ("Tu edad es un numero par")
    else:
        print ("Tu edad es un numero inpar")

# Si la edad no es numerica mostrar un error
else:
    print ("Entrda incorrecta, intenta otra vez")