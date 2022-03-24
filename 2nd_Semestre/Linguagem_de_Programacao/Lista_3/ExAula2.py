def fibo(n):
    if n <= 2:
        return n
    return fibo(n-1) + fibo(n-2)


num = int(input("Digite um numero -> "))
print(fibo(num))
