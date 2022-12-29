my_guest_list = ['michael angelo','luke jaeger','buckethead','chris storey','rusty cooley',' john petrucci']

# Sublistas (desde : hasta antes de)
print(my_guest_list[0:3]) # ['michael angelo', 'luke jaeger', 'buckethead']
print(my_guest_list[1:4]) # ['luke jaeger', 'buckethead', 'chris storey']
print(my_guest_list[:3]) # ['michael angelo', 'luke jaeger', 'buckethead']
print(my_guest_list[0:-1]) # ['michael angelo', 'luke jaeger', 'buckethead', 'chris storey', 'rusty cooley']
print(my_guest_list[4:]) # ['rusty cooley', ' john petrucci']
print ()

# Ejemplo de copiar variables de Str
# nombre = "Dari"
# nombre_copia = nombre # Dari
# nombre_copia += " Developer" # Dari Developer
# print (nombre)
# print (nombre_copia)

# Copiar listas
comidas = ["pizza", "hamburgesas", "enchiladas", "camarones", "chilaquiles"]
comidas_2 = comidas[:]
comidas_2[0] = "cuernitos"

print (comidas)
print (comidas_2)
print ()

# Recorrer una sublista
for comida in comidas[1:4]:
    print (comida)

