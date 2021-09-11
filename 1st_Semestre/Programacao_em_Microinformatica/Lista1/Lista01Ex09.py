'''
9.	Escreva um programa para ler uma temperatura em graus Fahrenheit,
calcular e escrever o valor correspondente em graus Celsius:
C = ((F – 32)/9)*5
'''
print("Conversor de graus Fahrenheit para graus Celsius")
F = float(input("ºF >> "))
C = ((F - 32) / 9) * 5
print(f"{F}° Fahrenheit = {C}° Celsius")