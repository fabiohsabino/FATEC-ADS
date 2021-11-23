from random import randint

vet = [0]*5


for i in range(5):
    vet[i] = [0]*5
    for j in range(5):
        vet[i][j] = randint(1, 2)
for i in range(5):
    for j in range(5):
        if j > i:
            print(f"\33[33m{vet[i][j]:2}\33[m",end = " ")
        elif j < i:
            print(f"\33[32m{vet[i][j]:2}\33[m",end = " ")
        else:
            print(f"{vet[i][j]:2}", end = " ")

    print()

sim = True
for i in range (1, 5):
    for j in range (i):
        if (vet[i][j] != vet[j][i]):
            sim = False
            break
if sim:
    print("Matriz Simetrica")
else:
    print("Matriz não simetrica")