# Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['atun', 'tocino', 'pollo', 'mortadella'] #lista con ordenes de diferentes sandwiches por hacer.
finished_sandwich_orders = [] #lista vacia para confirmar las ordenes de sandwich terminadas.
# removiendo cada orden de sandwich de la lista de ordenes, hasta que no quede ni una orden.

while sandwich_orders:
    
    finished_orders = sandwich_orders.pop()
    
    #moviendo cada orden de sandwich termianda a la lista vacia de ordenes finalizadas.
    print (f"I made your {finished_orders} sandwich")
    finished_sandwich_orders.append(finished_orders)
    
# recorriendo con bucle For la nueva lista de ordenes finalizadas y mostrar cada orden en pantalla
print ("\nI confirm each sandwich that was made:")
for finished in finished_sandwich_orders:
    print (finished.title())        