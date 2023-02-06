# Crear "plano" en base al que se harán los estudiante
class Estudiante ():
    
    # Constructor de clase
    def __init__ (self, nombre:str, matricula:str, apellido:str, edad:int, password:str):
        """ Constructor de clases

        Args:
            Args:
            nombre (str): nombre del estudiante
            matricula (str): matricula del estudiante
            apellido (str): apellido paterno del estudiante
            edad (int): edad delestudiante
        """
        
        # Crear los atributos de la clase, para compartilos con el rtesto de métodos
        self.nombre = nombre
        self.matricula = matricula
        self.apellido = apellido
        self.edad = edad
        
        # Crear unatributo "privado"
        self.__password__ = password
        
    def get_password (self):
        """ Devolver un atributo privado
        Returns:
            str: contraseña del usuario
        """
        return self.__password__
    
    def set_password (self, new_password):
        """ Actualizar atributo privado

        Args:
            new_password (str): contraseña
        """
        
        # Verificar que la contrseña sea segura
        # ...
        
        self.__password__ = new_password

    def mostrar_nombre (self):
        """ Imprimir nombre del estudiantes
        """
        print (f"El nombre del estudiantes: {self.nombre}")
    
    def mostrar_matricula (self):
        """ Imprimir matricula del estudiante
        """
        print (f"La matricula del estudiante es: {self.matricula}")
        
# Crear instanca / objeto / un algo de / en base a la Estudiante
estudiante_dari = Estudiante("dari", "d123456", "dev", 29, "12345")
estudiante_garra = Estudiante("garra", "g123456", "est", 53, "6789")

# Utilizar métodos de clase
estudiante_dari.mostrar_matricula ()
estudiante_garra.mostrar_matricula ()
print ()

# Acceder directamente a los atributos de la instancia / objeto
mat = estudiante_dari.matricula
estudiante_dari.matricula = "nueva123456"
print ()

# (encapsulamiento)
# Utilizar métodos para consultar y actualizar atributos privados 
print(estudiante_dari.get_password())



