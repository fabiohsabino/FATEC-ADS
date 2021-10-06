from random import randint

v1 = []
v2 = []
pe = 0

for i in range(10):
    v1.append(randint(1, 10))
    v2.append(randint(1, 10))
    pe += v1[i]*v2[i]

print(v1)
print(v2)
print(pe)



