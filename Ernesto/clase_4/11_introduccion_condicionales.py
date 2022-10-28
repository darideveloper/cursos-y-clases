# Comprar numeros
edad = 16

# == igual a
# != diferente de
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que

if edad == 18:
    print ("felicidades, eres mayor de edad!")
else:
    print ("No eres mayor de edad")
    
    
    
# Comparación de textos

# == igual a
# != diferente de

status = "activo"
if status == "activo":
    print ("El usuario está activo")
else:
    print ("El usuario no está activo")
    
    
    
# Inicio y terminación de textos

# .startswith
# .endswith

status = "error: intente de nuevo"
if status.startswith("error:"):
    print ("Hubo un error")
else:
    print ("Todo bien")
    
    
# Unir condiciones

# AND
# OR

edad = 1000
if edad >= 18 and edad < 100:
    print ("Eres mayor de edad")
else:
    print ("No eres mayor de edad, o tu edad incorrecta")
    
    
    
# Condicionales en ciclos
calificaciones =  [10, 8, 6, 4, 9, 10, 3, 3]
for calificacion in calificaciones:
    if calificacion >= 6:
        print (f"{calificacion} Aprobaste")
    else:
        print (f"{calificacion} Reprobaste")
        
        
# Prguntar por elementos en listas
usuarios_baneado = ["maria", "pedro", "josé"]
if "zdgvdsfgdgf" not in usuarios_baneado:
    print ("Puedes entrar a la pagina web")
else:
    print ("No puedes entrar a la web")

# Bools
activiado = True
activiado = False

# bloque completo de if-elif-else
for dia in range(1,20):
    
    # Mostrar el nombre del día
    if dia == 1: 
        print ("Lunes")
    elif dia == 2:
        print ("Martes")
    elif dia == 3:
        print ("Miercoles")
    elif dia == 4:
        print ("Jueves")
    elif dia == 5:
        print ("Viernes")
    elif dia == 6:
        print ("Sábado")
    elif dia == 7:
        print ("Domingo")
    else:
        print ("Ese día no existe")
        
# ifs separados
usuarios_nombres = ["maria", "pedro", "josé", "alberto", "iris"]
usuarios_edades = [12, 25, 14, 50, 26]

if len(usuarios_nombres) == len(usuarios_edades):

    for index in range (0, len(usuarios_nombres)):
        usuario = usuarios_nombres[index]
        edad = usuarios_edades[index]
        
        print (f"El usuario {usuario} tiene {edad}")
        
        # Proceso A: verificando edad
        if edad >= 18: 
            print ("Tienes edad para entrar")
        else:
            print ("No eres mayor de edad")
        
        # Proceso B: detectando usuarios baneados
        if usuario == "maria":
            print ("Tu no tienes permiso de entrar")
            
        print ("")   
else:
    print ("La informaición esta corrupa")