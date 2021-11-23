from random import randint

vet = [0]*4
cont = 0
mes = [0]*12
cm = 0
vet2 = []

for i in range(4):
    vet[i] = [0]*12
    for j in range(12):
        vet[i][j] = randint(1, 70)


for i in range(12):
    mes[i] = [0]*4
    cm = 0
    for j in range(4):
        mes[i][j] = vet[j][i]
        cm += mes[i][j]
    vet2.append(cm)
        

for i in range(4):
    for j in range(12):
            cont+=vet[i][j]
            print(f"{vet[i][j]:2}",end = " ")   
    print()
print()
for i in range(12):
    for j in range(4):
            
            print(f"{vet2}",end = " ")   
    print()
print()
print(f"Total de peças produzidas no mês = {mes}")
print(f"Total de peças produzidas no ano = {cont}")
