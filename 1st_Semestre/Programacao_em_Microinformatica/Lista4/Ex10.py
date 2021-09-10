while True:
    print("Informe o intervalo: ")
    ini = int(input("Inicio >> "))
    fim = int(input("Fim    >> "))
    if ini > fim:
        ini, fim = fim, ini
    soma = 0
    for n in range(ini,fim+1):
        soma += n
    print(f"A soma dos numeros entre {ini} e {fim} eh {soma}")

    resp = input("Deseja entrar com outro intervalo? [S/N]")
    if resp != 'S':
        break