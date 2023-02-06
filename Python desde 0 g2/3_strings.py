nombre = "josÉ lOPEZ hernANDez" # Texto obtenido de una base de datos

# Cases
nombre_mayusculas = nombre.upper() # Mayusculas con variable = José Lopez Hernandez
print (nombre_mayusculas)
print (nombre.upper()) # mayusculas sin variable = José Lopez Hernandez
print (nombre.lower()) # minusculas = josé lopez hernandez
print (nombre.title()) # titulo = José Lopez Hernandez
print ()

# Concatenar / unir textos
nombre = "dari"
apellido = "developer"
nombre_completo = nombre + " " + apellido
print (nombre_completo) # dari developer

# Concatenar / unir textos (f-strings)
nombre = "dari"
apellido = "developer"
nombre_completo = f"{nombre} {apellido}"
print (nombre_completo)
print ()

# Combinar operaciones
mensaje = "Bienvenido usuario: " # mensaje con espacio en blanco
nombre = "dari"
apellido = "developer"
print (mensaje + apellido.upper()) # Bienvenido usuario: DEVELOPER
print ()

# Caracteres espciales / caracteres en blanco
print ("Me gusta programar\nen python")
print ("Me gusta programar\ten python")
print ("M\ne gusta\n prog\t\t\tramar\ten pyt\t\thon")
print ()

# Quirtar espacios en blanco
nombre_1 = "\njosÉ lOPEZ hernANDez\t\n" # Texto obtenido de una base de datos
nombre_2 = "     josÉ lOPEZ hernANDez     " # Texto obtenido de una base de datos
print("*" + nombre_1 + "*")
print("*" + nombre_1.rstrip () + "*") # quitar espaciados a la derecha
print("*" + nombre_1.lstrip () + "*") # quitar espaciados a la izquierda
print("*" + nombre_1.strip () + "*") # quitar espaciados a la derecha e izquierda
print("*" + nombre_2 + "*")
print("*" + nombre_2.rstrip () + "*") # quitar espaciados a la derecha
print("*" + nombre_2.lstrip () + "*") # quitar espaciados a la izquierda
print("*" + nombre_2.strip () + "*") # quitar espaciados a la derecha e izquierda
print ()

# Tipos de comillas
nombre = "juan" # commillas dobles
nombre = 'juan' # comillas simples
nombre = """juan""" # triple comillas / triple comilla doble

# Usar comillas dobles DENTRO del texto
cita = '"La estupidez de lahumanidad es infinita" - Albert Eaitsain'
print (cita)

# Usar comillas simples DENTRO del texto
cita = "'La estupidez de lahumanidad es infinita' - Albert Eaitsain'"
print (cita)

# Usar comillas simple y dobles DENTRO del texto
cita = """'La estupidez de lahumanidad es infinita' - "Albert Eaitsain" """
print (cita)

# Texto multilinea
parrafo = """jnhbasdjvsadjhdsaJVHDAS
hgasdghjfdsa
JGASGFDGHASD
JHGSAGDHHAGSDHGDSADSA
    JHEFHGFSAD
JHSADDFGJHSDFÇ
JHDSFHJFD
HSAADAJSHD
usdcg   jknddfvjk"""
print (parrafo)