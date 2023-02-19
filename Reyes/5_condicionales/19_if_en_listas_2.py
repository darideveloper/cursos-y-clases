# Comprobar que elemento se encuentre en lista / Sistema de pedidos
comidas = ["pizza", "camarones", "hambuergesas", "cerveza", "papas fritas", "alitas"]

pedidos = ["alitas", "papas fritas", "cerveza", "nachos", "nopales"]

for pedido in pedidos:

    if pedido in comidas:
        print (f"Enseguida le traigo su pedido de {pedido}")
    else:
        print (f"Disculpe, ya se nos acabo los {pedido}")
