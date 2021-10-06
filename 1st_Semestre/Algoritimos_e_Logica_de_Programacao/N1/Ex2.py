a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B (O valor de B deve ser maior que o valor de A): "))
soma = 0
if a >= b:
    print("Valores invalidos!!!")
else: 
    for i in range (a, b+1):
        soma += a
        a+=1
    print(f"Soma dos valores compreendidos entre [A] e [B] = {soma}")



