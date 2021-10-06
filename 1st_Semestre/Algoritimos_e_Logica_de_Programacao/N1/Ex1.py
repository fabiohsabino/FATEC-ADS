nota = float(input("Digite a nota a ser convertida: "))

if nota > 10:
    print("Nota Invalida!!")
elif nota >= 9 and nota <= 10:
    print("Conceito: A")
elif nota >= 7 and nota < 9:
    print("Conceito: B")
elif nota >=5 and nota < 7:
    print("Conceito: C")
elif nota >= 3 and nota < 5:
    print("Conceito: D")
elif nota < 3:
    print("Conceito: E")

