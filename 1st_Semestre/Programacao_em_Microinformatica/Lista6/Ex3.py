from random import randint

vet = []
vetm = []

for i in range(20):
    vet.append(randint(1,50))
    if vet[i]%5 == 0:
        vetm.append(vet[i])
    
print(vet)
print(vetm)