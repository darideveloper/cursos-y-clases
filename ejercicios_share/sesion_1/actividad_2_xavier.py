"""
If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

# print ("\n Dari Dev")

invitados = [
    "martín",
    "xavier",
    "vladimir",
    "Heber", 
    "Alberto",
    "Lyriz",
]

# Imprimir set de invitados
for invitado in invitados:
    print(f"{invitado.title()} estás invitado...") 

"""
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.

Acabas de escuchar que uno de tus invitados no puede asistir a la cena, por lo que debes enviar un nuevo conjunto de invitaciones.
Tendrás que pensar en alguien más para invitar.
1. Start with your program from above. 1. Comience con su programa desde arriba.

2. Add a print statement at the end of your program stating the name of the guest who can’t make it.
2. Agregue una declaración impresa al final de su programa que indique el nombre del invitado que no puede asistir.

3. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
3. Modifique su lista, reemplazando el nombre del invitado que no puede asistir con el nombre de la nueva persona que está invitando.

4. Print a second set of invitation messages, one for each person who is still in your list.

4. Imprima un segundo conjunto de mensajes de invitación, uno para cada persona que todavía está en su lista.
"""
# se ve en la terminal el resultado del bucle que hice

print(f"{invitados.pop(0)} no puede asistir")

invitados.insert(0, "Gran Dari Superyayin")

print("//////////////////////////////////")
for invitado in invitados:
    print(f"{invitado.title()} estás invitado...") 



