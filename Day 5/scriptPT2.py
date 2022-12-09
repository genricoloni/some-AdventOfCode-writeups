file = open("input.txt", "r")

while True:
    #reaad the file until we found a line with numbers
    line = file.readline()
    if not line:
        break
    if line[1].isdigit():
        break
#we found the number of crates
crates = max(line.split())

print("Number of crates:", crates)

#crate of crates
CoC = [[] for i in range(int(crates))]
#read the file again
file = open("input.txt", "r")  
line = file.readline()


while True:
    for i in range(1,len(line), 4):
        #0->pos 1, 5->pos 2, 9->pos 3 and so on
        n = i//4
        if line[i].isalpha():
            CoC[n].append(line[i])
    line = file.readline()
    if not line or line[1].isdigit():
        break

#reverse the crates
for i in range(len(CoC)):
    CoC[i].reverse()
for i in range(len(CoC)):
    print(CoC[i])

#we have the crates of crates
#let's start the game reading line with the moves

line = file.readline()
print(line)
while True:
    line = file.readline()
    if not line:
        break
    #the line is formed by "move q from s to d"
    #we need to know q, s and d
    #q could be formed by 1 o 2 numbers
    #s and d are always 1 number
    #we need to know the position of the first space
    #and the position of the second space 
    if line[6] == " ":
        q = int(line[5])
        s = line[12]
        d = line[17]

    else:
        q = int(line[5:7])
        s = line[13]
        d = line[18]
    print("q:", q, "s:", s, "d:", d)

    tmp = []

    for i in range(q):
        #move i elements from crate s to create d
        tmp.append(CoC[int(s)-1].pop())
        #print the crates
    for i in range(q):
        CoC[int(d)-1] += tmp.pop()
    for i in range(len(CoC)):
        print(CoC[i])
    print("\n")

    

#print the crates
for i in range(len(CoC)):
    print(CoC[i])

#print the lasts elements of the crates
for i in range(len(CoC)):
    CoC[i].reverse()
    print(CoC[i][0])  



