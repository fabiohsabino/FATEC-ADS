from random import randint

vet = [0]*5

for i in range(5):
    vet[i] = [0]*5
    for j in range(5):
        if i==j or i+j == 4:
            vet[i][j] = 1
        else:
            vet[i][j] = 0


for i in range(5):
    for j in range(5):
        if i==j or i+j == 4:
            print(f"\33[33m{vet[i][j]:2}\33[m",end = " ")
        else:
            print(f"{vet[i][j]:2}",end = " ")
    print()