try:
    # Intenta hacer la siguiente linea
    import canvas
except:
    # Lineas a ejecutar si ocurre un error
    print ("Installa canvas para continuar")
else:
    # Lineas a ejecutar si no ocurre un error
    print ("Todo bien")

print ("Código final")

estudiantes = ["Ana", "Maria", "Jose", "Pedro", "Juan"]
for estudiante in estudiantes:

    if estudiante == "Ana":
        # Pasar a siguiente variable
        continue

    print (f"reprobaste {estudiante}")