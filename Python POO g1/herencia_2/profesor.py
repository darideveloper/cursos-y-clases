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
        """ Retornar el salario actual del profesor

        Returns:
            float: cantidad en dolares que gana el profesor
        """
        
        return self.salario       
    
    def set_salary (self, salary:float):
        """ Actualizar el salario del profesor

        Args:
            salary (float): _description_
        """
        self.salario = salary
                
    
    # Sobreescribir la función __str__ de la clase padre
    def __str__ (self):

        message = super().__str__ () # llamar a la función __str__ de la clase padre     
        
        # añadir información de la clase actual al mensaje   
        message += f"\tSalario: {self.salario}\tNivel de estudios: {self.nivel_estudios}"
        return message
    
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
        10_000, 
        [2,3,4],
        "Doctorado", 
        60
    )
    
    # Comprobar las funciones de la clase padre
    print (juan)
    juan.update_mat ()
    print (juan)

    # Comprobar las funciones de la clase actual
    salario_juan = juan.get_salary () # consultar el salario actual
    print (f"El profesor está ganando {salario_juan} pokedolares al mes")
    juan.set_salary (5_000) # actualizar el salario
    salario_juan = juan.get_salary () # consultar el salario nuevo
    print (f"El profesor está ganando {salario_juan} pokedolares al mes")