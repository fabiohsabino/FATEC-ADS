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
        print("Empate!!!\n")
    elif j1 != j2 and j1 != j3:
        p1 += 1
        print(f"J1P = {p1} | J2P = {p2} | J3P = {p3}\n")
    elif j2 != j1 and j2 != j3:
        p2 += 1
        print(f"J1P = {p1} | J2P = {p2} | J3P = {p3}\n")
    elif j3 != j1 and j3 != j2:
        p3 += 1
        print(f"J1P = {p1} | J2P = {p2} | J3P = {p3}\n")
if p1>p2 and p1>p3:
    print(f"Jogador 1 e o vencedor")
elif p2>p1 and p2>p3:
    print("Jogador 2 e o vencedor")
elif p3 > p1 and p3 > p2:
    print("Jogador 3 e o vencedor")




