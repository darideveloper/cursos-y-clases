#Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

cripto_currencies = ['litecoin', 'monero', 'bitcoin', 'ethereum', 'chainlinktoken', 'chilliz']
#usando len para ver el numero de objetos en mi lista
cripto_actives = len (cripto_currencies)
print (f"mi portafolio de criptoactivos esta compuesto por {cripto_actives} tokens")
print()
#ordenadas alfabeticamente y de forma temporal
print(f"mis monedas son: {sorted(cripto_currencies)}, ordenadas alfabeticamente")
print (cripto_currencies)
print()
#ordenadas alfebeticamente y permanentemente
cripto_currencies.sort()
print (cripto_currencies)
print()
#ordenadas afabeticamente y permanentemente en orden inverso
cripto_currencies.sort (reverse=True)
print (cripto_currencies)
print()
#invirtiendo el orden de la lista
cripto_currencies.reverse()
print (cripto_currencies)
print()
#revirtiendo el orden
cripto_currencies.reverse()
print (cripto_currencies)