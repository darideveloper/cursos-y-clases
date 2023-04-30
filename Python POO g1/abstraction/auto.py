from vehiculo import Vehiculo

class Auto (Vehiculo):
    
    def __init__ (self, nombre:str, color:str, peso:float, 
                  ancho:float, alto:float, ruedas:int, 
                  motor:str):
        
        super ().__init__ (nombre, color, peso, ancho, alto)
        
        self.ruedas = ruedas
        self.motor = motor
        
    def moverse (self):
        print (f"El auto '{self.nombre}' se movió por el suelo en {self.ruedas} ruedas")
    
    def detenerse (self):
        print ("El auto se detuvo")
    
if __name__ == "__main__":
    nissan = Auto ("auto nissan", "rojo", 1000, 2, 1, 4, "V8")
    nissan.moverse ()
    nissan.detenerse ()