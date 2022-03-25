frase = input("Digite uma palavra: ")
if len(frase)%2 == 1:
    print(frase[len(frase)//2])
else:
    print(f"{frase[(len(frase)//2)-1]}{frase[(len(frase)//2)]}")