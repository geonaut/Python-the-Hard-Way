#initialise some vars
i = 0
numbers = []

while i < 6:
    #print i
    print "At the top i is %d" % i
    #append i
    numbers.append(i)
    #increment i
    i = i + 1
    #print list
    print "Numbers now: ", numbers
    #print incremented value of i (aka number just added to list)
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num