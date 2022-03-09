def pot(a, b):
    a = a**b
    return a


#main
num = int(input("Digite um numero: "))
exp = int(input("Digite o valor da potencia: "))
print(pot(num, exp))