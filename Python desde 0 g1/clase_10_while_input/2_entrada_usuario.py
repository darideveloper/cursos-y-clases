# Leer entrada de usuario
# print ("Escribe tu nombre: ")
# nombre = input ()
# print (f"Hola usuario {nombre}")

# Convertir entrada de usuario
edad_texto = input ("Cuantos años tiernes? ")

# Try catch
try:
    # Intentar hacer esta linea de código
    edad = int(edad_texto)
except:
    # Si hay un error, hacer esto
    print ("Entrada incorrecta")
else:
    # Hacer esto si no hay ningún error
    if edad >= 18:
        print ("Eres mayor de edad")
    else:
        print ("Eres menor de edad")