from empleado import Empleado
from estudiante import Estudiante

class Becario (Empleado, Estudiante):
    
    def __init__ (self, salary:float, materias:list):
        """ Constructor de la clase, que recibe el salario y las materias

        Args:
            salary (float): salario del becario
            materias (list): materias que cursa el becario
        """
        
        # Forma B: no utilizar los constructores
        self.set_salary (salary)
        super ().__init__ (materias)
        
        self.cobrar_salario ()
        self.mostrar_materias ()
        
hatfune = Becario(2_000, ["Matemáticas", "Física", "Química"])