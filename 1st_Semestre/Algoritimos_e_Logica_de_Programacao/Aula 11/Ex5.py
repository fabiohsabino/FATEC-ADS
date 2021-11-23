from random import randint

a =[]
b =[]
c =[]

for i in range(10):
    a.append(randint(1, 50))
    b.append(randint(1, 50))

for i in range(10):
    for j in range(10):
        if a[i]==b[j]:
            c.append(a[i])

#falta remover repetidos da lista c

print(a)
print(b)
print(c)
