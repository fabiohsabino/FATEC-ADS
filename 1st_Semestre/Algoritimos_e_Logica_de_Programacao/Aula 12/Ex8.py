from random import randint

vet = [0]*8

for i in range(8):
    vet[i] = [0]*8
    for j in range(8):
        if (i+j)%2==0:
            vet[i][j] = 0
        else:
            vet[i][j] = 1


for i in range(8):
    for j in range(8):
            print(f"{vet[i][j]:2}",end = " ")
    print()
