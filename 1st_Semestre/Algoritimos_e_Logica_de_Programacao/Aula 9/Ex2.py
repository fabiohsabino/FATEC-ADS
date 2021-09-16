polu = float(input("Digite o nível de poluição: "))
if polu < 0.30:
    print("Poluição aceitavel!")
elif polu >= 0.30 and polu < 0.4:
    print("Industrias do Grupo 1 devem suspender as atividades")
elif polu >= 0.4 and polu < 0.5:
    print("Industrias do Grupo 1 e 2 devem suspender as atividades")
else:
    print("Todos os Grupos devem suspender as atividades")