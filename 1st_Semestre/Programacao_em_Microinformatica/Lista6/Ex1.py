from random import randint

vet = []
impar = 0
par = 0

for i in range(10):
    vet.append(randint(1, 50))
    if vet[i]%2 == 1:
        impar+=1
    else:
        par+=1
print(vet)
print(f"Impar = {impar} | Par = {par}")