import os
import time

tabela = {} #Dicionario Global
#----------------------------------------Estilo--------------------------------------------
def retorna_menu():
    os.system('cls')
    print("Retornando ao menu em inicial em:")
    time.sleep(1)
    print("3..")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1..")
    time.sleep(1)
    os.system('cls')

def senha_invalida():
    os.system('cls')
    print("\033[7;31mSenha Inválida!!!\33[m")
    time.sleep(1)
    os.system('cls')
    print("\033[0;31mSenha Inválida!!!\33[m")
    time.sleep(1)
    os.system('cls')
    print("\033[7;31mSenha Inválida!!!\33[m")
    time.sleep(1)
    os.system('cls')
    

def opcao_inva():
    os.system('cls')
    print("\033[7;31mOpção Invalida!!!\33[m")
    time.sleep(1)
    os.system('cls')
    print("\033[0;31mOpção Invalida!!!\33[m")
    time.sleep(1)
    os.system('cls')
    print("\033[7;31mOpção Invalida!!!\33[m")
    time.sleep(1)
    os.system('cls')
    print("\033[0;31mOpção Invalida!!!\33[m")
    time.sleep(1)


def operac_finali():
    os.system('cls')
    print("Operação Finalizada!!!")
    time.sleep(1)
    os.system('cls')
    print("")
    time.sleep(1)
    os.system('cls')
    print("Operação Finalizada!!!")
    time.sleep(1)
    os.system('cls')
    print("")
    time.sleep(1)
    os.system('cls')
    print("Operação Finalizada!!!")
    time.sleep(1)
    os.system('cls')

def login():
    os.system('cls')
    print("Login Efetuado!!!")
    time.sleep(1)
    os.system('cls')
    print("")
    time.sleep(1)
    os.system('cls')
    print("Login Efetuado!!!")
    time.sleep(1)
    os.system('cls')
    print("")
    time.sleep(1)
    os.system('cls')
    print("Login Efetuado!!!")
    time.sleep(1)
    os.system('cls')

def err_login():
    os.system('cls')
    print("Usuário ou senha incorretos!!!")
    time.sleep(1)
    os.system('cls')
    print("")
    time.sleep(1)
    os.system('cls')
    print("Usuário ou senha incorretos!!!")
    time.sleep(1)
    os.system('cls')
    print("")
    time.sleep(1)
    os.system('cls')
    print("Usuário ou senha incorretos!!!")
    time.sleep(1)
    os.system('cls')
#-------------------------------------Funçoes------------------------------------------------
def criptog(x):
    l = list(x)
    for i in range(len(l)):
        l[i] = chr(ord(l[i])+3)
    j = "".join(l)
    return j

def verifica(usr):
    
    if usr not in tabela:
        print(f"Digite uma senha para o usuário {usr}.")
        pws = input(">>> ")
        pws = criptog(pws)
        tabela[usr] = pws
        os.system('cls')
        print("Usuário cadastrado com sucesso!!!")
        time.sleep(1)
        operac_finali()
        retorna_menu()
        
    else:
        print("Usuário encontrado!!!")
        op = input(f"Deseja alterar a senha de {usr}?[S/N]\n>>> ").upper()
        match op:
            case 'S':
                print("Digite sua senha atual: ")
                pws = input(">>> ")
                pws = criptog(pws)
                for k, v in tabela.items():
                    if k==usr and v == pws:
                        tabela[usr] = input("Digite a nova senha:\n>>> ")
                        print("Senha alterada com sucesso!!!")
                        operac_finali()
                        retorna_menu()
                    else:
                        senha_invalida()
                        time.sleep(1)
                        retorna_menu()
            case 'N':
                operac_finali()
                retorna_menu()
            case _:
                opcao_inva()
                retorna_menu()
 #-----------------------------------------Main-----------------------------------------------           


while True:
    os.system('cls')
    print("-"*40)
    print("\t\t MENU \t\t")
    print("-"*40)
    op = int(input("Digite o numero da operação escolhida:\n1 - Cadastro\n2 - Realizar Login\n3 - Relatório de Usuários\n4 - Encerrar\n"+"-"*40+"\n>>> "))
    print("-"*40)
    match op:
        case 1:
            os.system('cls')
            print("-"*40)
            print("\t\tCADASTRO \t\t")
            print("-"*40)
            cad = input("Digite um nome de usuário: \n>>> ")
            verifica(cad)
        case 2:
            os.system('cls')
            print("-"*40)
            print("\t\tLogin\t\t")
            print("-"*40)
            usr = input("Digite seu usuário: ")
            pws = input("Digite sua senha: ")
            pws = criptog(pws)
            if tabela[usr] == pws:
                login()
                retorna_menu()
            else:
                err_login()
                retorna_menu()
        case 3:
            os.system('cls')
            print("-"*32)
            print("\t    RELATORIO \t\t")
            print("-"*32)
            for i in tabela:
                print(i)
            print("-"*32)
            sair = input("Entre com alguma tecla para sair.\n>>> ")
            retorna_menu()
        case 4: 
            os.system('cls')
            op = input("Deseja realmente encerrar o programa?[S/N]\n>>> ").upper()
            match op:
                case 'S':
                    operac_finali()
                    break
                case 'N':
                    retorna_menu()
                case _:
                    opcao_inva()
                    retorna_menu()
            
        case _:
            opcao_inva()
            retorna_menu()

            
    
  


    

    