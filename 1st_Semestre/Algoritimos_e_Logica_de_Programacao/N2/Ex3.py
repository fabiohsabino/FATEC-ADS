m = [0]*5

for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = 2**i

for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:2}", end = " ")
    print()
print()