from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(randint(1, 10))
    b.append(randint(1,10))

c.append(a)

for i in range(10):
    for j in range(10):
        if a[i] != b[j]:
            c.append(b[j])
print(a)
print(b)
print(c)

