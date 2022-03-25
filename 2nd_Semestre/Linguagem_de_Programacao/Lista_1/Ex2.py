frase = input("Digite uma frase: ")
vogal = "AaEeIiOoUu"
cont = 0
for i in range(len(frase)):
    if frase[i] not in vogal:
        cont+=1
print(cont)