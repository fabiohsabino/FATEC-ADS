def primo(a):
    cont = 0
    for i in range(1, a+1):
        if a%i == 0:
            cont+=1
    if cont == 2:
        return True
    else: 
        return False


#programa principal
num = int(input("Digite um numero: "))
if primo(num) == True:
    print("Numero Primo")
else:
    print("Não é numero primo")