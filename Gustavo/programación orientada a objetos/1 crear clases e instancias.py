class Auto ():
    
    # Contructor de la clase
    def __init__ (self):
        
        # Datos / Caracteristicas / Atributos de cada auto
        self.marca = "" # cada auto va a tener marca diferente
        self.modelo = ""
        self.color = ""
        self.precio = ""
        self.puertas = ""
    
    # Método de la clase Auto
    # (cuando tenemos una función dentro de una clase
    #  se le llama método)
    def arrancar (self):
        print ("El auto arrancó")
        
# Crear una instancia / objeto de la clase Auto   
auto_nissan = Auto ()

# Cambiando los valores de los atributos
auto_nissan.marca = "Nissan"
auto_nissan.modelo = "Versa"
auto_nissan.color = "Rojo"
auto_nissan.precio = 200000
auto_nissan.puertas = 4

# Usa el método arrancar
auto_nissan.arrancar ()

# Crear un segundo auto con la misma clase
auto_ford = Auto ()

# Cambiando los valores de los atributos
auto_ford.marca = "Ford"
auto_ford.modelo = "Fiesta"
auto_ford.color = "Azul"
auto_ford.precio = 150000
auto_ford.puertas = 2

# Usa el método arrancar
auto_ford.arrancar ()


