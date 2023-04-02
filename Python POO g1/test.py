class ClaseA:
    
    contador = 0
        
    def __init__(self, x):
        self.contador += 1
        self.x = x
        
instancia_1 = ClaseA(1)
instancia_2 = ClaseA(1)
instancia_3 = ClaseA(1)
instancia_4 = ClaseA(1)
print (ClaseA.contador)