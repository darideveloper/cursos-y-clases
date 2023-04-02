from persona import Persona
from carrera import Carrera

class Profesor (Persona):
    
    def __init__ (self, nombre:str, apellido_pat:str, apellido_mat:str, 
                  edad:int, carrera:Carrera, nacionalidad:str, email:str,
                  salario:float, grados:list, nivel_estudios:str, horas_semana:float):
        
        # Enviar datos originales a clase padre
        super().__init__ (nombre, apellido_pat, apellido_mat, 
                          edad, carrera, nacionalidad, email, "Profesor")
        
        # Guardar datos de la clase
        self.salario = salario
        self.grados = grados
        self.nivel_estudios = nivel_estudios
        self.horas_semana = horas_semana
    
    def get_salary (self) -> float:
        pass
    
    def set_salary (self, salary:float):
        pass
    
    # def __str__ (self):
    #     pass
    
if __name__ == "__main__":
    
    tics = Carrera("Tics", "9", "ciencias exactas")
    
    juan = Profesor (
        "Juan", 
        "Perez", 
        "Garcia", 
        30, 
        tics, 
        "Mexicana", 
        "juan@gmail.com", 
        10000, 
        [2,3,4],
        "Doctorado", 
        60
    )
    print (juan)
    juan.update_mat ()
    print (juan)