from classes import salvarSenhas, mostraSenhas

print("======= Gerenciador de senhas =======")
while True:
    opcao = input("1 - Ver senhas salvar\n2 - Adicionar uma nova senha\n-aperte ENTER para sair-\n")
    if opcao == '1' or opcao == '2' or opcao == '':
        break

    else:
        print("Digite uma opção válida")

if opcao == '1':
    pass
elif opcao == '2':
    while True:
        salvarSenhas(input("Digite o nome da senha: "),
                     input("Senha: "))
        if input("Deseja salvar outra senha?\n1 - SIM\n2 - NÃO\n") == '1':
            continue
        else:
            break
