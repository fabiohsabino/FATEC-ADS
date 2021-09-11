'''
9.	Uma receita para produzir um bolo conta com 2 xicaras de farinha de trigo,
3 ovos e 5 colheres de leite (estes dados são constantes nesta receita).
Você deve escrever um programa em Python que dados como entrada A
(quantidade de xicaras de farinha de trigo), B (quantidade de ovos) e
C (quantidade de colheres de leite) todos valores inteiros, o programa
deve mostrar quantos bolos podem ser produzidos.

Veja a simulação:
Ex.1	A =  4 B = 6 e  C = 10  produzirá a saída: 2 bolos.
Ex.2	A =  4 B = 6 e  C = 9  produzirá a saída: 1 bolo.
Ex.3	A = 10 B = 10 e C = 25  produzirá a saída: 3 bolos.
'''

print("Informe a quantidade de cada ingrediente que você possui")
A = int(input("xícaras de farinha de trigo >> "))
B = int(input("ovos >> "))
C = int(input("colheres de leite >> "))

A = A // 2
B = B // 3
C = C // 5

if A < B and A < C:
    print(f"Com esses ingredientes, você conseguirá fazer {A} bolos")
elif B < C:
    print(f"Com esses ingredientes, você conseguirá fazer {B} bolos")
else:
    print(f"Com esses ingredientes, você conseguirá fazer {C} bolos")
