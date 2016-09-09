import time
start = time.time()
total = 1
count = 0
mlist = []
o = 0
while total < 100000:
    num = total
    print num
    if(num in mlist):
        print "success"
        count += 1
        mlist.append(num)
    else:
        print "fail"
        sum = 0
        o = num
        while(num!=1 and num!=89):
            for i in str(num):
                sum += int(i)**2
            num = sum
            sum = 0
        print num
        if num == 89:
            count+=1
            mlist.append(o)
    total += 1
print count
print mlist
print time.time() - start
