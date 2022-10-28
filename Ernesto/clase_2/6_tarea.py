"""
La siguiente información se ha obtenido de una base de datos, por lo quen no la puedes modificar directamente.
Con la listad e usuarios, realiza lo siguiente: 
1. Crea una copia de las listas de usuarios, donde ningún elemento tenga texto adicional
2. Imprime un mensaje de bienvenida a cada usuario, asegurandote de no imprimir texto en blanco y que la primer letra de cada nombre esté en mayúscula
3. Añade a la lista de usuarios el usuario "admin" al inicio de la lista.
4. Elimina a "juan" de la lista de usuarios.
5. Copiar todos los usuarios a una nueva lista llamada "usuarios_sorted", donde los usuarios estén ordenados alfabéticamente.
6. Imprime el número de usuarios que hay en la lista.
7. Crear una nueva lista, llamada "contraseñas", donde cada usuario tenga una contraseña asociada.
8. Imprime la contraseña que corresponde al usuario "josé" 
"""

usuarios = [" juan ", "  josé ", "  maria", "jorge "]

usuarios_nuevo = []
for usuario in usuarios:
    # usuario_title = usuario.title()
    # usuarios_title.append (usuario_title)
    
    # 1.
    usuario_limpio = usuario.strip()
    usuarios_nuevo.append (usuario_limpio)
    
    
# 2.
for usuario in usuarios_nuevo:
    print (f"Bienvenido usuario: {usuario.title()}")

# Crear lista de contraseñas
print (usuarios_nuevo)
constraseñas = ['1234', '5678', '9123', '0000']

# Mostrar contraseña de un usuario
index_jose = usuarios_nuevo.index("alberto")
contraseña_jose = constraseñas[index_jose]
print (contraseña_jose)

# for usuario in usuarios:
#  2. Añade a la lista de usuarios el usuario "admin" al inicio de la lista.#nuevo_usuario = usuarios[:]#nuevo_usuario.append("Admin")#print(nuevo_usuario)
#  3. Elimina a "juan" de la lista de usuarios.#del usuarios[0]
# print(usuarios)
# 4. Copiar todos los usuarios a una nueva lista llamada "usuarios_sorted", donde los usuarios estén ordenados alfabéticamente.
# usuarios_sorted.sort()#usuarios_sorted.string()#print(usuarios_sorted)
# usuarios_sorted = usuarios
# 5. Imprime el número de usuarios que hay en la lista.#print(len(usuarios))
# 6. Crear una nueva lista, llamada "contraseñas", donde cada usuario tenga una contraseña asociada.contrasenas = []for usuario in usuarios:
