def verifica(ver, num):
    if num in ver:
        return True



#main()
from random import randint
v = []
n = randint(1,50)
#n = int(input("Digite um valor entre 1 e 50: "))

for i in range(10):
    v.append(randint(1,50))
print(n)
print(v)
if verifica(v, n):
    print("O numero está contido no vetor..")
else:
    print("Numero não está contido no vetor..")