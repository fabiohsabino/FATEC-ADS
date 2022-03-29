frase = input("Digite um frase: ")
cesar = ''

for i in frase:
    cesar += chr(ord(i)+3)

print(cesar)