from random import randint

vet = [0]*5

for i in range(5):
    vet[i] = [0]*5
    for j in range(5):
        if i == 0 or j == 0:
            vet[i][j]=0
        elif i == 1:
            vet[i][j] = j
        elif i == 2:
            vet[i][j] = j*2
        elif i == 3:
            vet[i][j] = j*3
        else:
            vet[i][j] = j*4

for i in range(5):
    for j in range(5):
            print(f"{vet[i][j]:2}",end = " ")
    print()