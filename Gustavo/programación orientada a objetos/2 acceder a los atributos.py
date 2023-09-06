class Auto ():
    
    def __init__ (self):
        
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.precio = ""
        self.puertas = ""
        
    def arrancar (self):
        
        # Acceder a los atributos desde adentro de la clase
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) arrancó"
        print (mensaje)        
    
    def frenar (self): 
        
        # Acceder a los atributos desde adentro de la clase
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) frenó"
        print (mensaje)
    
auto_nissan = Auto ()

auto_nissan.marca = "Nissan"
auto_nissan.modelo = "Versa"
auto_nissan.color = "Rojo"
auto_nissan.precio = 200000
auto_nissan.puertas = 4

# Consular datos de auto_nissan desde afuera
print (f"La marca del audo es: {auto_nissan.marca}")

auto_nissan.arrancar ()
auto_nissan.frenar ()

# Nueva instancia de clase
auto_ranault = Auto ()

auto_ranault.marca = "ranault"
auto_ranault.modelo = "Clio"
auto_ranault.color = "Blanco"
auto_ranault.precio = 150000
auto_ranault.puertas = 4

# Consular datos de auto_ranault desde afuera
print (f"La marca del audo es: {auto_ranault.marca}")

auto_ranault.arrancar ()
auto_ranault.frenar ()
