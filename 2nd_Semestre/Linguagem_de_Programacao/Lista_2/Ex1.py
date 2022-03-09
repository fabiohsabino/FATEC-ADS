def poui(k):
    if k%2 == 0:
        k = 'par'
        return k
       
    else:
        k = 'impar'
        return k
        

#programa principal

num = int(input("Digite um numero -> "))
print(poui(num))
