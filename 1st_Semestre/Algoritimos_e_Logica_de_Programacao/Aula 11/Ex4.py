a = 0
b = 1
c = 0
fib = []

for i in range(20):
    c = a+b
    b = a
    a = c
    fib.insert(i, c)
print(fib)