#listas dentro de listas
tipos_datos = [
    ['texto', 'string', 'cadenas'],
    [6, 5, 4, [1.1, 2.2, 3.2,]], #una lista dentro de otra lista
    [True, False],
    [float, int],
]
print ()
#accediendo a un elemento dentro de la lista
lista1 = tipos_datos[1] #sobreescribiendo la variable para acceder al elemento de enmedio
print (lista1)
print (lista1[3]) #de esta sublista accedemos al dato de esa lista
#forma simplificada
print (tipos_datos[1]) #accediendo a un elemento dentro de la lista
print (tipos_datos[1][3]) #accediendo a un elemento dentro de una sublista
print (tipos_datos[1][3][2]) #accediendo a un elemento de una lista dentro de una sublista de la lista
print ()
fighters = [
    # nombre, grappling, striking, special, 
    ['jones', 'wrestling', 'muay thai', ['elbows', 'guillotine']],
    ['poirier', 'jiu jitsu', 'boxing', ['resistance', 'sibmission']],
    ['chandler', 'wrestling', 'kickboxing', ['ko power', 'body punch']],
]

#recorriendo, usando ciclos for
for fighter in fighters:
    #print (fighter) # recorriendo todos los elementos de la lista
    # obteniendo los datos por separado
    name = fighter[0]
    grappling = fighter[1]
    striking = fighter[2]
    specials = fighter[3] 

# obteniendo los datos en una sola linea
    name, grappling, striking, specials = fighter
    print (f'{name.title()}')
    print (f'estadistics:')
    print (f'\t* grappling: {grappling}')
    print (f'\t* striking: {striking}')
    print (f'specials:')
    # ciclo FOR anidado dentro de otro ciclo FOR para acceder a cada uno de los elementos de la lista que esta dentro de la sublista.
    for special in specials:
        print (f'\t* {special}')
        
    print ()    
