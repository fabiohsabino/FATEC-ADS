'''
2.	Elaborar um programa para ler somente a parte numérica da
 placa de um carro e apresentar o dia do rodízio (em SP)
 para o mesmo (digitar apenas um número com 4 dígitos, fazer
 a validação).

Dia	            Segunda	 Terça	Quarta	 Quinta	 Sexta
Final da placa	1 ou 2	3 ou 4	5 ou 6	7 ou 8	9 ou 0
'''

placa = int(input("Informe os números da placa do veículo >> "))
if placa > 9999:
    print("A placa deve conter apenas 4 dígitos")
else:
    ud = placa % 10
    if ud == 1 or ud == 2:
       print("Seu rodízio é de segunda-feira")
    elif ud == 3 or ud == 4:
        print("Seu rodízio é de terça-feira")
    elif ud == 5 or ud == 6:
        print("Seu rodízio é de quarta-feira")
    elif ud == 7 or ud == 8:
        print("Seu rodízio é de quinta-feira")
    else:
        print("Seu rodízio é de sexta-feira")


