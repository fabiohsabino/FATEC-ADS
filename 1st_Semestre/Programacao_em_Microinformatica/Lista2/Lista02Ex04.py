'''
4.	Escreva um programa que leia o valor de 3 lados de um
triângulo e escreva se o triângulo é equilátero, isósceles
ou escaleno.
Observação:
Triângulo equilátero: possui três lados iguais.
Triângulo isósceles: possui dois lados iguais.
Triângulo escaleno: possui três lados diferentes.
Faça a validação para verificar se os valores dos lados formam
um triângulo. Nenhum lado pode ser maior que a soma dos
outros dois.
'''
print("Informe os 3 lados de um triângulo")
a = int(input("Lado a >> "))
b = int(input("Lado b >> "))
c = int(input("Lapdo c >> "))
if a >= b + c or b >= a + c or c >= a + b:
    print("As medidas não formam um triângulo")
elif a == b and b == c: # a == b == c:
    print("Triângulo equilátero")
elif a != b and b != c and a != c: # a != b != c != a:
    print("Triângulo escaleno")
else:
    print("Triângulo isósceles")