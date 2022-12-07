#prendo un file in input 
#ogni riga è un numero, numeri consecutivi fanno parte dello stesso zaino
#se la riga è vuota, il numero successivo è il primo di un nuovo zaino
#conto il peso di ogni zaino e trovo quello che pesa di più
#stampo il peso del zaino più pesante
import os
file = open("input.txt", "r")
#finchè non arrivo alla fine del file
#leggo una riga
#se la riga è vuota, il numero successivo è il primo di un nuovo zaino
#se la riga non è vuota, il numero è aggiunto al peso del zaino
#se il peso del zaino è maggiore del peso del zaino più pesante, il peso del zaino più pesante diventa il peso del zaino
#stampo il peso del zaino più pesante
maxWeight1 = maxWeight2 = maxWeight3 = 0
weight = 0
zaini = []
while True:
    line = file.readline()
    if not line:
        break
    #se la riga è vuota, il numero successivo è il primo di un nuovo zaino
    if line.isspace():
        zaini.append(weight)
        weight = 0
    #se la riga non è vuota, il numero è aggiunto al peso del zaino
    else:
        weight += int(line)
        #se il peso del zaino è maggiore del peso del zaino più pesante, il peso del zaino più pesante diventa il peso del zaino
        if weight > maxWeight1:
            maxWeight1 = weight
            continue
        #se il peso del zaino è maggiore del peso del secondo zaino più pesante, il peso del secondo zaino più pesante diventa il peso del zaino
        if weight > maxWeight2:
            maxWeight2 = weight
            continue
        #se il peso del zaino è maggiore del peso del terzo zaino più pesante, il peso del terzo zaino più pesante diventa il peso del zaino
        if weight > maxWeight3:
            maxWeight3 = weight
            continue

zaini.sort()
#stampo i primi tre elementi
print(zaini[-1]+zaini[-2]+zaini[-3])
        
#stampo il peso del zaino più pesante
"""print(maxWeight1)
print(maxWeight2)
print(maxWeight3)
print(maxWeight1 + maxWeight2 + maxWeight3)"""