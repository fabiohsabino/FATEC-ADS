'''
5.	A nota final de um estudante é calculada a partir de três
notas atribuídas entre o intervalo de 0 até 10, respectivamente,
a um trabalho de laboratório, a uma avaliação semestral e a um exame
final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3;
Exame Final: 5. De acordo com o resultado, mostre na tela se o
aluno está reprovado (média entre 0 e 2,9), de recuperação
(entre 3 e 4,9) ou se foi aprovado.
Faça todas as verificacões necessárias.
'''

print("Informe as notas do estudante")
trabLab = float(input("Nota do trabalho de laboratório >> "))
if trabLab not in range(0,11):
    print("Nota inválida!!")
else:
    avSem = float(input("Nota da avaliação semestral >> "))
    if avSem not in range(0,11):
        print("Nota inválida!!")
    else:
        exFinal = float(input("Nota do exame final >> "))
        if exFinal not in range(0,11):
            print("Nota inválida!!")
        else:
            media = (trabLab*2 + avSem*3 + exFinal*5) / 10
            if media < 3:
                print(f"Aluno reprovado com média = {media:.2f}")
            elif media < 5:
                print(f"Aluno de recuperação com média = {media:.2f}")
            else:
                print(f"Aluno aprovado com média = {media:.2f}")