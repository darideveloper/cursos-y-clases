
from auto import Auto
from helicoptero import Helicoptero

auto_a = Auto ("auto a", "rojo", 1000, 2, 1, 4, "V8")
auto_b = Auto ("auto b", "azul", 1000, 2, 1, 4, "V8")
auto_c = Auto ("auto c", "verde", 1000, 2, 1, 4, "V8")
helicoptero_a = Helicoptero ("helicoptero a", "blanco", 1000, 2, 1, 4, 10)
helicoptero_b = Helicoptero ("helicoptero b", "blanco", 1000, 2, 1, 4, 10)
helicoptero_c = Helicoptero ("helicoptero c", "blanco", 1000, 2, 1, 4, 10)

def mover_vehiculo (vehiculo:object):
    vehiculo.moverse ()
    
mover_vehiculo (auto_a)
mover_vehiculo (auto_b)
mover_vehiculo (auto_c)
mover_vehiculo (helicoptero_a)
mover_vehiculo (helicoptero_b)
mover_vehiculo (helicoptero_c)