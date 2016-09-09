import time
start = time.time()
count = 0
total = 1
while total < 100000:
    num = total
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
print time.time() - start
