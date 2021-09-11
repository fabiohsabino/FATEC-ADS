num = int(input("Digite um numero: "))
soma = 0

for i in range(1, num+1, 2):
    soma += i
    if soma>=num:
        break

if soma == num:
    print("Quadrado perfeito!")
else:
    print("Quadrado imperfeito!")
