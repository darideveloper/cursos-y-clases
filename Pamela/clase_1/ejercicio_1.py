var1 = "hola" # String
var2 = 12 # Int
var3 = 12.7 # Float
var4 = True # Boolan (si, no)

text = "P@#yn26atˆ&i5ve666ghjogb??!@"

contador_letras = 0
contador_numeros = 0
contador_especiales = 0

for letra in text:

    if letra.isnumeric():
        contador_numeros += 1
    elif letra.isalpha():
        contador_letras += 1
    else:
        contador_especiales += 1

print (f"Cantidad de letras: {contador_letras}")
print (f"Cantidad de numeros: {contador_numeros}")
print (f"Cantidad de caracteres especiales: {contador_especiales}")