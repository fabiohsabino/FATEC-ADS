from random import randint
import os

def collatz(x):
    l = []
    cp = 0
    ci = 0
    l.append(x)
    while x > 1:
        if x%2 == 0:
            x = x/2
            l.append(x)
            cp += 1
        else:
            x = 3*x+1
            l.append(x)
            ci += 1
    ci+=1        
    mx = max(l)
    return l, cp, ci, mx


os.system('cls')
os.system("mkdir Input")
os.system("mkdir Output")
for i in range(100):
    fi = open("Input\\A_"+str(i+1)+".txt", "w")
    fo = open("Output\\A_"+str(i+1)+".txt", "w")
    n = randint(1, 5)
    fi.write(f"{n}\n")
    for i in range(n):
        x = randint(1,15)
        fi.write(f"{x}\n")
        fo.write(f"Valor inicial: {x}\n")
        print(f"Valor inicial: {x}")
        a,b,y,z = collatz(x)
        #fp.write(f"Numeros gerados: {s}\n")           #Gravar Numeros Gerados
        #print(f"Numeros gerados: {a}")                #Verificar Numeros Gerados 
        fo.write(f"Numeros pares: {b}\nNumeros impares: {y}\nMaior Numero: {z}\n")
        print(f"Numeros pares: {b}\nNumeros impares: {y}\nMaior Numero: {z}")
    fi.close()
    fo.close()