senhaGerenciador = 0


def criarConta():
    global senhaGerenciador
    print("\n======= Gerenciador de senhas =======")
    while True:
        try:
            senhaGerenciador = int(input("\nCrie uma senha de 5 dígitos para acessar o geenciador\n"
                                         "(use apenas números)\n"
                                         "(não começe a senha com 0)\n"
                                         "Senha: "))
            if len(str(senhaGerenciador)) == 5 and str(senhaGerenciador)[0] != '-' and senhaGerenciador != 0:
                with open("verificar.txt", "w", encoding="utf-8") as senhas:
                    senhas.write(f"{criptografarSenha('verificar')}")
                print("\nSenha criada com sucesso!!")
                menuInicial()
                break
            else:
                print("\x1b[2J\x1b[1;1H")
                print("\nVocê digitou uma senha inválida, tente novamente")

        except ValueError as e:
            print("\x1b[2J\x1b[1;1H")
            print("\nVocê digitou uma senha inválida, tente novamente")


def excluirConta(primeiroAcesso=False):
    opcao = input("Deseja realmente EXCLUIR a sua conta?\ndigite S para SIM ou N para NÃO: ")
    while opcao == 's' or opcao == 'S' or opcao == 'n' or opcao == 'N':
        if opcao == 'S' or opcao == 's':
            with open('verificar.txt', 'w', encoding='utf8') as verificar:
                verificar.write('')
            with open('senhas_salvas.txt', 'w', encoding='utf-8') as senhas:
                senhas.write('')
                print("\n\nConta excluida com sucesso!!")
                tchau()
                break
        elif opcao == 'N' or opcao == "n" and primeiroAcesso is False:
            menuInicial()
            break
        elif opcao == 'N' or opcao == "n" and primeiroAcesso is True:
            break
    else:
        print("\x1b[2J\x1b[1;1H")
        print("\n**Digite uma opção válida**\n")
        excluirConta()


def acessarConta(senha):
    print("\x1b[2J\x1b[1;1H")
    global senhaGerenciador
    senhaGerenciador = int(senha)
    if verificarSenha() is True:
        menuInicial()
    else:
        print("\x1b[2J\x1b[1;1H")
        acessarConta("Senha incorreta, tente novamente\nSenha: ")


def menuInicial():
    print("\n======= Gerenciador de senhas =======\n")
    while True:
        opcao = input("1 - Ver senhas salvas\n2 - Adicionar uma nova senha\n3 - Excluir conta\n4 - SAIR\n")
        if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
            break

        else:
            print("\x1b[2J\x1b[1;1H")
            print("**Digite uma opção válida**")
            print("\n======= Gerenciador de senhas =======\n")

    if opcao == '1':
        with open("senhas_salvas.txt", "r", encoding="utf-8") as senhas:
            temSenhas = senhas.read()
        if temSenhas:
            mostraSenhas()
            while True:
                opcao = input("1 - Voltar ao menu inicial\n2 - SAIR\n")
                if opcao == '1':
                    print("\x1b[2J\x1b[1;1H")
                    menuInicial()
                    break
                if opcao == '2':
                    tchau()
                    break
                if opcao != '1' and opcao != '2':
                    print("\x1b[2J\x1b[1;1H")
                    print("\n**Digite uma opção válida**")

                else:
                    pass
        else:
            print("\x1b[2J\x1b[1;1H")
            print("**Você não possuí senhas salvas**")
            menuInicial()
    elif opcao == '2':
        nome = input("\nDigite o nome da senha: ")
        senha = input("Senha: ")
        salvarSenha(nome, senha)
        print("\x1b[2J\x1b[1;1H")
        print("\n**Senha adicionada com sucesso!**")
        menuInicial()

    elif opcao == "3":
        print("\x1b[2J\x1b[1;1H")
        excluirConta()

    elif opcao == '4':
        tchau()


