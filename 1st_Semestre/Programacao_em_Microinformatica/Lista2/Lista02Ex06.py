'''
Sejam três números inteiros diferentes digitados pelo usuário,
faça um programa que os coloque em
ordem crescente.
'''

print("Informe 3 valores")
a = int(input("1º valor >> "))
b = int(input("2º valor >> "))
c = int(input("3º valor >> "))
if a < b < c:
    print(a,b,c)
elif a < c < b:
    print(a,c,b)
elif b < a < c:
    print(b,a,c)
elif b < c < a:
    print(b,c,a)
elif c < a < b:
    print(c,a,b)
else:
    print(c,b,a)

#Trocando os valores das variáveis
#Colocando em a o menor valor, em b o valor do meio e em c o maior valor
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a,b,c)