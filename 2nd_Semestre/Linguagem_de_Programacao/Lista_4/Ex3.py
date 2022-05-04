from random import randint

l1 = [randint(1,50) for i in range(10)]
l2 = [randint(1,50) for i in range(10)]
l3 = []
for i in range(10):
    if i%2==0:
        l3.append(l1[i])
    else:
        l3.append(l2[i])
print(l1)
print(l2)
print(l3)
