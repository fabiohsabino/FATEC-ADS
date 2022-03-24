def fatorial(n):
    if n==1:
        return n
    return n * fatorial(n-1)


num = int(input("Digite um numero: "))
print(fatorial(num))