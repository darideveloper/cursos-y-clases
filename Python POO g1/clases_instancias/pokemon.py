class Pokemon:
    
    def __init__ (self, nombre:str, ataque:int, vida:int):
        """ Contructor de clase

        Args:
            nombre (str): nombre del pokemon
            ataque (int): ataque del pokemon
            vida (int): vida del pokemon
        """
        self.nombre = nombre
        self.ataque = ataque
        self.__vida__ = vida
    
    def atacar (self):
        """ Atacar a otros pokemon
        """
        print (f"{self.nombre} atacó e hizo un daño de {self.ataque}")
    
    def defender (self):
        """ Defenderse de un ataque
        """
        print (f"{self.nombre} ha defendido este turno")
    
    def ganar_vida (self, vida_extra:int):
        """ Aumentar la vida de un pokemon

        Args:
            vida_extra (int): puntos de vida adicionales
        """
        print (f"{self.nombre} ganó {vida_extra} puntos de vida")
    
    def perder_vida (self, vida_perdida:int):
        print (f"{self.nombre} perdió {vida_perdida} puntos de vida")
    
    def debilitarse (self):
        print (f"{self.nombre} se quedó sin puntos de vida")
        
        
pikachu = Pokemon("pikachu", 10, 40)
charmander = Pokemon("charmander", 12, 30)

pikachu.atacar()
charmander.atacar()