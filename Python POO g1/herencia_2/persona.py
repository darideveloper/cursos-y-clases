import random
from carrera import Carrera

class Persona:
    """ Miembro de la universidad (estudiante o profesor)"""
    
    def __init__ (self, nombre:str, apellido_pat:str, apellido_mat:str, 
                  edad:int, carrera:Carrera, nacionalidad:str, email:str):
        """ Guardar info de la clase Persona

        Args:
            nombre (str): nombre de la persona
            apellido_pat (str): apellido paterno de la persona
            apellido_mat (str): apellido materno de la persona
            edad (int): edad de la persona
            carrera (Carrera): _description_
            nacionalidad (str): nacionalidad de la persona
            email (str): email de contacto
        """
        
        # Guardar variables enviadas por el usuario
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.edad = edad
        self.__carrera__ = carrera
        self.nacionalidad = nacionalidad
        self.email = email
        
        # Calcular matricula: 3 numeros aleatorios màs la edad
        matricula_random = random.randint (100, 999)
        self.__matricula__ = f"{matricula_random}{self.edad}"
        
        # TODO: validar que no se repitan las matriculas
        
    def set_carrera (self, carrera:Carrera):
        """ Actualizar la carrera de la persona
        
        Args:
            carrera (Carrera): instancia de la clase Carrera
        """
                        
        # Validar el tipo de dato
        # if type(carrera) == Carrera: # misma comprobación
        if isinstance (carrera, Carrera): # misma comprobación
            self.__carrera__ = carrera      
        
        # Forzar un error  
        else:            
            raise Exception ("carrera debe ser una instancia de la clase Carrera")
                
    def get_carrera (self) -> Carrera:
        """ Retornar la carrera de la persona

        Returns:
            Carrera: instancia de la clase Carrera
        """
        return self.__carrera__
    
    def __str__ (self):
        """ Convertir a texto la instancia creada con la clase actual y devolverlo

        Returns:
            str: clase como texto
        """
        
        inicial = self.nombre[0].title() + "."
        apellido = self.apellido_pat
        matricula = str(self.__matricula__)
        carrera_nombre = self.__carrera__.nombre
        nacionalidad = self.nacionalidad[0:3].upper()     
        
        return f"{matricula}\tNombre: {inicial} {apellido}\tCarrera: {carrera_nombre}\tNacionalidad: {nacionalidad}"
    
    def update_mat (self, matricula:int):
        pass
    
    def set_edad (self, edad:int):
        pass
    
if __name__ == "__main__":
    
    # Crear la instancia de la clase Carrera
    tics = Carrera("Tics", "9", "ciencias exactas")
    filosofia = Carrera("Filosofia", "8", "humanidades")
    
    # Crear instancias de clase
    alberto = Persona("Alberto", "González", "González", 
                      20, tics, "Mexicana", "alberto@gmail.com")

    # Probar métodos
    print (alberto.get_carrera())
    # alberto.set_carrera ("Biología") # Forzar un error
    print (alberto.get_carrera())
    
    print (alberto)
    
    