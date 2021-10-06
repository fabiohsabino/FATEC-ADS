from random import randint

vet = [10]
maior = 0
menor = 101

for i in range(10):
    vet.append(randint(1, 100))
    if vet[i]>maior:
        maior = vet[i]
    if vet[i] < menor:
        menor = vet[i]

print(vet)
print(f"Maior Numero = {maior} | Menor numero = {menor}")