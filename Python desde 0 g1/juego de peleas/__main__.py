import random

# Personajes
# TODO: precisión, tipo
personajes = {
    "Togepi": {
        "vida": 120,
        "ataque": 20,
    },
    "Snake": {
        "vida": 80,
        "ataque": 25,
    },
    "Falcon": {
        "vida": 100,
        "ataque": 15,
    },
    "Jyglipoff": {
        "vida": 115,
        "ataque": 30,
    },
}

personajes_nombres = list(personajes.keys())

def obtener_personaje_random (): 
    # TODO: no repetir personaje
    personaje_seleccionado = random.choice (personajes_nombres)
    return personaje_seleccionado

def movimiento (nombre_jugador:str, personaje_ataque:str, personaje_defensor:str):
    
    print (f"\nJugador {nombre_jugador} ({personaje_ataque}):")
    while True:
                
        print ("¿Que desea hacer? \n1. Atacar \n2. Defender \n3. Descansar")
        opcion = input ()
        if opcion == "1":
            
            # Obtener estadisticas
            estadisticas_atacante = personajes[personaje_ataque]
            estadisticas_defensor = personajes[personaje_defensor]
            
            # Calcular dañó al enemigo
            estadisticas_defensor["vida"] -= estadisticas_atacante["ataque"]
            
            # Mostrar estatus del combate
            print (f"El personaje {personaje_ataque} atacó a {personaje_defensor}")
            print (f"Vida de {personaje_defensor} después del ataque: {estadisticas_defensor['vida']}")
            
            # obtener vida de los personajes
            vida_atacante = estadisticas_atacante["vida"]
            vida_defensor = estadisticas_defensor["vida"]
            if vida_defensor <= 0:
                print (f"Combate terminado. Ganador: {nombre_jugador}")           
                return False
            else:
                return True
            
        elif opcion == "2":
            # TODO: Implementar defensa
            print ("Defendiendo")
        elif opcion == "3":
            # TODO: Implementar descanso
            print ("No hacer nada")
        else:
            print ("Opcion invalida. Vuelve a intentar\n")
            continue
        
        break
    
def main ():
    # Asignar personajes a jugadores
    personaje_1 = obtener_personaje_random()
    personaje_2 = obtener_personaje_random()
    
    # TODO: Solicitar nombres de usuarios

    # Ciclo de combate
    while True:
        # TODO: restructurar
        continuar_combate = movimiento ("Juan", personaje_1, personaje_2)
        if continuar_combate == False:
            break
        
        continuar_combate = movimiento ("Maria", personaje_2, personaje_1)
        if continuar_combate == False:
            break
        
    # TODO: Mostrar resumen de combate
        
main ()
    
        
   
        
    
    

# Calculo de daño