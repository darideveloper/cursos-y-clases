class Carrera:
    def __init__ (self):
        pass

class Persona:
    """ Miembro de la universidad (estudiante o profesor)"""
    
    def __init__ (self, matricula:int, nombre:str, apellido_pat:str, apellido_mat:str, edad:int, carrera:Carrera, nacionalidad:str, email:str):
        """ Guardar info de la clase Persona

        Args:
            matricula (int): numero de identifiación de la persona
            nombre (str): nombre de la persona
            apellido_pat (str): apellido paterno de la persona
            apellido_mat (str): apellido materno de la persona
            edad (int): edad de la persona
            carrera (Carrera): _description_
            nacionalidad (str): nacionalidad de la persona
            email (str): em,ail de contacto
        """
        self.__matricula__ = matricula
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.edad = edad
        self.__carrera__ = carrera
        self.nacionalidad = nacionalidad
        self.email = email
        
    def set_carrera (self, carrera:Carrera):
        pass
    
    def get_carrera (self):
        return Carrera
        pass
    
    # Explicación pendiente
    def __str__ (self):
        return ""
        pass
    
    def set_mat (self, matricula:int):
        pass