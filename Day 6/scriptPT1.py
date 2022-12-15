#open the file
file = open("input.txt", "r")
#read the first line
line = file.readline()
for i in range(len(line)):
    tmp = line[i:i+4]           #14 for the 2nd part
    if len(tmp) < 4:            #14 for the 2nd part
        break
    #check if all the characters in tmp are different by each other
    print(tmp)
    found = True
    for j in range(len(tmp)):
        if tmp[j] in tmp and tmp.find(tmp[j]) != j:
            found = False
            break
    if found:
        print("Found:", tmp, i+4) #14 for the 2nd part
        break