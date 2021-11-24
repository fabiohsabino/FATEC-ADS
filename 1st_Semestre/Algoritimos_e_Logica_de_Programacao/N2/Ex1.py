from random import randint

cont = 9
sim = 0
op = True
v = []

for i in range(10):
    v.append(randint(1,2))

print(v)


for i in range(5):
    if v[i] == v[9-i]:
        sim += 1

if sim == 5:
    print("Vetor Simetrico!!")
    
else:     
    print("Vetor Não Simetrico!!")       
    



