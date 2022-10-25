# STRINGS

# Cases
print ("")
print ("Cases: ")
name = "ernestO MArtineZ"
print (name)
print (name.lower())
print (name.upper())
print (name.title())

# Concatenar
print ("")
print ("Concatenar: ")
name = "ernesto"
last_name = "martinez"
full_name = name.title() + " " + last_name.title()

# Concatenar place holders (f string)
print ("")
print ("Concatenar place holders (f string): ")
full_name = f"Hola, Usuario {name.title()} {last_name.title()}"
print (full_name)

# Quotes
print ("")
print ("Quotes: ")
name = "ernesto"
print (name)
name = 'ernesto'
print (name)
name = """ernesto"""
print (name)

quote = '"Dos cosas me inspiran asombro: los cielos estrellados en lo alto y el universo moral interior" - Albert aistain'
print (quote)

texto = "today's  monady"
print (texto)

texto_2 = """ "Dos cosas me inspiran asombro: los cielos estrellados en lo alto y el universo moral interior" - Albert aistain today's  monady """
print (texto_2)

# Comilla triple para formatear texto
print ("")
print ("Comilla triple para formatear texto: ")
saludo = """Hola, me llamo Dari, 
       ¿Cómo te llamas tu?"""
print (saludo)

# Strip
print ("")
print ("Strip: ")
email = "   darideveloper@gmail.com   "
print (f"'{email}'")
print (f"'{email.lstrip()}'")
print (f"'{email.rstrip()}'")
print (f"'{email.strip()}'")