x = 1
top = 0
while x < 9999:
    if 9 == int(x/ (10** (len (str (x))-1))):
        p = 0
        t = 1
        while p < 9:
            cat = ""
            t = t + 1
            for i in range(t):
                cat = cat + str((i+1)*x)
            p = len(cat)
        if p == 9:
            cat = ""
            for i in range(t):
                cat = cat + str((i+1)*x)
            print(x)
            print(cat)
    x += 1
