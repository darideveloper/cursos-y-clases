# Comprobar la edad e imprimir un mensaje
edad = 150

if edad < 10:
    print ("Eres un niño")
elif edad < 18:
    print ("Eres un adolescente")
elif edad < 50:
    print ("Eres un adulto")
elif edad < 100:
    print ("Eres un anciano")
else:
    print ("Eres un fantasma")

print ("Final del programa")

# Similar un inicio de sesión

# Consultando usuarios de la DB
users_db = ["daridev", "dari", "dariel", "darieldev"]

# Leer datos de inicio de sesión
user = "daridev"
password = "1234dari123*+"

# Comprobar el nombre de usuario
if user in users_db:
    
    # Obtener contraseña del usuario actual
    password_db = "1234dari123*+"
    
    # Comprobar contraseña
    if password == password_db:
        print ("Bienvenido")
    else:
        print ("Usuario o contraseña incorrectos")
        
else:
    print ("Usuario o contraseña incorrectos")
