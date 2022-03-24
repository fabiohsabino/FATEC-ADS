frase = input("Digite uma frase: ")
vogal = "AaEeIiOoUu"
for i in range(frase):
    if frase[i] not in vogal:
        print(frase[i],end = '')