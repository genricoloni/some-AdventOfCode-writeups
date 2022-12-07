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

    #we have to check if one of the two ranges is inside the other
    #if the head of the first range is inside the second range
    #or the head of the second range is inside the first range
    #then the two ranges are overlapping
    if ((int(head1) >= int(head2) and int(tail1) <= int(tail2))) or ((int(head2) >= int(head1) and int(tail2) <= int(tail1))):
        count += 1
print(count)

