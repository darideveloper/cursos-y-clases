usuarios = ["Maria", "Pedro", "José"]

# for usuario in usuarios:
#     print (f"Hola usuario {usuario}")

while usuarios:
    
    # Imprimir usuario
    print (f"Hola usuario {usuarios[0]}")
    
    # Eliminar usuario de la lista
    usuarios.pop(0)