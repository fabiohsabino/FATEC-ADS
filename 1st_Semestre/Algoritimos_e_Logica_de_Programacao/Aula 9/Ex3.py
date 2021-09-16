S = 2
i=1
print("S = ", end=' ')
for cont in range(1,10):
    print(f"2^{i} + ", end = ' ')
    S += 2**i
    i+=1
S += 2**10
print(f"2^10 ")
print(f"= {S}")