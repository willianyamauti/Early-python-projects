"""

Jogo da forca v.0.01

Nessa versao o programa usa as funções getpass e any e map para conferir se a string possui digitos

#
    paalavra = getpass.getpass(prompt ='')

#   string = 'abc2'
    resultado = any(chr.isdigit() for chr in strin) #retorna o valor em bool

Nesta versao o jogo funciona apenas no terminal

to do:

diminuir o tamnha do codigo criando mais funções


bugs:

"""
from forca_arte import logo, vidas
import forca_lib
from forca_palavras import lista_palavras
import getpass

forca_lib.print_logo(logo)
while True:

    tentativas = 0
    digitadas = []

    modo_jogo = input(f'Para jogar sozinho contra o computador escolha 1, para jogar contra outro'
                      f'jogador escolha 2: ')
    if not modo_jogo.isdigit():
        print('Digite uma opção valida!')
        continue
    modo_jogo = int(modo_jogo)
    if modo_jogo != 1 and modo_jogo != 2:
        print('Digite uma opção valida!')
        continue

    if modo_jogo == 1:
        palavra_secreta = forca_lib.computador_escolher(lista_palavras)
        palavra_escondida = forca_lib.esconder_palavra(palavra_secreta)
        while True:
            if forca_lib.morrreu(tentativas, vidas, palavra_secreta):
                break
            else:
                forca_lib.clear()
                forca_lib.imprimir_status(vidas, palavra_escondida, tentativas)
                letra = input('Digite uma letra: ')
                if len(letra) > 1 or letra.isdigit() == True:
                    print('Digite corretamente, apenas uma letra e sem numeros!!! ;< ')

                    continue
                digitadas, tentativas = forca_lib.conferir_letra(digitadas,letra,palavra_secreta,tentativas)
            palavra_escondida = forca_lib.atualizar_palavra_escondida(digitadas,palavra_secreta)
            if forca_lib.fim_de_jogo(vidas, palavra_escondida, palavra_secreta, tentativas):
                break

        opcao = input(f'Deseja continuar jogando?\n'
                      f'Pressione s para continuar,ou qualquer outra tecla para sair: ')
        if opcao == 's':
            continue
        else:
            break


    elif modo_jogo == 2:
        palavra_secreta = getpass.getpass(prompt='Digite a palavra secreta: ')
        if forca_lib.check_palavra(palavra_secreta):
            continue
        else:
            palavra_secreta = palavra_secreta.lower()
            palavra_escondida = forca_lib.esconder_palavra(palavra_secreta)

        while True:
            if forca_lib.morrreu(tentativas, vidas, palavra_secreta):
                break
            else:
                forca_lib.clear()
                forca_lib.imprimir_status(vidas, palavra_escondida, tentativas)
                letra = input('Digite uma letra: ')
                if len(letra) > 1 or letra.isdigit() == True:
                    print('Digite corretamente, apenas uma letra e sem numeros!!! ;< ')

                    continue
                digitadas, tentativas = forca_lib.conferir_letra(digitadas,letra,palavra_secreta,tentativas)
            palavra_escondida = forca_lib.atualizar_palavra_escondida(digitadas,palavra_secreta)
            if forca_lib.fim_de_jogo(vidas, palavra_escondida, palavra_secreta, tentativas):
                break

        opcao = input(f'Deseja continuar jogando?\n'
                      f'Pressione s para continuar,ou qualquer outra tecla para sair: ')
        if opcao == 's':
            continue
        else:
            break

print('FIM DE JOGO!!!')
