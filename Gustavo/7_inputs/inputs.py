# Intentar convertir entdada del usuario a entero
try:
    # Solicitar entrada del usuario
    edad = int(input ("Ingresa tu edad: "))   
except:
    print ("Entrada inmcorrecta")
    quit ()

if edad > 50:
    print ("ya estás viejo")
elif edad > 30:
    # menos de 50 y en mas 30
    print ("Eres un adulto")
else:
    print ("todavia estás joven")