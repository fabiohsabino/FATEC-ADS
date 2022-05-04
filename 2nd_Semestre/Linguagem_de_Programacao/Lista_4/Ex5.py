from random import randint

l = [randint(1,50) for i in range(20)]
print(l)
n = int(input("Digite um numero >> "))
while True:
    if n in l:
        l.remove(n)
    else:
        break
print(l)