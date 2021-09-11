'''
8.	Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias
pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''

print("Programa para calcular o valor do aluguel de um carro")
print("="*55)
dias = int(input("Informe a quantidade de dias de aluguel >> "))
km = float(input("Informe a quantidade de km percorridos >> "))
print("="*55)
pagar = dias * 60 + km * 0.15
print(f"O preço do aluguel do carro ficou em R$ {pagar:.2f}")