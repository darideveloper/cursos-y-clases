from abc import ABC, abstractmethod

class Vehiculo (ABC): # Decir que es una clase abstracta
    def __init__ (self, nombre:str, color:str, peso:float, 
                  ancho:float, alto:float):
        """_summary_

        Args:
            nombre (str): _description_
            color (str): _description_
            peso (float): _description_
            ancho (float): _description_
            alto (float): _description_
        """
        
        self.nombre = nombre
        self.color = color
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    
    # Declaramos que este método debe "redefinirse" en la clase hija
    @abstractmethod
    def moverse (self):
        pass
    
    @abstractmethod
    def detenerse (self):
        pass