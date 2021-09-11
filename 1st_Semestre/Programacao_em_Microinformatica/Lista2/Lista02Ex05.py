'''
5.	Escreva um programa que leia o valor de 3 ângulos de um
triângulo e escreva se o triângulo é acutângulo, retângulo
ou obtusângulo.
Observação:
Triângulo retângulo: possui um ângulo reto (90 graus).
Triângulo obtusângulo: possui um ângulo obtuso
                       (ângulo maior que 90 graus).
Triângulo acutângulo: possui 3 ângulos agudos
                      (ângulo menor que 90 graus).
Faça a validação para verificar se a soma dos ângulos é igual a 180
'''
print("Informe as medidas dos ângulos de um triângulo")
a = float(input("Ângulo 1 >> "))
b = float(input("Ângulo 2 >> "))
c = float(input("Ângulo 3 >> "))
if a+b+c == 180 and a!=0 and b!=0 and c!=0:
    if a == 90 or b == 90 or c == 90:
        print("Triângulo retângulo")
    elif a > 90 or b > 90 or c > 90:
        print("Triângulo obtusângulo")
    else:
        print("Triângulo acutângulo")
else:
    print("Valores inválidos!!")
