
# Comprobar que elemento se encuentre en lista / Sistema de pedidos
comidas = ["pizza", "camarones", "hambuergesas", "cerveza", "papas fritas", "alitas"]

pedido = "ALITAS"

if pedido.lower() in comidas:
    print ("Enseguida le traigo su pedido\n")
else:
    print ("Disculpe, ya se nos acabó esa madre\n")

# Comprobar que elementos no se encuentre en lista / Sistema de baneos
usuarios_bloqueados = ["dari", "reyes", "josé", "miguelito"]
usuario = "dari"
if usuario not in usuarios_bloqueados:
    print ("Bienvenido\n")
    
# Comprobar si una lista tiene contenido o está vacía / carrito de compras
items_carrito = []

if items_carrito:
    print ("el carrito tiene cosas\n")
else:
    print ("el carrito está vacío\n")
