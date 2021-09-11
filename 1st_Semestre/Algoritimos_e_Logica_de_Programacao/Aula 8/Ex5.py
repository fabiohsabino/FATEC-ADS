num = int(input("Digite um numero: "))
perf = 0
for i in range (1, num):
    if num%i == 0:
        perf += i
if perf == num:
    print("\nNumero perfeito!")
else:
    print("\nNao e um numero perfeito!")

