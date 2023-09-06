# Importar un archivo entero
import tools

user_name = "    \t\nDar$i\nDeve$lo!pe---r\t"
user_email = "    \t\ndaridevelop--er@g--mail.com\t"

# Limpiar sin funciones
# user_name = user_name.strip().replace("$", "").replace("!", "").replace("\n", " ")
# user_email = user_email.strip().replace("$", "").replace("!", "").replace("\n", " ")

# Limpiar con funciones
user_name = tools.limpiar_texto(user_name)
user_email = tools.limpiar_texto(user_email)

print (user_name, user_email)
    
