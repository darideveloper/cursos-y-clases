# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

#Start with your program from Exercise 3-4 or Exercise 3-5. 
# Add a print statement to the end of your program informing people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list. 
# Use insert() to add one new guest to the middle of your list. 
# Use append() to add one new guest to the end of your list. 
# Print a new set of invitation messages, one for each person in your list.

# Lista de invitados y mensaje de invitacion
my_guest_list = ['luke gaeger', 'chris storey', 'shawn lane']
mensaje_invitacion = ' estás invitad@ a mi comida'

# Imprimir primer set de invitaciones
print (my_guest_list[0] + mensaje_invitacion)
print (my_guest_list[1] + mensaje_invitacion)   
print (my_guest_list[2] + mensaje_invitacion)

# Indicar que un invitado no puede asistir
print("\n" + my_guest_list[1] + ' cancelo, tengo nuevo invitado a la cena')

# Remplzar invitado de mi lista
my_guest_list[2] = 'rusty cooley'

# Imprimir set de invitaciones
print ("\nLos nuevos invitados son:")
print (my_guest_list[0] + mensaje_invitacion)
print (my_guest_list[1] + mensaje_invitacion)
print (my_guest_list[2] + mensaje_invitacion)

# Avisar que tenemos mesa mas grande
print ("\nSeñores, me confirman que tenemos mesa mas grande, osea, tendremos mas invitados")

# Agregar invitados
my_guest_list.insert (0, 'michael angelo')
my_guest_list.insert (2, 'buckethead')
my_guest_list.append ('john petrucci')

# Imprimir set de invitaciones
print ("\nLos nuevos invitados son:")
print (my_guest_list[0] + mensaje_invitacion)
print (my_guest_list[1] + mensaje_invitacion)
print (my_guest_list[2] + mensaje_invitacion)
print (my_guest_list[3] + mensaje_invitacion)
print (my_guest_list[4] + mensaje_invitacion)
print (my_guest_list[5] + mensaje_invitacion)

# ------------------------------


# my_guest_list = ['luke jaeger','chris storey','rusty cooley']
# my_guest_list.insert (0, 'michael angelo')
# my_guest_list.insert (2, 'buckethead')
# my_guest_list.append ('john petrucci')
# print(my_guest_list)

# print ('hey ' + my_guest_list[1] + ' tenemos nueva banda en la mesa')
# print()
# print ('bienvenido ' + my_guest_list[0])
# print()
# print (my_guest_list[3] + ' se viene toda la pandilla')
# print()
# print (my_guest_list[2] + ' bienvenido, saca las chelas, culo')
# print()
# print (my_guest_list[4] + ' te traes las chelas, que te estamos esperando puto')
# print()
# print ('ohhh, que hombre tal elegante, pase usted, señor ' + my_guest_list[5])
# print()
# print('correccion, nos quitaron la mesa y solo podre invitar a dos personas, puta madre')