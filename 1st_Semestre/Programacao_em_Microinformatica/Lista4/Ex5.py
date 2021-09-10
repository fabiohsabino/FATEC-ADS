par = 0
impar = 0
cont = 1
while cont <= 10:
    num = int(input(f"Digite o {cont} numero: "))
    
    if num%2 == 0:
        par += num
    else:
        impar += num
print(f"PAR = {par}|IMPAR = {impar}")