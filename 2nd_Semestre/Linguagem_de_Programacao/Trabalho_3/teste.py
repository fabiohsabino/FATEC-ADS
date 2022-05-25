teste = '12345'
j = list(teste)
print(j)
for i in range(len(j)):
    j[i] = chr(ord(j[i])+1)
l = "".join(j)
print(l)