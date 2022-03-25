frase = input("Digite uma frase: ")
carac = input("Digite um caractere a ser encontrado: ")
cont = 0
for i in range(len(frase)):
    if frase[i] in carac:
        cont += 1

print(cont)