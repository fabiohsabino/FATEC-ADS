txt = input('Informe a palavra >> ')
cri = ''
for letra in txt:
    cri += chr(ord(letra)+1)
print(cri)