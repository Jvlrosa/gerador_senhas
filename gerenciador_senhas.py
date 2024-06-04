import random
import string

def gerar_senha():
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(10))
    
    if senha[0].isalpha():
        senha = senha[0].upper() + senha[1:]
    return senha

senha_gerada = gerar_senha()
print("Sua senha gerada é:", senha_gerada)

resposta = input('Deseja salvar essa senha? Escreva (s) para sim e (n) para não: \n').lower()

if resposta == 's':
    site = input('deseja salvar essa senha para qual site? \n')

    nome = (senha_gerada)

    with open('minhas_senhas.txt', 'a') as arquivo:
        arquivo.write(site + ' - ' + nome + '\n')

    print("Senha salva com sucesso")
else:
    print("Vc escolheu não salvá-la.")

input()
