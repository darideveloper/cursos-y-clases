from materia import Materia

class Estudiante ():
    
    def __init__(self, name:str, age:int, nombre_mat:str, nombre_prof:str):
        self.name = name
        self.age = age
        
        self.materia = Materia (nombre_mat, nombre_prof)
        
    def mostrar_datos (self):
        print (f"nombre: {self.name}")
        print (f"nombre: {self.age}")

victor = Estudiante ("Victor", 20, "Programación", "Juan")
victor.materia.mostrar_datos()