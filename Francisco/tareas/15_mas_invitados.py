"""
You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

1. Start with your program from Exercise 14 or Exercise 13.
2. Add a print statement to the end of your program informing people that you found a bigger dinner table.
3. Use insert() to add one new guest to the beginning of your list.
4. Use insert() to add one new guest to the middle of your list.
5. Use append() to add one new guest to the end of your list.
6. Print a new set of invitation messages, one for each person in your list

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

print ("\nEncontré una mesa mas grande, voy a invitar a mas personas")

invitados.insert (0, 'Fernando')
invitados.insert (2, 'Dari')
invitados.append ('Ricardo')

print ("\nEstas invitado a mi cena " + invitados[0])
print ("Estas invitada a mi cena " + invitados[1])
print ("Estas invitado a mi cena " + invitados[2])
print ("Estas invitado a mi cena " + invitados[3])
print ("Estas invitada a mi cena " + invitados[4])
print ("Estas invitado a mi cena " + invitados[5])



