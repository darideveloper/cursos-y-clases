class Auto ():
    
    def __init__ (self, marca:str, modelo:str, color:str, precio:str, puertas:int=4):
        """ Guardar datos del auto

        Args:
            marca (str): marca/fabricante del auto
            modelo (str): modelo del auto
            color (str): color del auto
            precio (str): precio del auto
            puertas (int, optional): Numero de puertas. Defaults to 4.
        """
        
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.puertas = puertas
        
    def arrancar (self):
        """ Arrancar el auto
        """
        
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) de arrancó"
        print (mensaje)        
    
    def frenar (self): 
        """ Frenar el auto
        """
        
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) frenó"
        print (mensaje)