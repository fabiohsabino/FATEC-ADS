n = int(input("Digite o tamanho do quadrado: "))
m = [0]*n
cont = 1
soma = 0


print()
for i in range(n):
    m[i] = [0]*n
    for j in range(n):
        m[i][j] = int(input(f"{cont}ª Valor ->"))
        cont += 1
print()     

for i in range(n):
    for j in range(n):
        print(f"{m[i][j]:2}", end = " ")
    print()

soma = (n + n**3)/2


cont_linha = 0
cont_coluna = 0
diag1 = 0
diag2 = 0
for i in range(n):  
    soma_linha = 0
    soma_coluna = 0
    for j in range(n):
        soma_linha += m[i][j]
        soma_coluna += m[j][i]
        if j == i:
            diag1 += m[i][j]
        if j+i == (n-1):
            diag2 += m[i][j] 
    if soma_linha == soma:
        cont_linha += 1
    if soma_coluna == soma:
        cont_coluna += 1

print()


if (cont_linha == n and cont_coluna == n) and (diag1 == soma and diag2 == soma):
        print("-="*10,"É QUADRADO MÁGICO!","=-"*10)
        

else:
        print("-="*10,"NÃO É QUADRADO MÁGICO!","=-"*10)
