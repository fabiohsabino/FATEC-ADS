'''
2. Faça um programa que receba um
número inteiro e verifique se este número é par ou ímpar.
'''
print("Informe um número para verificar se é PAR ou ÍMPAR")
numero = int(input("Número >> "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR")
else:
    print(f"O número {numero} é ÍMPAR")