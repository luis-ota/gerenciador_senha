senha_gerenciador = 1000


def criptografarSenha(senha):
    senha_letras = []
    for letra in senha:
        senha_letras.append(chr(ord(letra) + senha_gerenciador))
    return "".join(senha_letras)


def descriptografarSenha(key):
    senha_descrip = []
    for letra in key:
        senha_descrip.append(chr(ord(letra) - senha_gerenciador))
    return ''.join(senha_descrip)


def mostraSenhas():
    pass


def salvarSenhas(nome_senha, senha):
    with open("senhas_salvas.txt", "a", encoding="utf-8") as senhas:
        senhas.write(f"{nome_senha}: {criptografarSenha(senha)}\n")