from random import randint

vet = []
num = int(input("Digite um valor: "))
cont = 0

for i in range(10):
    vet.append(randint(1,50))
for i in range(10):
    if vet[i] == num:
        cont+=1
print(vet)
if cont == 0:
    print("Numero não encontrado!")
else:
    print(f"Numero encontrado {cont}x")