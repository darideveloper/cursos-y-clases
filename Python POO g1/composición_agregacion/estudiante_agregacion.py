from materia import Materia

class Estudiante ():
    
    def __init__(self, name:str, age:int, materia:Materia):
        self.name = name
        self.age = age
        self.materia = materia
        
    def mostrar_datos (self):
        print (f"nombre: {self.name}")
        print (f"nombre: {self.age}")

poo2 = Materia ("POO 2", "Dari Developer")
redes = Materia ("Redes", "Abel Soto")

victor = Estudiante ("Victor", 20, redes)
victor.materia.mostrar_datos()