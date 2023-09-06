dia = 6

# Mostrar el día de la semana en texto
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
    print ("Sabado")
else:
    print ("Domingo")

# Mostrar el día de la semana en texto (con listas)
dia = 7
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print (dias_semana[dia - 1])