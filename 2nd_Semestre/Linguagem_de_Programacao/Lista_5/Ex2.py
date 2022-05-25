def quadrados(x):
    l = [i*i for i in range(x+1)]
    return l


num = int(input("Digite um numero: "))
print(quadrados(num)[1:])