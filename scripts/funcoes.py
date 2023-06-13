from getpass import getpass


senhaGerenciador = 0
listaSenhas = []


def criarConta():
    global senhaGerenciador
    print("\n======= Gerenciador de senhas =======")
    while True:
        try:
            senhaGerenciador = int(getpass("\nCrie uma senha de 5 dígitos para acessar o geenciador\n"
                                         "(use apenas números)\n"
                                         "(não começe a senha com 0)\n"
                                         "Senha: "))
            if len(str(senhaGerenciador)) == 5 and str(senhaGerenciador)[0] != '-' and senhaGerenciador != 0:
                with open("verificar.txt", "w", encoding="utf-8") as verificar:
                    verificar.write(f"{criptografarSenha('verificar')}")
                    verificar.close()
                print("\nSenha criada com sucesso!!")
                menuInicial()
                break
            else:
                print("\x1b[2J\x1b[1;1H")
                print("\nVocê digitou uma senha inválida, tente novamente")

        except ValueError:
            print("\x1b[2J\x1b[1;1H")
            print("\nVocê digitou uma senha inválida, tente novamente")


def excluirConta(primeiroAcesso=False):
    opcao = input("Deseja realmente EXCLUIR a sua conta?\ndigite S para SIM ou N para NÃO: ")
    while opcao == 's' or opcao == 'S' or opcao == 'n' or opcao == 'N':
        if opcao == 'S' or opcao == 's':
            with open('verificar.txt', 'w', encoding='utf8') as verificar:
                verificar.write('')
                verificar.close()
            with open('senhas_salvas.txt', 'w', encoding='utf-8') as senhas:
                senhas.write('')
                senhas.close()
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
    global listaSenhas
    print("\n======= Gerenciador de senhas =======\n")
    while True:
        opcao = input("1 - Ver senhas salvas\n"
                      "2 - Adicionar uma nova senha\n"
                      "3 - Excluir conta\n"
                      "4 - SAIR\n")
        if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
            break

        else:
            print("\x1b[2J\x1b[1;1H")
            print("**Digite uma opção válida**")
            print("\n======= Gerenciador de senhas =======\n")

    if opcao == '1':
        with open("senhas_salvas.txt", "r", encoding="utf-8") as senhas:
            temSenhas = senhas.read()
            senhas.close()
        if temSenhas:
            print("\x1b[2J\x1b[1;1H")
            mostraSenhas()
            while True:
                opcao = input("----------------------------------------\n\n"
                              "1 - Adicionar senha\n"
                              "2 - Atualizar senha\n"
                              "3 - Remover senha\n"
                              "4 - Voltar ao menu inicial\n"
                              "5 - SAIR\n")
                if opcao == '1':
                    nome = input("\nDigite o nome da senha (0 para cancelar): ")
                    if nome == '0':
                        menuInicial()
                        break
                    else:
                        adicionarSenha(nome, input("Senha: "))
                        print("\x1b[2J\x1b[1;1H")
                        print("\n**Senha adicionada com sucesso!!**")
                        menuInicial()
                        break
                if opcao == '2':
                    print("\x1b[2J\x1b[1;1H")
                    with open("senhas_salvas.txt", 'r', encoding='utf-8') as senhasLeitura:
                        listaSenhas = senhasLeitura.read().split('\n')[:-1]
                        senhasLeitura.close()
                    while True:
                        try:
                            mostraSenhas()
                            idSenha = int(input("Digite o ID da senha que deseja atualizar (0 para cancelar): "))
                            if idSenha in range(1, len(listaSenhas) + 1):
                                atualizarSenha(idSenha)
                                break
                            elif idSenha == 0:
                                print("\x1b[2J\x1b[1;1H")
                                menuInicial()
                                break
                            else:
                                print("\x1b[2J\x1b[1;1H")
                                print('**Digite uma opção valida**')
                                continue
                        except:
                            print("\x1b[2J\x1b[1;1H")
                            print('**Digite uma opção valida**')
                            continue
                    break

                elif opcao == '3':
                    print("\x1b[2J\x1b[1;1H")
                    with open("senhas_salvas.txt", 'r', encoding='utf-8') as senhasLeitura:
                        listaSenhas = senhasLeitura.read().split('\n')[:-1]
                        senhasLeitura.close()
                    while True:
                        try:
                            mostraSenhas()
                            idSenha = int(input("Digite o ID da senha que deseja remover (0 para cancelar): "))
                            if idSenha in range(1, len(listaSenhas) + 1):
                                removerSenha(idSenha)
                                break
                            elif idSenha == 0:
                                print("\x1b[2J\x1b[1;1H")
                                menuInicial()
                                break
                            else:
                                print("\x1b[2J\x1b[1;1H")
                                print('\n**Digite uma opção valida**')
                                continue
                        except:
                            print("\x1b[2J\x1b[1;1H")
                            print('\n**Digite uma opção valida**')
                            continue
                    break
                if opcao == '4':
                    print("\x1b[2J\x1b[1;1H")
                    menuInicial()
                    break
                if opcao == '5':
                    tchau()
                    break
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                    print("\x1b[2J\x1b[1;1H")
                    print("\n**Digite uma opção válida**")
                else:
                    pass
        else:
            print("\x1b[2J\x1b[1;1H")
            print("**Você não possuí senhas salvas**")
            menuInicial()
    elif opcao == '2':
        adicionarSenha(input("\nDigite o nome da senha: "), input("Senha: "))
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
        verificar.close()
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
    with open("senhas_salvas.txt", 'r', encoding='utf-8') as senhasSalvas:
        senhas = senhasSalvas.read().split('\n')[:-1]
        senhasDescrip = ['\n ID |        Nome        |         Senha\n'
                         '----------------------------------------\n']
        for senha in senhas:
            senhaNome = senha.split(':')[0]
            senhaDescrip = descriptografarSenha(senha.split(':')[-1][1:])
            senhasDescrip.append(f" {senhas.index(senha) + 1:<5} {senhaNome:^17} {senhaDescrip:>15}\n")
        print(''.join(senhasDescrip))
        senhasSalvas.close()


