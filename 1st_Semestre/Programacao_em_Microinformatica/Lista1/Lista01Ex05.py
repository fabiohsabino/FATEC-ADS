'''
5.	Escreva um programa que armazene um valor de entrada em uma
variável A e outro em uma variável B. A seguir (utilizando apenas
atribuições entre variáveis) troque os seus conteúdos fazendo com
que o valor que está em A passe para B e vice-versa.
Ao final escrever os valores que ficaram armazenados nas variáveis.
'''

a = int(input("Informe o valor de a >> "))
b = int(input("Informe o valor de b >> "))

#1ª solução
print(f"Antes da troca  a = {a} e b = {b}")
x = a
a = b
b = x
print(f"Após a troca    a = {a} e b = {b}")

#2ª solução
print(f"Antes da troca  a = {a} e b = {b}")
a, b = b, a
print(f"Após a troca    a = {a} e b = {b}")