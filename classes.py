key = ''
def crip_key(senha_usuario, pergunta_red=None, redefinir=False):
    if redefinir:
        pass
    else:
        key_letras = []
        for letra in senha_usuario:
            key_letras.append(chr(ord(letra) + 69))
        key = ("".join(key_letras))
        return key


def descrip_key(key):
    senha_descrip = []
    for letra in key:
        senha_descrip.append(chr(ord(letra) - 69))
    return ''.join(senha_descrip)


def criar_senha_gerenciador():
    print("======= Gerenciador de senhas =======")
    senha = input("Crie uma senha para o gerenciador de pelo menos 6 letras\nSenha: ")
    # pergunta = input("responda uma pergunta de segurança: ")

    with open("senhas_gerenciador.txt", "w", encoding="utf-8") as senhas:
        senhas.write(crip_key(senha), )


class Senha:
    def __init__(self, nome_senha, senha, key=key):
        self.nome_senha = nome_senha
        self.key = key
        self.senha = senha

    def criptografar(self, senha, key=key):
        pass

    def descriptografar(self, senha_c):
        pass

    def salvar(self):
        with open("senhas_salvas.txt", "a", encoding="utf-8") as senhas:
            senhas.write(f"{self.nome_senha}: {self.senha}\n")
