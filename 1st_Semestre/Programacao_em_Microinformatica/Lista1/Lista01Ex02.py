'''
2.	Fazer um programa para receber 3 valores inteiros do usuário
e mostrar a sua média.
'''

print("Informe 3 valores")
print("<>"*15)
v1 = int(input("1º >> "))
v2 = int(input("2º >> "))
v3 = int(input("3º >> "))
media = (v1 + v2 + v3) / 3
print("<>"*15)
print(f"Média = {media:.2f}")