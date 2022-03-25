pal = input("Digite uma palavra: ")
for i in range(len(pal)):
    pal[i] = ord(pal[i]+1)
print(pal)