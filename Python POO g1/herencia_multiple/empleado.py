class Empleado ():

    def set_salary (self, salary:float):
        """ Guardar salario del empleado

        Args:
            salary (float): _description_
        """
        self.salary = salary

    def cobrar_salario (self):
        print (f"El empleado cobró {self.salary} pokedolares")

if __name__ == "__main__":
    carlos = Empleado ()
    carlos.set_salary (10_000)
    carlos.cobrar_salario ()