def enviar_correo ():
    """ Función para enviar un correo electrónico """
    
    # Solicitar datos
    email_to = input ("Destinatario: ")
    email_text = input ("Texto: ")
    email_from = input ("Correo de origin: ")
    
    # Enviar
    print (f"Enviando correo '{email_text}', al email {email_to}, desde el correo: {email_from}")

def registrar_usuario ():
    """ Función para registrar un usuario """
    
    # Solicitar datos generales
    input ("Nombre: ")
    input ("Edad: ")
    
    # Solicitar el tipo de usuario
    print ("Elige un tipo de usuario: ")
    print ("1. Estandar")
    print ("2. Admin")
    
    # Leer opción del usuario
    user_type = input ()
    
    if user_type == "1":
        usuario_tipo = "estandar"
    else:
        usuario_tipo = "admin"
    
    # regitsrar usuario
    print (f"Usuario registrado exitosamente, tipo {usuario_tipo}")


# Menu básico de opciones
running = True
while running:
    
    # Menu principal
    print ("\nElige una opción: ")
    print ("1. Enviar correo")
    print ("2. Registrar usuario")
    print ("3. Salir")
    
    # Leer opción del usuario
    user_option = input ()
    
    if user_option == "1":
        enviar_correo ()    
    elif user_option == "2":
        registrar_usuario ()        
    elif user_option == "3":
        running = False
    else:
        print ("Entrada incorrecta, intente de nuevo...")