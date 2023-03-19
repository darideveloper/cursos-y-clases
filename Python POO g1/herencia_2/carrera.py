class Carrera:
    def __init__ (self, nombre:str, duracion:int, area:str):
        """ Guardar la información de la carrera y crear el mapa curricular

        Args:
            nombre (str): nombre de la carrera
            duracion (int): duración de la carrera en semestres
            area (str): area de especialida de la cerrera (ejemplo: Ciencia exactos o Humanidades)
        """
        
        # Guardar variables enviadas por el usuario
        self.nombre = nombre
        self.duracion = duracion
        self.area = area
        
        # Inicializar variables de uso interno
        self.__mapa_curricular__ = []
        
    def add_subject (self, nombre_materia):
        """ Agregar una materia al mapa curricular

        Args:
            nombre_materia (str): materia a añadir
        """
        
        # Validar el tipo de dato
        if type(nombre_materia) == str:
            self.__mapa_curricular__.append (nombre_materia)
            
        # Forzar un error
        else:            
            raise Exception ("nombre_materia debe ser un str")
    
    def del_subject (self, nombre_materia:str):
        """ Eliminar una materia al mapa curricular

        Args:
            nombre_materia (str): materia a eliminar
        """        
        
        # Comprobar si la materia existe en el mapa curricular
        if nombre_materia in self.__mapa_curricular__:
            self.__mapa_curricular__.remove (nombre_materia)
            
        # Mostrar un error 'sutil'
        else:
            print (f"Materia {nombre_materia} no encontrada en la carrera {self.nombre}")
            
    def get_subjects (self) -> list:
        """ Retornar el mapa curricular

        Returns:
            list: listado de materias de la carrera
        """
        
        return self.__mapa_curricular__ 
    
    def set_name (self, nombre_carrera:str):
        """ Actualizar el nombre de la cerrera

        Args:
            nombre_carrera (str): nuevo nombre de la carrera
        """
        
        # Validar el tipo de dato
        if type(nombre_carrera) == str:
            self.nombre = nombre_carrera
            
        # Forzar un error
        else:            
            raise Exception ("nombre_carrera debe ser un str")
    
    def __str__ (self) -> str:
        """ Convertir a texto la instancia creada con la clase actual y devolverlo

        Returns:
            str: clase como texto
        """
        
        return f"{self.nombre.upper()} ({self.duracion} semestres - Area: {self.area.title()})"

if __name__ == "__main__":

    # Crear la instancia de la clase Carrera
    tics = Carrera("Tics", "9", "ciencias exactas")
    filosofia = Carrera("Filosofia", "8", "humanidades")

    # Utilizar los métodos de la clase
    tics.add_subject ("fundamentos de programación")
    tics.add_subject ("introducción a redes")
    tics.add_subject ("desarrollo web")

    tics_materias = tics.get_subjects ()
    print (tics_materias)
    tics.del_subject ("redes 2")

    tics_materias = tics.get_subjects ()
    print (tics_materias)

    tics.set_name ("Tecnologias de la Información y Comunicación")

    # Imprimir el objeto
    print (tics) # TICS (9 semestres - Area: Ciencias Exactas)
    print (filosofia) # IFILOSOFIA (8 semestres - Area: Humanidades)
    tics_texto = str(tics) # TICS (9 semestres - Area: Ciencias Exactas)