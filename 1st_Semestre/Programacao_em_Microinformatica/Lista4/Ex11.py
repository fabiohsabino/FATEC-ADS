for i in range (1000,10000):
   div = i//100
   rest = i%100
   soma = div + rest
   if soma**2 == i:
       print(i, end=' ')