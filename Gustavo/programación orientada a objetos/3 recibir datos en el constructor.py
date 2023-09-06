class Auto ():
    
    # Recibiendo datos desde afuera 
    # Con el contructor de la clase
    def __init__ (self, marca:str, modelo:str, color:str, precio:str, puertas:int=4):
        
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.puertas = puertas
        
    def arrancar (self):
        
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) de arrancó"
        print (mensaje)        
    
    def frenar (self): 
        
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) frenó"
        print (mensaje)

# Indicar los atributos al mismo tiempo que se crea la instancia
auto_nissan = Auto ("Nissan", "Versa", "Rojo", 200000, 5)

print (f"La marca del auto es: {auto_nissan.marca}")

auto_nissan.arrancar ()
auto_nissan.frenar ()
