s1 = input("Digite uma frase: ")
print(len(s1))
s2 = input("Digite uma frase: ")
if s1 == s2:
    print("Frases iguais!!!")
else:
    print("Frases diferentes!!!")
print(s1+s2)
print(s1[::-1])
car = input("Digite um caractere: ")
print(s1.count(car))
c1 = input("Digite um caractere: ")
c2 = input("Digite um segundo caractere: ")
print(s1.replace(c1,c2))
if s2 in s1:
    print(f"é uma substring de s1")
else:
    print("Não é uma substring de s1")
ret = int(input("Digite a posição a ser retornada: "))
print(s1[ret::])