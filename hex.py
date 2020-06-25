rem = {}
i = 1
sums = 0
total = 0
while i <= 10000:
    sums = 0
    lowest = 0
    for p in rem:
        if i%p == 0:
            sums += rem[p][0]
            if lowest == 0:
                lowest = p
            for e in rem[p][1]:
                if i%e == 0:
                    sums += rem[p][1][e][0]
    if i<= 5000:
        if lowest == 0:
            rem[i] = [(i)-sums, {}]
        else:
            rem[lowest][1][i] = [(i)-sums]
    total += sums
    i+=1
print(total*6)
