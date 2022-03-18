def verifica(a):
    a = a.split()
    for p in a:
        if not p.isalpha():
            return False
    return True

def somatoria(a):

    a = a.split()
    for i in range(len(a)):
        v = []
        for j in range(len(a[i])):
            v.append(ord(a[i][j]))
        v = sum(v)
        print(v)

        if primo(v):
            print("-"*30)
            print("Palavra Prima!!!")
            print(f"{a[i]} -> {v}")
            print("-" * 30)



def primo(a):
    cont = 0
    for i in range(1, a + 1):
        if a % i == 0:
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

