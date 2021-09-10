num = int(input("Dogite um numero: "))
cont = 0
for i in range (1, num+1):
    if num%i == 0:
        cont += 1
if cont == 2:
    print("Numero primo")
else:
    print("Nao e primo")
