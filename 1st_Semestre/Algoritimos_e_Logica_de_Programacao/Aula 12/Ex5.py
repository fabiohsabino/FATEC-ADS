from random import randint

vet = [0]*5

for i in range(5):
    vet[i] = [0]*5
    for j in range(5):
        vet[i][j] = randint(1, 9)
for i in range(5):
    for j in range(5):
        if i+j>4:
            print(f"\33[33m{vet[i][j]:2}\33[m",end = " ")
        else:
            print(f"{vet[i][j]:2}",end = " ")
    print()