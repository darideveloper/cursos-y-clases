class Estudiante:
    
    # Variable de clase
    escuela = "DariDev"
    contador = 0
        
    def __init__(self, nombre):
        # Atributo o variable de instancia 
        self.name = nombre
        Estudiante.contador += 1

maria = Estudiante("Maria")
pedro = Estudiante("Pedro")
jose = Estudiante("Jose")
alberto = Estudiante("Alberto")

print (maria.escuela)
print (pedro.escuela)
print (jose.escuela)
print (alberto.escuela)

Estudiante.escuela = "DariDev2"

print (maria.escuela)
print (pedro.escuela)
print (jose.escuela)
print (alberto.escuela)

print (maria.contador)
print (pedro.contador)
print (jose.contador)
print (alberto.contador)