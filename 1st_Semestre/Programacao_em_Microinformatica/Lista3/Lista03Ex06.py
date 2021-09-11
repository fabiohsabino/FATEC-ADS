'''
6. Calcule as raízes da equação de 2o grau.
Lembrando que:
Onde 𝛥 = 𝑏^2 − 4𝑎𝑐
E 𝑎𝑥^2 + 𝑏𝑥 + 𝑐 = 0 representa uma equação de 2º grau.
A variável a tem que ser diferente de zero. Caso seja igual,
imprima a mensagem “Não é equação de segundo grau”.
• Se ∆ < 0, não existe raiz real. Imprima a mensagem “Não existe raiz”.
• Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem “Raiz única”.
• Se ∆ > 0, imprima as duas raízes reais.
'''
from math import sqrt

print("Informe os coeficientes para cálculo das raízes de uma equação de 2º grau")
a = float(input("a >> "))
if a == 0:
    print("Não é equação de 2º grau")
else:
    b = float(input("b >> "))
    c = float(input("c >> "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existe raiz real")
    elif delta == 0:
        x = -b / 2*a
        print(f"Raiz única x = {x}")
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f"As raízes são x1 = {x1} e x2 = {x2}")
