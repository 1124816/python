import math
place = 2
number = 3
square = 0
loop = 0
while(place <= 200000):
    square = math.sqrt(number)
    loop = 3
    while(loop<=square):
        if(number%loop==0):
            break
        loop += 2
    else:
        print str(place) + ": " + str(number)
        place +=1
    number += 2
