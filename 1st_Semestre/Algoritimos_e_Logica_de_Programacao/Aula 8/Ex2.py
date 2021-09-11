num = int(input("Digite um numero: "))
fat = 1
for i in range(num,1,-1):
    fat *= i
print(f"{num}! = {fat}")
