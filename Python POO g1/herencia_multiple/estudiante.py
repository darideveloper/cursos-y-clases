class Estudiante ():
    def __init__ (self, materias:list):
        """ Contructor de la clase estudiante

        Args:
            materias (list): lista de materias que cursa actualmente el estudiante
        """
        self.materias = materias
        
    def mostrar_materias (self):
        """ Mostrar las materias que cursa el estudiante
        """
        print ("Las materias son: ")
        for materia in self.materias:
            print (f"\t{materia}")

if __name__ == "__main__":
    materias = ["Matemáticas", "Física", "Química"]
    dario = Estudiante (materias)
    dario.mostrar_materias ()