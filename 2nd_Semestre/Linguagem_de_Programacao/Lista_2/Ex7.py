def verifica(data):
    data = data.split("/")
    data = "".join(data)
    if data.isalnum:
        if len(data) == 8:
            return True
    

def valida(data):
    data = data.split("/")
    dia = data[0]
    mes = data[1]
    ano = data[2]
    print("cheguei aqui")



data = input("digite uma data [dd/mm/aa]")
if verifica(data):
    valida(data)