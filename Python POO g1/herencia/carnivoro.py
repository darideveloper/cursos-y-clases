from animal import Animal

class Carnivoro (Animal):
    def __init__ (self, periodo_caza:str, hibernacion:str, especie:str, edad:int, tamaño:float, genero:str, alimentacion:list, tipo_alimentacion:str, name:str):
        self.periodo_caza = periodo_caza
        self.hibernacion = hibernacion
                
        super().__init__ (especie, edad, tamaño, genero, alimentacion, tipo_alimentacion, name)
        
    def cazar (self, animal_cazado:str):
        print (f"{self.name} cazó a un(a) {animal_cazado}")