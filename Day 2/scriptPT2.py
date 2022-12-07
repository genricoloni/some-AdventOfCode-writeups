file = open("input.txt", "r")
#finchè non arrivo alla fine del file
#leggo una riga
points = 0
while True:
    line = file.readline()
    if not line:
        break
    opp = line[0]
    res = line[2]
    

    opp = ord(opp) - 64

    #caso di sconfitta
    if res == 'X':
        # SASSO
        if opp == 1:
            #perdo con forbice
            #aggiungo solo i punti del segno giocato
            points += 3
            continue
        # CARTA
        elif opp == 2:
            #perdo con sasso
            #aggiungo solo i punti del segno giocato
            points += 1
            continue
        # FORBICE
        else:
            #perdo con carta
            #aggiungo solo i punti del segno giocato
            points += 2
            continue
    
    #caso di pareggio
    elif res == 'Y':
        # SASSO
        if opp == 1:
            #pareggio con sasso
            #aggiungo i punti del segno giocato e 3 punti
            points += 3+1
            continue
        # CARTA
        elif opp == 2:
            #pareggio con carta
            #aggiungo i punti del segno giocato e 3 punti
            points += 3+2
            continue
        # FORBICE
        else:
            #pareggio con forbice
            #aggiungo i punti del segno giocato e 3 punti
            points += 3+3
            continue
        #Caso di vittoria
    else:
            # SASSO
        if opp == 1:
            #vittoria con carta
            #aggiungo i punti del segno giocato e 6 punti
            points += 2+6
            continue
            # CARTA
        elif opp == 2:
                #vittoria con forbice
                #aggiungo i punti del segno giocato e 6 punti
            points += 3+6
            continue
            # FORBICE
        else:
                #vittoria con sasso
                #aggiungo i punti del segno giocato e 6 punti
            points += 1+6
            continue

print(points)
