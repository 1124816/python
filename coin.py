import math
c = 2
sumProb = 0
sumTie = 1
while sumProb < .95:
    x = c
    p = x
    sumProb = 0
    while x > 0:
        y = x
        while y > 0:
            y-=1
            sumProb+= .60000**x*.40000**(p-x)*.50000**p*(math.factorial(p)/math.factorial(p-y))/math.factorial(y)*(math.factorial(p)/math.factorial(p-x))/math.factorial(x)
        #print(sumProb)
        x-=1
    
    sumTie = 0
    x = c
    p = x
    while x>=0:
        sumTie += .6**(x)*.4**(p-x)*.5**(p)*((math.factorial(p)/math.factorial(p-x))/math.factorial(x))**2
        x-=1
    sumTie = 1-sumTie
    print(str(c)+' : '+str(sumProb))
    c+=1
