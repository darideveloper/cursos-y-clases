class Empleado ():
    
    def __init__ (self, name:str, age:int, salary:float):
        self.name = name
        self.age = age
        self.salary = salary
    
    def get_salary (self) -> float:
        """ Retornar el salario actual del empleado

        Returns:
            float: cantidad en dolares que gana el empleado
        """
        
        return self.salary       
    
    def set_salary (self, salary:float):
        """ Actualizar el salario del empleado

        Args:
            salary (float): _description_
        """
        self.salary = salary

    def __str__ (self):
        """ Convertir a texto la instancia creada con la clase actual y devolverlo
        """
        
        return f"Nombre: {self.name} - Edad: {self.age} - Salario: {self.salary}"

if __name__ == "__main__":

    emmanuel = Empleado ("Emmanuel", 30, 10_000)
    print (emmanuel)