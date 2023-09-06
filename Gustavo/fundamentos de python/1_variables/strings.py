nombre = "DAri DEveLoper"

# Cases
print (nombre.upper())
print (nombre.lower())
print (nombre.title())
print ()

# Concatenar (normal)
nombre = "dari"
apellido = "developer"
nombre_completo = nombre + " " + apellido
print (nombre_completo)

# Concatenar (f-strings)
nombre = "dari"
apellido = "developer"
nombre_completo = f"{nombre} {apellido}"
print (nombre_completo)
print ()

# Caracteres especiales / Espacios en blanco
print ("\tHola mundo\nEstoy aprendiendo python")
print ()

# Strip caracteres en blanco
nombre = "   \tDari Developer\n   "
print (f"--{nombre}--")
print (f"--{nombre.lstrip()}--")
print (f"--{nombre.rstrip()}--")
print (f"--{nombre.strip()}--")