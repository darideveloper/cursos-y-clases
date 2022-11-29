"""
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

1. Start with your program from Exercise 13. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
2. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
3. Print a second set of invitation messages, one for each person who is still in your list.
"""

invitados = ['Ana', 'Pedro', 'Juan']
print ("Estas invitada a mi cena " + invitados[0])
print ("Estas invitado a mi cena " + invitados[1])
print ("Estas invitado a mi cena " + invitados[2])

print ("\nNo pudo asistir " + invitados[-1])
invitados[-1] = 'Maria'

print ("\nEstas invitada a mi cena " + invitados[0])
print ("Estas invitado a mi cena " + invitados[1])
print ("Estas invitada a mi cena " + invitados[2])
