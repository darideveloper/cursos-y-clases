import time
from threading import Thread
from servicios.openweather import Weather
from servicios.ipinfo import get_location


# Localicación de ejemplo
tiempo_actualizacion = 10
lat = 19.4579
lon = -99.1223

# Crear construcor de clase con clima de ejemplo
# clima = Weather (tiempo_actualizacion, lat, lon)

# obtener locaclización mediante ip
lat, lon = get_location ()
clima = Weather (tiempo_actualizacion, lat, lon)

# Ejecutar función que actualiza clima automáticamente
auto_save_thread = Thread (target = clima.auto_save)
auto_save_thread.start ()

# Obtener datos del clima
time.sleep (5)
data = clima.get_clima ()
print (data)
