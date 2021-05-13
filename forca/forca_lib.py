from os import system, name
from time import sleep
import random

#limpar tela
def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#checa se a palavra é invalida e retorna True para invalida e False para valida
def check_palavra(palavra):
    checagem = any(caractere.isdigit() for caractere in palavra)
    if checagem == True or palavra.count(' ') > 0:
        print(f'A palavra não pode conter numeros ou espaços!!!'
              f'Tente de novo')
    return checagem

#transforma a palavra em __________ de acordo com o nunmero de letras
def esconder_palavra(palavra):
    palavra_escondida = ''
    for letra_secreta in palavra:
        palavra_escondida += '_'
    return palavra_escondida

def morrreu(vidas,arte,palavra):
    if vidas == 6:
        print(arte[6])
        print(f'Você morreu!!!\n'
              f'A palavra secreta era {palavra.upper()}, Jogador 2 ganhou')
        return True
    else:
        return False

def imprimir_status(arte,palavra_escondida,tentativas):
    print(arte[tentativas], palavra_escondida)
    print(f'Chances restantes: {6 - tentativas}')

def conferir_letra(digitadas, letra, palavra,tentativas):
    digitadas.append(letra)
    if letra not in palavra:
        tentativas += 1
        digitadas.pop()
    return digitadas, tentativas

def atualizar_palavra_escondida(digitadas,palavra):
    secreto = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            secreto += letra_secreta
        else:
            secreto += '_'
    return secreto

def fim_de_jogo(arte,secreto,palavra,tentativas):
    if secreto == palavra:
        print(f'{arte[tentativas]} {secreto}'
              f'{arte[7]}\n\n'
              f'Você acertou a palavra secreta "{palavra.upper()}" com {tentativas} erros (s)!\n'
              f'O Jogador 1 ganhou')
        return True

def computador_escolher(lista_palavras):
    palavra = random.choice(lista_palavras)
    return palavra

def print_logo(logo):
    print(logo)