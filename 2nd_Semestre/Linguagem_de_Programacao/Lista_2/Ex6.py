'''Faça um programa em Python que gere uma matriz 10 x 10 de inteiros e crie funções para calcular 
e retornar o maior elemento de uma determinada coluna (informada por parâmetro) e o menor elemento de uma determinada linha 
(informada por parâmetro). Peça a coluna e a linha, chame os respectivos métodos e mostre o resultado.'''

from random import randint
def linha(a, b):
    menor = 51
    for i in range(10):
        if a[b][i] <= menor:
            menor = a[b][i]
    return menor

def coluna(a, b):
    maior = -1
    for i in range(10): 
        if maior <= a[i][b]:
            maior = a[i][b]
    return maior
    
#programa principal
m = [0]*10

for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(1,50)

for i in range(10):
    for j in range(10):
        print(f"[{m[i][j]:2}]", end=' ')
    print()

l = int(input("Digite o numero da linha: "))
c = int(input("Digite o numero da coluna: "))

print(linha(m, l))
print(coluna(m, c))
