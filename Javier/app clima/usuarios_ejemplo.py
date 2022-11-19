from servicios.usuario import Usuario

user_manager = Usuario()
login_done = user_manager.login ("javi", "12345")
if login_done:
    print ("Usuario logeado")
else:
    print ("Usuario o contraseña incorrectos")
    
user_created = user_manager.singup ('daridev2', "darideveloper2@gmail.com", '00000')
if user_created:
    print ("Usuario creado exisamente")
else:
    print ("No se pudo crear el usuario")