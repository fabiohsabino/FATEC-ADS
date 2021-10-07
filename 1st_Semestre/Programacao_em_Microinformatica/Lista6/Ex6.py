from random import randint, vonmisesvariate

veta =[]
vetb = []
x = int(input("Digite um numero: "))

for i in range(20):
    veta.append(randint(1,50))
    vetb.append(veta[i]*x)

print(veta)
print(vetb)
