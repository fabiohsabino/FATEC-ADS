from random import randint

j1 = 0
j2 = 0 
j3 = 0
p1 = 0
p2 = 0
p3 = 0

while (p1 < 3) and (p2 < 3) and (p3 < 3):
    j1 = randint(1, 2)
    j2 = randint(1, 2)
    j3 = randint(1, 2)
    print(f"J1 = {j1} | J2 = {j2} | J3 = {j3}")
    if j1 == j2 == j3:
        print(">>Empate<<\n")
    elif j1 != j2 and j1 != j3:
        p1 += 1
        print(f"J1 Ganhou -> J1 Pontos = {p1} | J2 Pontos = {p2} | J3 Pontos = {p3}\n")
    elif j2 != j1 and j2 != j3:
        p2 += 1
        print(f"J2 Ganhou -> J1 Pontos = {p1} | J2 Pontos = {p2} | J3 Pontos = {p3}\n")
    else:
        p3 += 1
        print(f"J3 Ganhou -> J1 Pontos = {p1} | J2 Pontos = {p2} | J3 Pontos = {p3}\n")
if p1>p2 and p1>p3:
    print("#"*17)
    print(f"Jogador 1 Venceu!")
    print("#"*17)
elif p2>p1 and p2>p3:
    print("#"*17)
    print("Jogador 2 Venceu!")
    print("#"*17)
else:
    print("#"*17)
    print("Jogador 3 Venceu!")
    print("#"*17)




