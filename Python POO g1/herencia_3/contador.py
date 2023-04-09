from empleado import Empleado

class Contador (Empleado):
    
    def __init__ (self, name:str, age:int, salary:float, speciality:str, certs:dict={}):
        
        # Enviar datos originales a clase padre
        super().__init__ (name, age, salary)
        
        # Guardar los nuevos datos
        self.speciality = speciality
        self.certs = certs
        
    def get_speciality (self) -> str:
        """ Retornar la especialidad del contador

        Returns:
            str: area de especialidad
        """
        
        return self.speciality
    
    def set_speciality (self, speciality:str):
        """ Actualizar la especialidad del contador

        Args:
            speciality (str): nueva area de especialidad
        """
        
        self.speciality = speciality
        
    def add_cert (self, name:str, year:int):
        """ Añadir un certificado al contador

        Args:
            name (str): nombre del ceritificado
            year (int): años de validez del certificado
        """
        
        self.certs[name] = year
        
    def get_cert_years (self, name:str) -> int:
        """ Retornar los años de validez de un certificado

        Args:
            name (str): nombre del certificado

        Returns:
            int: años de validez
        """
        
        # Obtener los años de validez del certificado
        years = self.certs[name]
        return years

if __name__ == "__main__":


    gilberto = Contador ("Gilberto", 30, 10_000, "Contabilidad")
    gilberto.set_salary (30_000)
    print (gilberto)
    
    gilberto.add_cert ("CPA", 5)
    gilberto.add_cert ("CIA", 10)
    gilberto.add_cert ("CISA", 15)
    
    print(gilberto.get_cert_years ("CISA"))