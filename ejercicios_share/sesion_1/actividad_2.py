"""
If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

print ("\n Dari Dev")

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
1. Start with your program from above. 1. Comience con su programa desde arriba.

2. Add a print statement at the end of your program stating the name of the guest who can’t make it.
2. Agregue una declaración impresa al final de su programa que indique el nombre del invitado que no puede asistir.

3. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
3. Modifique su lista, reemplazando el nombre del invitado que no puede asistir con el nombre de la nueva persona que está invitando.

4. Print a second set of invitation messages, one for each person who is still in your list.

4. Imprima un segundo conjunto de mensajes de invitación, uno para cada persona que todavía está en su lista.
"""
# se ve en la terminal el resultado del bucle que hice

print("\n Martin")

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
    print(f"{invitado[0]} no puede asistir")

# -------------------------------------

print("\n Alberto")

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

# Quien no viene
noviene=invitados[2]
print("\n\n"+noviene+" no vendra al gran opening") 

invitados.pop(2)
invitados.append('juan')

for invitado in invitados:
    print(f"{invitado.title()} nueva invitacion...") 

# -------------------------------------

print("\n Jenny")

invitados=[
    "José",
    "Esteban",
    "Antonio",
    "Paulo",
    "ELENA",
    "Consuelo"
]

for invitado in invitados:
    print(f"{invitado.title()} estas invitado...")

print("\nLo siento, " + "Maria" + " No podrá asistir.") 

# -------------------------------------

print("\n Heber")

invitados = [
    "martín",
    "xavier",
    "vladimir",
    "Heber", 
    "Alberto",
    "Lyriz",
]

for invitado in invitados:
    print(f"{invitado.title()} estas invitado...")
       
novienen = invitados[3]

print(f"{novienen} no viene al evento")

del invitados[3]
invitados.append("Lorenzo")

# -------------------------------------

print("\n Dari Dev")

invitados=[
    "José",
    "Esteban",
    "Antonio",
    "Paulo",
    "ELENA",
    "Consuelo"
]

# Mostrar lista de invitados
print ("Invitaciones: ")
for invitado in invitados:
    print(f"\t{invitado.title()} estas invitado...")
    
# Remplazar a un invitado
delete_invitado = invitados[2]
print (f"\n{delete_invitado} no podrá asistir")
invitados[2] = "Joshua"

# Mostrar (otra vez) lista de invitados
print ("\nInvitaciones: ")
for invitado in invitados:
    print(f"\t{invitado.title()} estas invitado...")


"""
Start with your program above 
1. Add a print statement to the end of your program informing people that you found a bigger dinner table.
2. Use insert() to add one new guest to the beginning of your list.
3. Use insert() to add one new guest to the middle of your list.
4. Use append() to add one new guest to the end of your list.
4. Print a new set of invitation messages, one for each person in your list.
"""