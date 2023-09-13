class Auto ():
    
    def __init__ (self, marca:str, modelo:str, color:str, precio:str, puertas:int=4):
        """ Guardar datos del auto

        Args:
            marca (str): marca/fabricante del auto
            modelo (str): modelo del auto
            color (str): color del auto
            precio (str): precio del auto
            puertas (int, optional): Numero de puertas. Defaults to 4.
        """
        
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.puertas = puertas
        
    def arrancar (self):
        """ Arrancar el auto
        """
        
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) de arrancó"
        print (mensaje)        
    
    def frenar (self): 
        """ Frenar el auto
        """
        
        mensaje = f"El auto {self.marca} {self.modelo} ({self.color.lower()}) frenó"
        print (mensaje)
        
    def get_info (self) -> dict:
        """ Resume la infomación del auto

        Returns:
            dict: datos del audo
            
            {
                "marca": str,
                "modelo": str,
                "color": str,
                "precio": int,
                "puertas": int
            }
        """
        
        # Crear diccionario
        data = {
            "marca": self.marca,
            "modelo": self.modelo,
            "color": self.color,
            "precio": self.precio,
            "puertas": self.puertas
        }
        
        # Devolver diccionario
        return data
    
    def get_info_text (self) -> str:
        """ Resume la infomación del autoy la devuelve como texto

        Returns:
            str: parrafo de texto con los datos del auto
        """
        
        # Llamar a la función dentro de la clase
        info = self.get_info ()

        # Formatear datos
        text = ""
        for item, value in info.items ():
            text += f"{item} {value}, "
        
        # Devolver texto
        return text

    
auto1 = Auto("Nissan", "Versa", "Rojo", 200000, 4)

# llamar a la función que devuelve datos, fuera de clase
info_auto1 = auto1.get_info_text ()
print (info_auto1)