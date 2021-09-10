num = int(input("Digite um numero a ser fatorado: "))
fat = 1
for i in range (num,1,-1):
    fat *= i
print(f"Fatorial de {num} = {fat}")