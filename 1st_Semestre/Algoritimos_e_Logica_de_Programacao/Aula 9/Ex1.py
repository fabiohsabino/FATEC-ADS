peso = float(input("Digite o peso dos peixes: "))
if peso < 50.0:
    print("Não há multa")
else:
    multa = 4.00 * (peso-50)
    print(f"Valor da multa = {multa}")