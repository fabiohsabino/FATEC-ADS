from random import randint

vet =[]
veti = []

for i in range(20):
    vet.append(randint(1,50))
for i in range(19,0,-1):
    veti.append(vet[i])
print(vet)
print(veti)
