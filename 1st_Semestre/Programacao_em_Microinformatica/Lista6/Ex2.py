from random import randint

vet = []
vpar = []
par = 0
soma = 0
media = 0


for i in range(20):
    vet.append(randint(1, 50))
    if vet[i]%2 == 0:
        vpar.append(vet[i])
        soma+=(vet[i])

media = soma/(len(vpar))

print(vet)
print(f"O total de numeros pares é {len(vpar)} e a media deles é {media}")
        