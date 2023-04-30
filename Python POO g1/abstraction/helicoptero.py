from vehiculo import Vehiculo

class Helicoptero (Vehiculo):
    
    def __init__ (self, nombre:str, color:str, peso:float, 
                  ancho:float, alto:float, num_elices:int,
                  paso_max:float):
        
        self.num_elices = num_elices
        self.paso_max = paso_max
        
        super().__init__ (nombre, color, peso, ancho, alto)
    
    def moverse (self):
        print (f"El helicoptero '{self.nombre}' se movió por el aire")
        
    def detenerse (self):
        print ("El helicoptero arretizó")

if __name__ == "__main__":
    helicoptero_dari = Helicoptero("Helicoptero Dari", "blanco", 1000, 2, 1, 4, 10)
    helicoptero_dari.moverse ()
    helicoptero_dari.detenerse ()