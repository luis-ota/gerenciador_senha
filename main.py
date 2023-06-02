from classes import Senha

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
    senha = Senha(nome_senha=input("Digite o nome da senha: "), senha=input("Digite a senha: "))
    senha.criptografar(senha.senha)
    senha.salvar()
