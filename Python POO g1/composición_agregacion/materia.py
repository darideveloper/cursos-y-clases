class Materia ():
    
    def __init__ (self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        
    def mostrar_datos (self):
        print (f"nombre: {self.nombre}")
        print (f"profesor: {self.profesor}")