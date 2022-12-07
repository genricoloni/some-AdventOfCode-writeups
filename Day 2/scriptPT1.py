file = open("input.txt", "r")
#finchè non arrivo alla fine del file
#leggo una riga
points = 0
while True:
    
    #ogni riga è composta da due numeri separati da un carattere di spazio
    #devo salvarli in due variabili separate
    line = file.readline()
    if not line:
        break
    num1 = line[0]
    num2 = line[2]
    #normalizzo le lettere e faccio in modo che valgano i punti del segno giocato

    #trasformo le lettere in numeri tramite delle sottrazioni
    num1 = ord(num1) - 64
    #a num2 devo sottrarre 'X'
    num2 = ord(num2) - 87
    print(num1, num2)
    


    #aggiungo a prescindere i punti del segno giocato
    points += num2

    #caso del pareggio
    if num1 == num2:
        points += 3
        continue
    #il primo giocatore ha fatto sasso
    if num1 == 1:
        #caso SASSO-CARTA
        if num2 == 2:
            #vittoria
            points += 6
        #caso SASSO-FORBICE
        else:
            #sconfitta, non sottraggo punti
            continue

    #il primo giocatore ha fatto carta
    elif num1 == 2:
        #caso CARTA-FORBICE
        if num2 == 3:
            #vittoria
            points += 6
        #caso CARTA-SASSO
        else:
            #sconfitta, non sottraggo punti
            continue

    #il primo giocatore ha fatto forbice
    elif num1 == 3:
        #caso FORBICE-SASSO
        if num2 == 1:
            #vittoria
            points += 6
        #caso FORBICE-CARTA
        else:
            #sconfitta, non sottraggo punti
            continue

print(points)



