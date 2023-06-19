# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# Mensaje de que se acabo el pastrami para el sandwich.
print ("¡Sorry!, We run out of pastrami.\n")

sandwich_orders = ['atun', 'pastrami', 'tocino', 'pastrami', 'pollo', 'mortadella', 'pastrami', 'aceitunas'] #lista de ordenes
finished_sandwich_orders = [] #lista de ordenes terminadas

# removiendo el elemento 'pastrami' de lista de ordenes usando un buble while.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_orders = sandwich_orders.pop()
    #moviendo cada orden de sandwich termianda a la lista vacia de ordenes finalizadas.
    print (f"I made your {finished_orders} sandwich")
    finished_sandwich_orders.append(finished_orders)
# recorriendo con bucle For la nueva lista de ordenes finalizadas y mostrar cada orden en pantalla
print ("\nI confirm each sandwich that was made:")
for finished in finished_sandwich_orders:
    print (finished.title())   
