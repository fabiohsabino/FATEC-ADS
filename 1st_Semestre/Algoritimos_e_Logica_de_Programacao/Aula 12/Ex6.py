from random import randint

vet = [0]*4

for i in range(4):
    vet[i] = [0]*6
    for j in range(5):
        vet[i][j] = randint(1, 9)

for i in range(4):
    for j in range(6):
            print(f"{vet[i][j]:2}",end = " ")   
    print()

print()

for i in range(6):
    for j in range(4):
        print(f"{vet[j][i]:2}", end = " ")
    print()