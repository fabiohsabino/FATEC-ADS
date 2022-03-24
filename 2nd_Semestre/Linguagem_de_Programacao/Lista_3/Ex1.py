def eleva(n,e):
    if e == 1:
        return n
    return n*eleva(n, e-1)


#main()
num = int(input("Digite um numero: "))
ex = int(input("Digite o numero a ser elevado: "))
print(eleva(num, ex))