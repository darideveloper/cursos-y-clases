# Informacion de una taqueria sobre su menu
# listas dentro de un diccionario
# ofreciendo el menu a clientes
# tomando el pedido a los clientes para su elaboracion
tacos = {
    'tortillas': ['harina', 'maiz'],
    'carnes': ['arabe', 'pastor'],
    'salsas': ['habanero', 'extra hot'],
}
#imprimiendo el menu para las ordenes posibles
print ('¡Que tal! ¿de que quiere sus tacos?')
for carne in tacos['carnes']:
    print (f'Tenemos de carne {carne}')

print ('\n¿Que tortilla quiere para sus tacos?')
for tortilla in tacos['tortillas']:
    print (f'¿{tortilla}?')

print ('\n¿Con que salsa?')
for salsa in tacos['salsas']:
    print (f'tenemos {salsa}')    
#lista de ordenes de los clientes   
ordenes = {
    'cliente_1': ['arabe', 'maiz', 'habanero'],
    'cliente_2': ['pastor', 'harina', 'extra hot'],
    'cliente_3': ['arabe', 'harina', 'extra hot']
}
print ('\n¡Salen estas ordenes para los clientes!, que son las siguientes:')
#ciclos for anidados para recorrer el diccinario y las listas dentro del mismo.
for cliente, orden in ordenes.items():
    print (f'\nLa orden del {cliente} es:') #impresion del cliente, recorriendo cada cliente en el diccionario.
    for orden in orden: #recorriendo cada orden del cliente
        print (f'{orden}')
        
print ("\n¡Al momento tenemos sus ordenes!, gracias por la espera.")        

items = {
    "casa": ["vaso", "jarra", "mascota"],
    "bosque": ["espada maldta", "escudo de madera", "armadura de cuero"],
    "camino": ["persona", "señal"]
}