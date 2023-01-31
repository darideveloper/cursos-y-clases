
soup = jhasjhsadjhsad
mis_elementos = soup.select ("h1.hola.mundo")
elementos_terminados = []

for elem in mis_elementos:
    
    # Extraer datos:
    print (elem.getText())
    
    # Gurdar elemento atual en lista de terminados
    elementos_terminados.append (elem)



