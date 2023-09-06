# Operadores lógicos aritmeticos
10 > 5 # True
10 >= 5 # True
10 < 5 # False
10 <= 5 # False
10 == 5 # False
10 != 5 # True

# Comprar textos
"Ana" == "Maria" # False
"Ana" != "Maria" # True
not "Ana" == "Maria" # True
"ana" in "mariana" # True

# Comprar listas
["Ana", "Maria"] == ["Ana", "Maria"] # True
["Ana", "Maria"] != ["Ana", "Maria"] # False

# Preguntar por valores en listas
nombres = ["Ana", "Maria", "Jose", "Pedro", "Juan"]
"Ana" in nombres # True
"ana" in nombres # False

# Nexos / conciones
# And
if "Ana" in nombres and "Jose" in nombres:
    print ("Todos están")
else:
    print ("Alguno de los nombre no está en la lista")
print ()

# And
if "Ana" in nombres or "Jose" in nombres:
    print ("Alguno de los nombres está en la lista")
else:
    print ("Ninguno de los nombre está en la lista")
