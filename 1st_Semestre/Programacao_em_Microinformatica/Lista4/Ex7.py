from random import randint
cont = 1
maior = 0
while cont <= 20:
    num = randint(1,50)
    print(num)
    if num>maior:
        maior = num
    cont += 1
print(f"\nMAIOR VALOR = {maior}")