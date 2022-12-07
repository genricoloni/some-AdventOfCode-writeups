#open input file for input
file = open("input.txt", "r")
tot_prio = 0
#we need to read the file line by line
while True:
    line = file.readline()

    #we reach the end of the file
    if not line:
        break

    #two compartments cointains the same number of elements
    #so we split the line in two lists
    tmp = len(line)//2
    comp1 = line[:tmp]
    comp2 = line[tmp:]

    #we check if a letter is present in both compartments
    for letter in comp1:
        #found the letter
        if letter in comp2:
            if letter.isupper():
                #it's a capital letter so it has a bigger priority than the same lowercase letter
                #the priority is based on the letter: 'a' is 1, 'A' is 27 and so on
                tmp_prio = ord(letter) - 64 +26
            else:
                #it's a lowercase letter
                tmp_prio = ord(letter) - 96
            #we add the priority to the total priority
            tot_prio += tmp_prio
            break

print(tot_prio)
