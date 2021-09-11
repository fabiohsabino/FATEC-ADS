'''
13.	Quadrante
Leia 2 valores com casa decimal (x e y), que devem representar as coordenadas
de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence
o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem “Origem”.
Q1  x e y positivos
Q2  x negativo e y positivo
Q3  x e y negativos
Q4  x positivo e y negativo
'''

print("Informe as coordenadas de um ponto em um plano")
x = float(input("x >> "))
y = float(input("y >> "))
if x == 0 and y == 0:
    print("ORIGEM")
elif y == 0:
    print("Eixo X")
elif x == 0:
    print("Eixo Y")
elif x > 0 and y > 0:
    print("Quadrante 1")
elif x < 0 and y > 0:
    print("Quadrante 2")
elif x < 0 and y < 0:
    print("Quadrante 3")
else:
    print("Quadrante 4")