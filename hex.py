rem = []
i = 1
sums = 0
total = 0
while i <= 100000000:
    sums = 0
    for p in rem:
        if i%p[0] == 0:
            sums += p[1]
    if i<= 500:
        rem.append([i, (i)-sums])
    total += sums
    i+=1
print(total*6)
