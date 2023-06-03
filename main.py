from funcoes import acessarConta, criarConta

with open("senhas_salvas.txt", "r", encoding="utf-8") as senhas:
    temSenhas = senhas.read()

if temSenhas:
    while True:
        try:
            acessarConta(int(input("Digite sua senha de acesso\nSenha: ")))
        except:
            print('Você digitou a senha errada, tente novamente')
else:
    criarConta()



