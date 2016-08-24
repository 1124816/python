import math
place = 2
number = 3
square = 0
loop = 0
while(place <= 10006):
    square = math.sqrt(number)
    loop = 2
    while(loop<=square):
        if(number%loop==0):
            break
        loop += 1
    else:
        print str(place) + ": " + str(number)
        place +=1
    number += 2
