import math
total = 1
count = 0
while total < 10000000:
    num = total
    print str(num) + ":"
    sum = 0
    while(num!=1 and num!=89):
        for i in str(num):
            sum += int(i)**2
        num = sum
        sum = 0
    print num
    if num == 89:
        count+=1
    total += 1
print count
#8581146?
