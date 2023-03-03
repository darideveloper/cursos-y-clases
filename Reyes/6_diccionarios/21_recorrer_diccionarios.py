# Comenzar con un diccionario en blanco
proyectos = {}

proyectos["elias"] = "python / django"
proyectos["josue"] = "javascript / react"
proyectos["fernando"] = "python / flask"
proyectos["martín"] = "python / django"
print (proyectos)
print ()

# {
#     'elias': 'python / django', 
#     'josue': 'javascript / react', 
#     'fernando': 'python / flask', 
#     'martín': 'python / django'
# }

# Recorrer los keys de un diccionario
for cliente in proyectos:
    print (cliente)
print ()
    
for cliente in proyectos.keys():
    print (cliente)
print ()

# Recorrer valores de un diccionario 
for proyecto in proyectos.values():
    print (proyecto)
print ()

# Convert los keys a una lista
proyectos_keys = list(proyectos.keys())
print (proyectos_keys)
print ()

# Convert los valores a una lista
proyectos_values = list(proyectos.values())
print (proyectos_values)
print ()

# Recorrer keys y valores de un diccionario
for cliente, proyecto in proyectos.items ():
    print (f"Estoy trabajando un proyecto de {proyecto} para mi cliente {cliente}")