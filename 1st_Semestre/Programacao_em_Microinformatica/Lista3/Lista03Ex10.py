'''
10.	Jogo da Roleta (Simulador)
Pesquisa: Método para gerar um número aleatório

Dados de entrada:
	Valor da aposta em R$.
	Número a ser apostado (1 a 36).

O programa deverá sortear um número aleatório e as seguintes regras deverão ser
consideradas:

	Se o apostador acertar o número, imprimir o valor ganho sendo 5 vezes o
    valor apostado;
	Case ele erre, mas acertar a dúzia, isto é, Número da Aposta estiver entre
    (1 e 12) e o Número Sorteado também estiver entre (1 e 12) ou Número da Aposta
    estiver entre (13 e 24) e o Número Sorteado também estiver entre (13 e 24)
    ou Número da Aposta estiver entre (25 e 36) e o Número Sorteado também estiver
    entre (25 e 36), imprimir o valor ganho sendo 3 vezes o valor da aposta;
	Caso ainda erre, mas acertar a paridade, isto é, o Número da Aposta é par e o
    Número Sorteado também for par ou Número da Aposta é ímpar e o Número Sorteado
    também for ímpar, imprimir o valor ganho sendo o dobro do valor da aposta.
	Caso erre ainda, ele perde a quantia apostada.
'''
from random import randint
print("JOGO DA ROLETA".center(50))
print("="*50)
valor = float(input("Aposta >> R$ "))
aposta = int(input("Número [1 a 36] >> "))
print("="*50)
if aposta not in range(1,37):
    print("O número apostado não está dentro do intervalo válido!!")
else:
    sorteio = randint(1,36)
    print(f"Número sorteado >> {sorteio}")
    if aposta == sorteio:
        print(f"ACERTOU O NÚMERO!! Ganhou R$ {valor * 5:.2f}")
    elif (aposta - 1) // 12 == (sorteio -1) // 12:
        print(f"ACERTOU A DÚZIA!! Ganhou R$ {valor * 3:.2f}")
    elif sorteio % 2 == aposta % 2:
        print(f"ACERTOU A PARIDADE!! Ganhou R$ {valor * 2:.2f}")
    else:
        print("PERDEU TUDO!!")



