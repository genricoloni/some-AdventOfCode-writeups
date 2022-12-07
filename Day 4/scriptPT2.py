#open input file for input
file = open("input.txt", "r")
count = 0
#we need to read the file line by line
i = 0
while True:
    line = file.readline()


    #we reach the end of the file
    if not line:
        break

    #we split the line in two lists
    couple1, couple2 = line.split(",")

    #let's found the head and the tail of the ranges+
    #a couple is divided by a '-'
    #the head is the first number of the couple
    #the tail is the second number of the couple
    head1, tail1 = couple1.split("-")
    head2, tail2 = couple2.split("-")

    #we have to check if one of the range is totally or partially inside the other one
    firstrange = range(int(head1), int(tail1)+1)
    secondrange = range(int(head2), int(tail2)+1)
    if (set(firstrange).intersection(secondrange)) or (set(secondrange).intersection(firstrange)):
        count += 1
print(count)