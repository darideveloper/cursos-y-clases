class Jugador():
    
    def moverse (self):
        print ("El jugador se movió")
        
class Zombie ():
    
    def moverse (self):
        print ("El zombie se movió (muy lento)")
        
class Coche ():
    
    def moverse (self):
        print ("El coche se movió (muy rápido)")

class Casa ():
    
    def abrir (self):
        print ("Se abrió la puerta de la casa.")

# Poliformo
def mover_algo (algo:object):
    algo.moverse ()        
   
dari = Jugador ()
carlos = Zombie ()
honda = Coche ()
# cabaña = Casa ()

mover_algo (dari)
mover_algo (carlos)
mover_algo (honda)
# mover_algo (cabaña)