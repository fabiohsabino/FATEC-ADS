from random import randint

l = [randint(1,10) for num in range(20)]
n = int(input("Digite um numero entre 1 e 10 >> "))
if n <= 0 and n >= 10:
    print("numero invalido!!!")
else:
    print(l)
    print(f"O valor {n} foi encontrado {l.count(n)} vezes")
