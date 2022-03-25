def verifica(ver, num):
    if len(ver) == 0:
        return False
    if ver[0] == num:
        return True
    return verifica(ver[1:], num)
  
        
#main()
from random import randint
v = []
n = randint(1,50)

for i in range(10):
    v.append(randint(1,50))
print(n)
print(v)
if verifica(v, n):
    print("O numero está contido no vetor..")
else:
    print("Numero não está contido no vetor..")