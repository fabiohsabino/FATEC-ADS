#Fabio Henrique Sabino de Souza

from random import randint
pj1 = 0
pj2 = 0
while pj1 < 2 and pj2 < 2:
    j1 = int(input("\nEscolha:\n[1] - Papel | [2] - Pedra | [3] - Tesoura:  "))
    j2 = randint(1, 3)

    if j1 == j2:
        if j1 == 1:
            print("Jogador -> Papel x Papel <- Computador")
        if j1 == 2:
            print("Jogador -> Pedra x Pedra <- Computador")
        if j1 == 3:
            print("Jogador -> Tesoura x Tesoura <- Computador")
        print("\t\t>>Empate<<")
        print(f"Pontos Jogador {pj1} | Pontos Computador {pj2}")
    elif j1 == 1 and j2 == 2:
        print("Jogador -> Papel x Pedra <- Computador")
        print("\t\t>>Você Ganhou<<")
        pj1 += 1
        print(f"Pontos Jogador {pj1} | Pontos Computador {pj2}")
    elif j1 == 2 and j2 == 3:
        print("Jogador -> Pedra x Tesoura <- Computador")
        print("\t\t>>Você Ganhou<<")
        pj1 += 1
        print(f"Pontos Jogador {pj1} | Pontos Computador {pj2}")
    elif j1 == 3 and j2 == 1:
        print("Jogador -> Tesoura x Papel <- Computador")
        print("\t\t>>Você Ganhou<<")
        pj1 += 1
        print(f"Pontos Jogador {pj1} | Pontos Computador {pj2}")
    else:
        if j2 == 1:
            print("Jogador -> Pedra x Papel <- Computador")
        if j2 == 2:
            print("Jogador -> Tesoura x Pedra <- Computador")
        if j2 == 3:
            print("Jogador -> Papel x Tesoura <- Computador")

        print("\t\t>>Você Perdeu<<")
        pj2 += 1
        print(f"Pontos Jogador {pj1} | Pontos Computador {pj2}")
    
if pj1 > pj2:
    print("\n")
    print("#"*33)
    print(f"  Parabens, você ganhou por {pj1}x{pj2}")
    print("#"*33)
else:
    print("\n")
    print("#"*31)
    print(f"  Computador ganhou por {pj2} x {pj1}")
    print("#"*31)