def atualizarSenha(idSenha):
    global listaSenhas
    print("\x1b[2J\x1b[1;1H")
    with open("senhas_salvas.txt", 'w', encoding='utf-8') as senhasEscrita:
        print(f"Você está atualizando a senha: {listaSenhas[int(idSenha) - 1].split(': ')[0]}\n")
        listaSenhas[int(idSenha) - 1] = f"{input('Digite o novo nome da senha: ')}: " \
                                        f"{criptografarSenha(input('Digite a nova senha: '))}"

        listaSenhasCorrigida = []
        for senha in listaSenhas:
            senha += '\n'
            listaSenhasCorrigida.append(senha)
        senhasAtualizadas = "".join(listaSenhasCorrigida)
        senhasEscrita.write(senhasAtualizadas)
        senhasEscrita.close()
        print("\x1b[2J\x1b[1;1H")
        print("\n**Senha atualizada com sucesso!!**")
        menuInicial()


def removerSenha(idSenha):
    global listaSenhas
    print("\x1b[2J\x1b[1;1H")
    with open("senhas_salvas.txt", 'w', encoding='utf-8') as senhasEscrita:
        del listaSenhas[int(idSenha) - 1]
        listaSenhasCorrigida = []
        for senha in listaSenhas:
            senha += '\n'
            listaSenhasCorrigida.append(senha)
        senhasAtualizadas = "".join(listaSenhasCorrigida)
        senhasEscrita.write(senhasAtualizadas)
        senhasEscrita.close()
        print("\x1b[2J\x1b[1;1H")
        print("\n**Senha removida com sucesso!!**")
        menuInicial()


def adicionarSenha(nomeSenha, senha):
    with open("senhas_salvas.txt", "a", encoding="utf-8") as senhas:
        senhas.write(f"{nomeSenha}: {criptografarSenha(senha)}\n")
        senhas.close()


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
        "tchau\n"
        "Desenvolido por GDP® LTDA 2023"
    )
