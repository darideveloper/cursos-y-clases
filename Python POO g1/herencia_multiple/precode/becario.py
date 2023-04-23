from empleado import Empleado
from estudiante import Estudiante

class Becario (Empleado, Estudiante):
    def __init__ (self, salario:float, materias:list):
        Empleado.__init__ (self, salario)
        Estudiante.__init__ (self,materias)
        
        
dari = Becario (1000, ['Programación', 'Matemáticas', 'Física'])
print (dari.materias)