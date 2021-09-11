'''
3.	Faça um programa que lê um conjunto de 3 valores opção,
base, altura, onde opção é um valor inteiro e positivo
e base e altura, são quaisquer valores reais. A seguir:
a)	Se op=1 calcular e imprimir a área de um retângulo
    Area=base*altura.
b)	Se op=2 calcular e imprimir a área de triângulo
    Area=(base*altura)/2.
'''

print("Informe o polígono desejado para cálculo da área")
op = int(input("1. Retângulo"
               "\n2. Triângulo"
               "\nOpção >> "))
if op != 1 and op != 2:    # ou 1 != op != 2:
    print("Opção inválida!!")
else:
    base = float(input("Base >> "))
    altura = float(input("Altura >> "))
    if op == 1:
        area = base * altura
        print(f"A área do retângulo é {area:.2f}")
    else:
        area = (base * altura) / 2
        print(f"A área do triângulo é {area:.2f}")