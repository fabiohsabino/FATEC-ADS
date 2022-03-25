frase = input("Digite uma frase: ")
fraseinv = frase[::-1]
print(f"{frase} <-> {fraseinv}")

if frase == fraseinv:
    print("Palindromo")
else:
    print("Não Palindromo")