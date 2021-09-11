'''
8.	Leia uma data e determine se ela é válida.
Ou seja, veriﬁque se o mês está entre 1 e 12, e se o dia existe naquele mês.
Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
'''

print("Informe uma data")
dia = int(input("Dia >> "))
mes = int(input("Mês >> "))
ano = int(input("Ano >> "))
valid = False
if 1 <= mes <= 12:
    if mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if 1 <= dia <= 29:
                valid = True
        else:
            if 1 <= dia <= 28:
               valid = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1 <= dia <= 30:
            valid = True
    else:
        if 1 <= dia <= 31:
            valid = True

if valid: # é a mesma coisa que comparar if valid == True:
    print("Data válida!!")
else:
    print("Data inválida!!")