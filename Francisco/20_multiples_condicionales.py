# Tablas de verdad
# and - ambos verdadderos
# or - cualquiera verdaddero
# not - opuesto

# Ejemplo de and 
logged = True
tipo_usuario = "admin"
estatus = "inactivo"

if (logged) and (tipo_usuario == "admin") and (estatus == "activo"):
    print ("Bienvenido usuario administrador")        
else:
    print ("No tienes permiso para acceder a este contenido")
    
# # Ejemplo de or
# cuenta_chaques = 100
# cuenta_ahorro = 200
# cantidad_retirar = 150

# if cuenta_chaques >= cantidad_retirar:
#     print ("Aqui está tu dinero")
# else:
#     print ("")
