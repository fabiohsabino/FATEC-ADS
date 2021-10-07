from random import randint

vet = []
vetm = []
num = int(input("Digite um numero: "))

for i in range(20):
    vet.append(randint(1,50))
    if vet[i]%num == 0:
        vetm.append(vet[i])
    
print(vet)
print(vetm)
