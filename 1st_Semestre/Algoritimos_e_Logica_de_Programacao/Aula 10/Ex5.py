from random import randint

vet = []
num = int(input("Digite um numero: "))
cont = 0

for i in range(10):
    vet.append(randint(1,10))
for i in range(10):
    if vet[i] == num:
        cont += 1
print(vet)
print(f"{num} foi encontrado {cont}x")