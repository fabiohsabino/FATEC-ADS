num = int(input("Digite um nuemro: "))
ant = 1
prox = 0
fib = 0
for i in range(num):
    prox = ant
    ant = fib
    fib = ant+prox
    print(fib, end = ' ') 