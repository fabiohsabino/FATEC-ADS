from unidecode import unidecode


def verifica(a):
    if a.isalpha():
        a = unidecode(a)
        return a
    else:
        return False


def somatoria(a):
    v = []
    a = a.split()
    for i in range(len(a)):
        for j in range(len(a[i])):
            v.append(ord(a[i][j]))
    v = sum(v)

    if primo(v):
        print("-"*30)
        print("Palavra Prima!!!")
        print(f"{a} -> {v}")
        print("-" * 30)

    else:
        print("-" * 30)
        print("Não é uma Palavra Prima!!!")
        print(f"{a} -> {v}")
        print("-" * 30)


def primo(a):
    cont = 0

    for i in range(1, a):
        if a%i == 0:
            cont += 1
        if cont == 2:
            return True
        else:
            return False


while True:
    frase = input("Digite uma frase: ").upper()
    if verifica(frase):
        somatoria(frase)
    else:
        print("Frase contem caracteres invalidos...")