'''
1.	Elabore um programa que leia um número (de 3 algarismos,
faça a validação para aceitar apenas números menores que 1000)
e imprima se ele é ascendente. Um número é ascendente se seus
algarismos estão em ordem crescente.
Por exemplo, o número 258 é ascendente, pois, 2 < 5 e 5 < 8.
'''

num = int(input("Informe um número de 3 dígitos >> "))
if num >= 1000:
    print("Inválido!!")
else:
    c = num // 100
    d = num % 100 // 10
    u = num % 10
    if c < d and d < u:  # ou if c < d < u:
        print(f"{num} é um número ascendente")
    else:
        print(f"{num} não é um número ascendente")
