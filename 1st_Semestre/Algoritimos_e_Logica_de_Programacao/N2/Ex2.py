from random import randint

m = [0]*5
maior = 0
menor = 51
v = int(input("Digite o numero da linha [0 a 4]: "))
if v < 0 or v > 4:
    print("Linha inválido!!")
else:
    for i in range(5):
        m[i] = [0]*5
        for j in range(5):
            m[i][j] = randint(1,50)
    
    for i in range(1):
        for j in range(5):
            if m[v][j]>maior:
                maior = m[v][j]
            if m[v][j]<menor:
                menor = m[v][j]

    print()
    for i in range(5):
        for j in range(5):
            print(f"{m[i][j]:2}",end = " ")
        print()
    
    print()
    print(f"Menor valor da linha {v} = {menor}")
    print(f"Maior valor da linha {v} = {maior}")
    