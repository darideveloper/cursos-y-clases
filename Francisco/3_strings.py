# Comillas
nombre1 = "Ana's book" # Comillas dobles
nombre2 = ' Albert Eaintain dijo "la jente es tonta" ' # Comillas simples
nombre3 = """ Ana's book Albert Eaintain dijo "la jente es tonta" """ # Comillas triples

# Case
nombre = "FraNCiscO darI" # texto original
nombre_minusculas = nombre.lower() # francisco dari
nombre_mayusculas = nombre.upper() # FRANCISCO DARI
nombre_title = nombre.title() # Francisco Dari

print (nombre)
print (nombre_minusculas)
print (nombre_mayusculas)
print (nombre_title)
print (nombre)
print ()

# Concatenar (normal)
nombre = "Juan"
apellido = "Lopez"
nombre_completo = nombre.upper() + " " + apellido # JUAN Lopez
print (nombre_completo)

# Concatenar (f-string)
nombre_completo = f"{nombre} {apellido.upper()}" # Juan LOPEZ
print (nombre_completo)

# Espacios en blanco / Caracteres especiales
print ()
print ("\tHola\n\t\tMundo")

# Remover espacio en blanco
print ()
nombre = "    \n     Juan Lopez \t    "
mensaje = f"Hola --{nombre.lstrip()}--"
print (mensaje)

mensaje = f"Hola --{nombre.rstrip()}--"
print (mensaje)

mensaje = f"Hola --{nombre.strip()}--"
print (mensaje)