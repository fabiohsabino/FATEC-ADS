par = 0
impar = 0
cont = 1
qtd = int(input("Quantidade de vezes a ser repetido: "))
while cont <= qtd:
    num = int(input(f"Digite o {cont} numero: "))
    
    if num%2 == 0:
        par += num
    else:
        impar += num
    cont += 1
print(f"PAR = {par}|IMPAR = {impar}")