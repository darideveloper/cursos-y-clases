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
        
class Carnivoro (Animal):
    def __init__ (self, periodo_caza:str, hibernacion:str, especie:str, edad:int, tamaño:float, genero:str, alimentacion:list, tipo_alimentacion:str, name:str):
        self.periodo_caza = periodo_caza
        self.hibernacion = hibernacion
                
        super().__init__ (especie, edad, tamaño, genero, alimentacion, tipo_alimentacion, name)
        
    def cazar (self, animal_cazado:str):
        print (f"{self.name} cazó a un(a) {animal_cazado}")        
        
leon_jose = Carnivoro ("todo el año", "diciembre", "leon", 10, 1.9, "m", ["jirafas", "zebras"], "carnivoro", "josé")
leon_jose.correr ()
leon_jose.cazar ("jirafa")
leon_jose.reproducirse ()
leon_jose.morir ()        
    