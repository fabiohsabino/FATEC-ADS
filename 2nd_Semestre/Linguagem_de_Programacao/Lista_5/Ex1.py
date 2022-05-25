def soma_nat(x):
    l = [i for i in range(x+1)]
    return sum(l)


n = int(input("Digite um numero: "))
print(soma_nat(n))