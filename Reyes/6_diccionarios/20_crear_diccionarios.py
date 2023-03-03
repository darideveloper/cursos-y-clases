# Crear una lista
personaje_list = [180,   123, 12343, 34532, 1342516712]
#                 Salud  atq   def    mana     exp
#                   0     1     2       3       4

# Diccionario con datos del personaje
personaje_dict = {
    "ataque": 123,
    "experiencia": 1342516712,
    "defensa": 12343,
    "mana": 34532,
    "salud": 180
}

# Consultar datos de un diccionario
ataque = personaje_dict["ataque"]
print ("El ataque del personaje es", ataque)
print ()

# Actualizar datos de un diccionario
personaje_dict["ataque"] = 99999
print (personaje_dict)
print ()

# Añadir datos a un diccionario
personaje_dict["ataque magico"] = 199
print (personaje_dict)
print ()

# Borrar datos de un diccionario
del personaje_dict["ataque magico"]
print (personaje_dict)
print ()

# Comenzar con un diccionario en blanco
proyectos = {}

proyectos["elias"] = "python / django"
proyectos["josue"] = "javascript / react"
proyectos["fernando"] = "python / flask"
proyectos["martín"] = "python / django"
print (proyectos)
print ()

# Manipular valores de un diccionario
print ("Estoy trabajando un proyecto de " + proyectos["elias"].title())
print ()