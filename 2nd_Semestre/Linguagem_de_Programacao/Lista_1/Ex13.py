s1 = input("Digite uma frase: ")
s2 = input("Digite uma segunda frase: ")
n = int(input("Digite um valor inteiro: "))

L = s1.split()
G = s2.split()

print(L)
print(G)
for i in range(n):
    L[i] += G[i]
L = " ".join(L)
print(L)