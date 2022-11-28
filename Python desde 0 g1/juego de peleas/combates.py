import random
from personajes_data import personajes

personajes_nombres = list(personajes.keys())

def obtener_personaje_random (): 
    """ Obtiene un personaje aleatorio de la lista de personajes

    Returns:
        str: nombre de un personaje
    """
    
    # Seleccionar personaje de la lista de nombres
    personaje_seleccionado = random.choice (personajes_nombres)
    
    # Eliminar personaje seleccionado de la lista de nombres
    personajes_nombres.remove (personaje_seleccionado)
    
    # Devolver personaje seleccionado
    return personaje_seleccionado

def movimiento (nombre_jugador:str, personaje_ataque:str, personaje_defensor:str):
    """ Realiza un movimiento de un personaje atacante a uno defensor

    Args:
        nombre_jugador (str): nombre del jugador en el turno actual
        personaje_ataque (str): nombre del personaje del jugador
        personaje_defensor (str): nombre del personaje del oponente

    Returns:
        bool: indicador si el combate ya terminó (False) o sigue en curso (True)
    """
    
    print (f"\nJugador {nombre_jugador} ({personaje_ataque}):")
    while True:
                
        print ("¿Que desea hacer? \n1. Atacar \n2. Defender \n3. Descansar")
        opcion = input ()
        
        # Obtener estadisticas
        estadisticas_atacante = personajes[personaje_ataque]
        estadisticas_defensor = personajes[personaje_defensor]
        
        if opcion == "1":
            
            # Calcular dañó al enemigo
            estadisticas_defensor["vida"] -= estadisticas_atacante["ataque"]
            
            # Mostrar estatus del combate
            print (f"El personaje {personaje_ataque} atacó a {personaje_defensor}")
            print (f"Vida de {personaje_defensor} después del ataque: {estadisticas_defensor['vida']}")
            
            # obtener vida de los personajes
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
            
            # Incrementar vida
            estadisticas_atacante["vida"] += 25
            
            # Mostrar estatus del combate
            print (f"El personaje {personaje_ataque} descansó para recuperarse")
            print (f"Vida de {personaje_ataque} después del descanso: {estadisticas_atacante['vida']}")
            
        else:
            print ("Opcion invalida. Vuelve a intentar\n")
            continue
        
        break
    
def combate ():
    """ Ciclo principal de batalla para dos jugadores  """
    
    # Solicitar nombres y asginar personajes
    jugadores = []
    personajes = []
    for jugador_index in range(1, 3): 
        
        jugadores.append (input (f"Jugador {jugador_index}: "))
        personajes.append (obtener_personaje_random())
        print (f"Personaje asignado: {personajes[-1]}")

    # Ciclo de combate
    while True:
        continuar_combate = movimiento (jugadores[0], personajes[0], personajes[1])
        if continuar_combate == False:
            break
        
        continuar_combate = movimiento (jugadores[1], personajes[1], personajes[0])
        if continuar_combate == False:
            break
        
    # TODO: Mostrar resumen de combate