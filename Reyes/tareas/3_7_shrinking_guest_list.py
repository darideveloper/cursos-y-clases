

my_guest_list = ['michael angelo','luke jaeger','buckethead','chris storey','rusty cooley',' john petrucci']
print (f'lamento la situacion, pero solo hay mesa para dos personas{my_guest_list[-1]}')
my_guest_list.pop(-1)
print()
print (f'Se cancela la invitacion, solo tengo lugar para dos, lo siento {my_guest_list[0]}')
my_guest_list.pop(0)
print()
print (f'Se cancelo esta mierda, vale verga compa, lo siento {my_guest_list[3]}')
my_guest_list.pop(3)
print()
print (f'se cancelo esto a la verga compa, vale verga a la verga, hasta la proxima {my_guest_list[1]}')
my_guest_list.pop(1)
print()
print (my_guest_list)
print (f'despues de todo este puto perro desmadre, alcanzaste invitacion {my_guest_list[1]}')
#print ({my_guest_list[0]}f'maestro, solo seremos tres, te traes las caguamas')
print (my_guest_list[0] + ' maestro, solo seremos tres, te traes las caguamas')
del my_guest_list[1]
print (my_guest_list)
del my_guest_list[0]
print (my_guest_list)
