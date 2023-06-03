senhaGerenciador = 0
tentativa = 0
import os


def criarConta():
    global senhaGerenciador
    print("\n======= Gerenciador de senhas =======")
    while True:
        try:
            senhaGerenciador = int(input("\nCrie uma senha de 6 números para acessar o geenciador\nSenha: "))
            if len(str(senhaGerenciador)) == 6 and senhaGerenciador > 0:
                with open("verificar.txt", "w", encoding="utf-8") as senhas:
                    senhas.write(f"{criptografarSenha('verificar')}")
                menuInicial()
            else:
                print("\nVocê digitou uma senha inválida, tente novamente")

        except ValueError as e:
            print("\nVocê digitou uma senha inválida, tente novamente")
            print(e)


def acessarConta(senha):
    global senhaGerenciador
    senhaGerenciador = senha
    if verificarSenha() is True:
        menuInicial()
    else:
        acessarConta("Você digitou a senha errada, tente novamente\nSenha: ")


def verificarSenha():
    global tentativa
    tentativa += 1
    if tentativa == 4:
        print("Você errou a senha de acesso muitas vezes, encerrando programa")
        os._exit()
    with open("verificar.txt", "r", encoding="utf-8") as verificar:
        v = verificar.read()
    if descriptografarSenha(v) == 'verificar':
        return True


def criptografarSenha(senha):
    global senhaGerenciador
    senha_letras = []
    for letra in senha:
        senha_letras.append(chr(ord(letra) + senhaGerenciador))
    return "".join(senha_letras)


def descriptografarSenha(key):
    global senhaGerenciador
    senha_descrip = []
    for letra in key:
        senha_descrip.append(chr(ord(letra) - senhaGerenciador))
    return ''.join(senha_descrip)


def mostraSenhas():
    pass


def salvarSenha(nome_senha, senha):
    with open("senhas_salvas.txt", "a", encoding="utf-8") as senhas:
        senhas.write(f"{nome_senha}: {criptografarSenha(senha)}\n")


def menuInicial():
    print("\n======= Gerenciador de senhas =======\n")
    while True:
        opcao = input("1 - Ver senhas salvar\n2 - Adicionar uma nova senha\n3 - SAIR\n")
        if opcao == '1' or opcao == '2' or opcao == '3':
            break

        else:
            print("Digite uma opção válida")

    if opcao == '1':
        mostraSenhas()
    elif opcao == '2':
        while True:
            salvarSenha(input("Digite o nome da senha: "),
                        input("Senha: "))

            if input("Deseja salvar outra senha?\n1 - SIM\n2 - NÃO\n") == '1':
                continue
            else:
                continue
    elif opcao == '3':
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
        os._exit(0)
