import time
import requests
from .config import Config
from .ipinfo import get_location
from .mysql import MySQL


class Weather (MySQL):
    
    def __init__ (self, refresh_time:int, lat:float, lon:float):
        """Constructor de la clase

        Args:
            refresh_time (int): Segundos que tardará en actualizarse la base de datos.
            lat (float): ubicación de la desea obtener el clima
            lon (float): ubicación de la desea obtener el clima
        """
            
        # Obtener credenciales
        credentials = Config()
        server = credentials.get ("server")
        database = credentials.get ("database")
        username = credentials.get ("username")
        password = credentials.get ("password")
        
        # Llamar al constructor del padre
        super().__init__ (server, database, username, password)  
        
        # Variables de clase
        self.refresh_time = refresh_time
        self.lat = lat
        self.lon = lon

    def save_weather(self):
        """ Obtener el clima actual de la ciudad del usuario y guardar en base de datos """
                
        # Obtener pikey de credenciales
        credentials = Config()
        apikey_openweather = credentials.get ("apikey_openweather")

        url_openweather = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={apikey_openweather}"
        res = requests.get (url_openweather)
        res.raise_for_status ()
        data = res.json () 
        
        # obtener datos de lluvia
        latitud = data["coord"]["lat"]
        longitud = data["coord"]["lon"]
        clima_nombre = data["weather"][0]["main"]
        clima_descripcion = data["weather"][0]["description"]
        temperatura = data["main"]["temp"] - 273.15
        sensacion_termica = data["main"]["feels_like"] - 273.15
        temperatura_min = data["main"]["temp_min"] - 273.15
        temperatura_max = data["main"]["temp_max"] - 273.15
        presion = data["main"]["pressure"]
        humedad = data["main"]["humidity"]
        nivel_mar = data["main"].get("sea_level", 0) 
        viento_velocidad = data["wind"]["speed"]
        viento_direccion = data["wind"]["deg"]
        viento_resistencia = data["wind"].get("gust", 0) 
        
        # Obtener volumen de lluvia, en caso de que exista
        lluvia = data.get ("rain", {})
        lluvia_volumen = lluvia.get ("1h", 0)
        
        nubosidad = data["clouds"]["all"]
        zona = data["timezone"]
        ciudad = data["name"]
        
       
        # Guardar datos en base de datos
        sql = f""" INSERT INTO registro (latitud, longitud, clima_nombre, clima_descripcion, temperatura, sensacion_termica, temperatura_min, temperatura_max, presion, humedad, nivel_mar, viento_velocidad, viento_direccion, viento_resistencia, lluvia_volumen, nubosidad, zona, ciudad)
            VALUES
            (
                {latitud}, 
                {longitud}, 
                '{clima_nombre}', 
                '{clima_descripcion}',
                {temperatura},
                {sensacion_termica},
                {temperatura_min},
                {temperatura_max},
                {presion},
                {humedad},
                {nivel_mar},
                {viento_velocidad},
                {viento_direccion},
                {viento_resistencia},
                {lluvia_volumen},
                {nubosidad},
                {zona},
                '{ciudad}'
            )
        """
        self.run_sql (sql)

    def auto_save (self):
        """ Guardar el clima cada cierto tiempo """
        
        while True:
            print ("Obteniendo clima...")
            self.save_weather ()
            print ("Clima guardado en base de datos, espero por siguiente actualización...")
            time.sleep (self.refresh_time)
            
    def get_clima (self):
        """ Obtener clima de la base de datos """
        
        sql = "SELECT * FROM registro"
        data = self.run_sql (sql)
        return data
        