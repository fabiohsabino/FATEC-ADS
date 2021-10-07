from random import randint

vet = []

for i in range(10):
    vet.append(randint(1,50))
print(vet)
vet.sort(reverse=False)
print(vet)
