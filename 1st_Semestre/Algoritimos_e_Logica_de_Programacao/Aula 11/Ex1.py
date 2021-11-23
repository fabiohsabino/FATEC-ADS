from random import randint

vet = []
vetb = []

for i in range(20):
    vet.append(randint(1,50))
print(vet)
for i in range(10):
    vet[i],vet[i+10] = vet[i+10],vet[i]
print(vet)
