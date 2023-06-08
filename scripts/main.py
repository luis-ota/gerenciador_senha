from funcoes import acessarConta, criarConta, excluirConta

with open("verificar.txt", "r", encoding="utf-8") as senhas:
    temConta = senhas.read()

a = True
primeiroAcesso = True
tentativa = 0
opcao = ''
if temConta:
    while a:
        try:
            if primeiroAcesso:
                opcao = input("1 - Acessar conta\n2 - EXCLUIR conta\n")
                while True:
                    if opcao == '1':
                        primeiroAcesso = False
                        print("\x1b[2J\x1b[1;1H")
                        break
                    elif opcao == '2':
                        break
                    else:
                        print("\x1b[2J\x1b[1;1H")
                        print("**Você digitou uma opção inválida**\n")
                        break
            if opcao == '1':
                acessarConta(int(input("Digite sua senha de acesso\nSenha: ")))
                a = False
            elif opcao == '2':
                excluirConta(primeiroAcesso=True)
                a = False
                break
        except ValueError as e:
            tentativa += 1
            if tentativa == 4:
                print("\x1b[2J\x1b[1;1H")
                print(f'{chr(128545)}{chr(128545)}{chr(128545)}{chr(128545)}{chr(128545)}\n'
                      "\nVocê errou a senha mais de 3 vezes, encerrando programa")
                a = False
            else:
                print(f'\nSenha incorreta, tente novamente')
        except:
            tentativa += 1
            print("**Senha inválida, tente uma nova senha**")

    exit()
else:
    criarConta()
