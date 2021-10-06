from random import randint

v1 = [10]
v2 = [10]
vs = [10]

for i in range(10):
    v1.insert(i, randint(1, 10))
    v2.insert(i, randint(1, 10))
    vs.insert(i, v1[i] + v2[i])
print(v1)
print(v2)
print(vs)
