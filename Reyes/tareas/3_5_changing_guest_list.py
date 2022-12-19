# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

#Start with your program from Exercise 3-4. 
# Add a print statement at the end of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

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

# Imprimir primer set de invitaciones
print ("\nLos neevos invitados son:")
print (my_guest_list[0] + mensaje_invitacion)
print (my_guest_list[1] + mensaje_invitacion)
print (my_guest_list[2] + mensaje_invitacion)

# # ------------------------------

# my_guest_list = ['luke jaeger','chris storey','shawn lane']

# print(my_guest_list[0] + ' te confirmo la invitacion y el nuevo invitado')
# print(my_guest_list[1] + ' shawn cancelo, tengo nuevo invitado a la cena')
# print('bienvenido a la cena, maestro ' + my_guest_list[2])

# print('señores, me confirman que tenemos mesa mas grande, osea, tendremos mas invitados')
