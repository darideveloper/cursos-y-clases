
# Solicitar entrada al usuario
maximo = int(input ("Cuentos elementos: "))

# Contador de simbolos
contador = 1

maximo_encontrado = False

while contador > 0:
    
    # Imprimir simbolo
    print ("*"*contador)
    
    if contador == maximo:
        maximo_encontrado = True
        
    # Incrementar o decrementar contador
    if not maximo_encontrado:
        contador += 1
    else: 
        contador -= 1
        
# Ciclo for
# alumnos = ["pamela", "luis", "alberto"]
# for alumno in alumnos:
#     print (alumnos)
    

