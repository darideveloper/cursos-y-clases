# COMILLAS

texto1 = "Juan" # Comillas dobles
texto2 = 'Juan' # Comillas simples
texto3 = """Juan""" # Comillas triples

# Comillas dobles dentro de texto
cita = 'Albert Aiinstain dijo: "Todo debe simplificarse lo máximo posible, pero no más"'

# Comillas simples dentro de texto
message = "Ana's book"

# Comillas dobles y simples dentro de texto
parrafo = """Lorem''' ipsum d""o"lor sit amet, con"s""ectetur adipiscing elit. """

print (cita)
print (message)
print (parrafo)

# CASES

nombre = "JuAn LoPeZ"
print (nombre.upper()) # JUAN LOPEZ
print (nombre.lower()) # juan lopez
print (nombre.title()) # Juan Lopez

# CANCATENAR (UNIR TEXTOS)

nombre = "Alberto"
apellido = "Martinez"
edad = 50
print ("Bienvenido usuario " + edad + " " + apellido)

# CONCATENAR (STRING PREFORMATEADOS / F-STRINGS)
nombre = "Alberto"
apellido = "Lopez"
print (f"Bienvenido usuario {nombre} {apellido}") 

# CARACTERES ESPECIALES
parrafo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\nLorem ipsum dolor sit amet, consectetur adipiscing elit."
nombre = "\t\t\tJuan"
print (parrafo)
print (nombre)

# QUITAR ESPACIOS EN BLANCO
name = "     HOLA    "
name_clean = name.rstrip() # "     HOLA"
name_clean = name.lstrip() # "HOLA    "
name_clean = name.strip() # "HOLA"
print (f"'{name_clean}'")