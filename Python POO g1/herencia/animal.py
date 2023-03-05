class Animal:
    def __init__ (self, especie:str, edad:int, tamaño:float, genero:str, alimentacion:list, tipo_alimentacion:str, name:str):
        self.especie = especie
        self.edad = edad
        self.tamaño = tamaño
        self.genero = genero
        self.alimentacion = alimentacion
        self.tipo_alimentacion = tipo_alimentacion
        self.name = name
        
    def caminar (self):
        print (f"{self.name} caminó")
    
    def comer (self):
        print (f"{self.name} comió")
    
    def correr (self):
        print (f"{self.name} corrió")
    
    def reproducirse (self):
        print (f"{self.name} se reprodujo")
    
    def morir (self):
        print (f"{self.name} se murió")
    