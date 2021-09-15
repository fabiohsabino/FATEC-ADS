mn = -1
for i in range(1, 4):   
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    if media>mn:
        ma = nome
        mn = media
print(f"O melhor aluno(a) é {ma} com a media de {mn:.2f}")
