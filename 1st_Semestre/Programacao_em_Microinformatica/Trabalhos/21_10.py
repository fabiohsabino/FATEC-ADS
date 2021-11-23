from random import randint

dado = []
qtde = [0,0,0,0,0,0]

for i in range(10):
    dado.append(randint(1,6))
print(f"Numeros Sorteados: {dado}")
for i in range(10):
    if dado[i]==1:
        qtde[0] += 1
    elif dado[i]==2:
        qtde[1] += 1
    elif dado[i]==3:
        qtde[2] += 1
    elif dado[i]==4:
        qtde[3] += 1
    elif dado[i]==5:
        qtde[4] += 1
    else:
        qtde[5] += 1
print("Lancamento de dados\nNumero - Quantidade")
for i in range(6):
    print(f"{i+1}\t\t{qtde[i]}")