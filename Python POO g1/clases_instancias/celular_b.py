class Celular:
    """ Clase para crear celulares de diferentes marcas """
        
    def __init__ (self, screen_size, battery, camara, wight, price, model, brand):
        """ constructor de clase para crear los atributos """
        self.screen_size = screen_size
        self.battery = battery
        self.camara = camara
        self.wight = wight
        self.price = price
        self.model = model
        self.brand = brand        
        
    def describe (self): 
        """ Mostrar caractersricas del celular """
               
        print (f"Soy un smartphone de la marca {self.brand} y modelo {self.model}")
        print (f'tamaño de pantalla: {self.screen_size}"')
        
    def take_picture (self):
        """ Tomar una foto y guardarla en el pc """
        print ("Foto tomada con éxito")
        
    def install_app (self, app_name:str):
        """ instalar una aplicación desde la tienda

        Args:
            app_name (str): nombre de la aplicación a instalar
        """
        print (f"La aplicación {app_name} se instaló exitosamente")
    
    def call (self, phone:int=911):
        """ LLamar a un numero de telefono

        Args:
            phone (int, optional): numero de telefono a llamar. Defaults to 911.
        """
        print (f"El numero {phone} no contesta")
    
    def message (self, phone:int, message:str):
        """ Enviar mensaje de texto 

        Args:
            phone (int): numero que recibirá el mensaje
            message (str): texto del mensaje
        """
        print (f"Mensaje enviado a {phone}")

# Crear instancia de celular, con atributos
# iphone13 = Celular(6.8, 6000, 40, 150, 20000, "phone 13", "apple")
iphone13 = Celular(
    screen_size=6.8, 
    battery=6000, 
    camara=40, 
    wight=150,
    price=20000,
    model="phone 13", 
    brand="apple"
)

# actualizar una atributo
iphone13.screen_size = 6.79

# acceder a un dato de la clase
camara_iphone = iphone13.camara
print ("Camara: " + str(camara_iphone) + "mpx")


# Utilizar los métodos del celular
print ("----------------------")
iphone13.describe ()
print ("----------------------")
iphone13.take_picture ()
iphone13.install_app ("Tinder")
iphone13.call ()
iphone13.call (7295162572)
iphone13.message (7295162572, "Hola mundo")
