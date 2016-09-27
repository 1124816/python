import time
start = time.time()
def codeCha2(limit):
    sumsq = [sum((0 * 0,))] + [None] * limit

    for i in xrange(1 + limit):
        sumsq[i] = (i % 10) ** 2 + sumsq[i // 10]


    #1 or 89.
    all_down = False
    while not all_down:
        all_down, eighty_nines = True, 0
        for i in xrange(1, 1 + limit):
            if sumsq[i] == 1:
                pass
            elif sumsq[i] == 89:
                eighty_nines += 1
            else:
                all_down = False
                sumsq[i] = sumsq[sumsq[i]]
    return eighty_nines


print codeCha2(162)
print time.time() - start
