'''
3. Escreva um programa que, dados dois números inteiros,
mostre na tela o maior deles, assim como a
diferença existente entre ambos.
'''

a = int(input("Entre com o 1º valor >> "))
b = int(input("Entre com o 2º valor >> "))
if a > b:
    print(f"{a} é maior que {b} e a diferença entre eles é {a-b}")
elif b > a:
    print(f"{b} é maior que {a} e a diferença entre eles é {b-a}")
else:
    print("São números iguais, não há diferença entre eles")