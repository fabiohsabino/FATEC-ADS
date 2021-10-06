from random import randint

vet = []
par = []
impar = []

for i in range(20):
    vet.append(randint(1, 100))
    if vet[i]%2 == 0:
        par.append(vet[i])
    else:
        impar.append(vet[i])
print(vet)
print(par)
print(impar)