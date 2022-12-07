#open input file for input
file = open("input.txt", "r")
tot_prio = 0
#we need to read three lines at a time
while True:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

    #we reached the end of the file
    if not line1 or not line2 or not line3:
        break

    #check for every letter in the first line if it's present in the second and third line
    for letter in line1:
        if letter in line2 and letter in line3:
            if letter.isupper():
                tmp_prio = ord(letter) - 64 +26
            else:
                tmp_prio = ord(letter) - 96
            tot_prio += tmp_prio
            break

print(tot_prio)
