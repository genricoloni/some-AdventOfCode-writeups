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
maxWeight = 0
weight = 0
while True:
    line = file.readline()
    if not line:
        break
    #se la riga è vuota, il numero successivo è il primo di un nuovo zaino
    if line.isspace():
        weight = 0
    #se la riga non è vuota, il numero è aggiunto al peso del zaino
    else:
        weight += int(line)
        #se il peso del zaino è maggiore del peso del zaino più pesante, il peso del zaino più pesante diventa il peso del zaino
        if weight > maxWeight:
            maxWeight = weight
#stampo il peso del zaino più pesante
print(maxWeight)