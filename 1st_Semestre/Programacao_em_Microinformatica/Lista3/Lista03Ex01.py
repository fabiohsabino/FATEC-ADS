'''
1. Faça um programa que leia um número e, caso ele seja positivo,
calcule e mostre:
• O número digitado ao quadrado
• A raiz quadrada do número digitado
'''
from math import sqrt

num = int(input("Informe um número >> "))
if num < 0:
    print("Número negativo")
else:
    print(f"{num} ao quadrado é {num**2}")
    print(f"Raiz quadrada de {num} é {sqrt(num)}")