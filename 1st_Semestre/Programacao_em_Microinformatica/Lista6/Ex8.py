from random import randint

veta = []
vetb = []
vetc = []

for i in range(20):
    veta.append(randint(1,50))
    if veta[i]%2 == 0:
        vetb.append(veta[i])
    else:
        vetc.append(veta[i])
print(veta)
print(f"Pares = {vetb}")
print(f"Impares = {vetc}")