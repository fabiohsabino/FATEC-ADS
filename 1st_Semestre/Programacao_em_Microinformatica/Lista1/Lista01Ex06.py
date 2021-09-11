'''
6.	Implemente um programa para ler o salário mensal atual de
um funcionário e o percentual de reajuste. Calcular e escrever
o valor do novo salário.
'''

salario = float(input("Informe o salário atual >> R$ "))
reajuste = float(input("Informe o percentual de aumento >> "))
novoSal = salario * (reajuste/100) + salario
print(f"Com o aumento de {reajuste} % o salário foi para R$ {novoSal:.2f}")