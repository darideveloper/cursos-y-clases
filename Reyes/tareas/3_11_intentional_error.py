#If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program

cripto_currencies = ['litecoin', 'monero', 'bitcoin', 'ethereum', 'chainlinktoken', 'chilliz']
#usando len para ver el numero de objetos en mi lista
cripto_actives = len (cripto_currencies)
print (cripto_currencies[100]) # IndexError: list index out of range