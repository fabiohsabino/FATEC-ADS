'''
4.	Escreva um programa que leia a quantidade de dias, horas,
minutos e segundos do usuário. Calcule o total em segundos.
'''

print("Informe a quantidade de cada item abaixo")
dias = int(input("Dias >> "))
horas = int(input("Horas >> "))
minutos = int(input("Minutos >> "))
segundos = int(input("Segundos >> "))

totalS = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print("Total de segundos >>",totalS)