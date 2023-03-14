tablero = [
    ["dari 1", "dari 2", "dari 3"], 
    ["dari 4", "dari 5", "dari 6"], 
    ["dari 7", "dari 8", "dari 9"],
]

# consuiltar un elemento (opción A)
fila = tablero[1]
print (fila[1])

# consuiltar un elemento (opción B)
celda = tablero[1][1]
print (celda)
print ()

personajes = [
    # nombre, vida, ataque, defensa, lista de movimientos
    ["pikachu", 50, 70, 30, ["impactruno", "bol voltio"]],
    ["charmander", 40, 90, 20, ["lanzallamas"]],
    ["agumon", 30, 50, 60, ["morder"]],
    ["angewomon", 120, 20, 30, ["viento sagrado", "curar"]],   
    ["goku", 9999, 999, 999, ["kamekameha", "henkidama"]]
]

# Obtener nombre del último personaje
name = personajes[-1][0]
print (name)

# Obtener el primer ataque de agumon
movimiento_agumon = personajes[2][-1][0]
print (movimiento_agumon)

# obtener el último ataque de angewomon
movimiento_angewomon = personajes[3][4][-1]
print (movimiento_angewomon)
print ()

# Recorrer personajes
for personaje in personajes:

    # Obtener los datos por separado
    # nombre = personaje[0]
    # vida = personaje[1]
    # ataque = personaje[2]
    # defensa = personaje[3]
    # movimientos = personaje[4]
    
    # Obteniendo los datos en una sola linea
    nombre, vida, ataque, defensa, movimientos = personaje
    
    print (f"{nombre.upper()}")
    print (f"Estasiticas:")
    print (f"\t* Vida: {vida} puntos")
    print (f"\t* Ataque: {ataque} puntos")
    print (f"\t* Defensa: {defensa} puntos")
    print (f"Movimientos:")
    
    for movimiento in movimientos:
        print (f"\t* {movimiento}")

    print ()