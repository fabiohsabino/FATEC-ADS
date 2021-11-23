gab = []
alu = []
cont = 0


while True:
    for i in range(3):
        gab.append(input(f"Digite a {i+1}ª resposta do gabarito: "))
    for i in range(3):
        alu.append(input(f"Digite a sua resposta da {i+1}ª questão: "))
    for i in range(3):
        if gab[i] == alu[i]:
            cont+=1
    print(f"Voce acertou {cont+1} questões")
    var = input("Deseja continuar? [s/n]")
    if var == 'n':
        break
        



