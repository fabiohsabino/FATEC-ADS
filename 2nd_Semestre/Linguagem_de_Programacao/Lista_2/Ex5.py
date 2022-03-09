def primo(a):
    cont = 0
    for i in range(1, a+1):
        if a%i == 0:
            cont+=1
    if cont == 2:
        return True
    else: 
        return False

#Programa principal
v = []
cont = 0
num = (int(input("Digite um numero: ")))
num2 = (int(input("Informe um intervalo: ")))
while cont<=num2:
    if primo(num) == True:
        v.append(num)
        cont+=1
    num+=1
print(v)