def verificarSenha():
    with open("verificar.txt", "r", encoding="utf-8") as verificar:
        v = verificar.read()
    if descriptografarSenha(v) == 'verificar':
        return True


def criptografarSenha(senha):
    global senhaGerenciador
    senha_letras = []
    for letra in senha:
        senha_letras.append(chr(int(ord(letra) + senhaGerenciador)))
    return "".join(senha_letras)


def descriptografarSenha(key):
    global senhaGerenciador
    senha_descrip = []
    for letra in key:
        senha_descrip.append(chr(int(ord(letra) - senhaGerenciador)))
    return ''.join(senha_descrip)


def mostraSenhas():
    print("\x1b[2J\x1b[1;1H")
    with open("senhas_salvas.txt", 'r', encoding='utf-8') as senhasSalvas:
        senhas = senhasSalvas.read().split('\n')[:-1]
        senhasDescrip = ['\n', 'Nome | Senha\n']
        for senha in senhas:
            senhaNome = senha.split(':')[0]
            senhaDescrip = descriptografarSenha(senha.split(':')[-1][1:])
            senhasDescrip.append(f"{senhaNome}: {senhaDescrip}\n")
        print(''.join(senhasDescrip))


def salvarSenha(nome_senha, senha):
    with open("senhas_salvas.txt", "a", encoding="utf-8") as senhas:
        senhas.write(f"{nome_senha}: {criptografarSenha(senha)}\n")


def tchau():
    print("\x1b[2J\x1b[1;1H")
    print("Encerrando programa\n")
    print(
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣀⠈⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⡄⠄⠉⠙⠓⢦⡀⠈⠻⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⠛⠛⠉⠋⠄⣠⣤⣄⠄⠄⠂⠤⣄⠈⠳⣄⠄⢹⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⡟⠁⠄⣰⣶⣦⡀⠻⣿⣿⣷⣄⠄⠄⢸⡆⠄⣿⠄⠄⠈⠉⠻⣿⣿\n"
        "⣿⣿⣿⡿⠁⢠⣴⣶⣌⠹⣿⣿⣷⣍⠻⣿⣿⣶⣄⠄⠄⠄⠄⣰⣾⣶⡆⠄⣿⣿\n"
        "⣿⣿⣿⣇⠄⠈⠻⣿⣿⣧⡈⠻⣿⣿⣷⣌⠻⣿⣿⣷⡄⠄⠄⣿⣿⣿⡇⠄⣿⣿\n"
        "⣿⣿⣿⣿⠃⢀⣠⣀⠙⢿⣿⣷⣄⠻⣿⣿⣿⣾⣿⣿⣿⣷⠄⣿⣿⣿⡇⠄⣿⣿\n"
        "⣿⣿⣿⣿⠄⠸⢿⣿⣷⣌⠻⢿⣿⣦⣈⣿⣿⣿⣿⣿⢟⣡⣾⣿⣿⣿⡇⠄⣿⣿\n"
        "⣿⣿⠟⠋⠁⠄⠄⠙⢿⣿⣷⣄⢹⣿⣿⣿⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⡇⠄⣿⣿\n"
        "⣿⣿⠄⠠⡆⠄⢰⡀⠄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣏⠸⣿⣿⣿⣿⣿⣿⡇⠄⣿⣿\n"
        "⣿⣿⠄⠄⢻⡀⠈⠳⣤⡄⠄⠙⢿⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⠇⠄⣿⣿\n"
        "⣿⣿⣷⣄⠄⠑⢦⣄⣀⡀⠄⢀⠄⠙⠿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⠏⠄⢠⣿⣿\n"
        "⣿⣿⣿⣿⣶⣄⠄⠈⠉⠁⠄⣸⣿⣄⠄⠈⠻⣿⣿⣿⣿⣿⣿⠿⠃⠄⣠⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⢀⢀⢀⢀⢀⢀⣠⣴⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "tchau"
    )
