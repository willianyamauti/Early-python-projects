"""

Jogo da forca v.0.01

Nessa versao o programa usa as funções getpass e any e map para conferir se a string possui digitos

#
    paalavra = getpass.getpass(prompt ='')

#   string = 'abc2'
    resultado = any(chr.isdigit() for chr in strin) #retorna o valor em bool

Nesta versao o jogo funciona apenas no terminal


to do:
- adicionar banco de dados de palavra aleatorias
- mais modos de jogo

"""

print('''       
       __    ______     _______   ______       _______       ___      
      |  |  /  __  \   /  _____| /  __  \     |       \     /   \     
      |  | |  |  |  | |  |  __  |  |  |  |    |  .--.  |   /  ^  \      
.--.  |  | |  |  |  | |  | |_ | |  |  |  |    |  |  |  |  /  /_\  \   
|  `--'  | |  `--'  | |  |__| | |  `--'  |    |  '--'  | /  _____  \                
 \______/   \______/   \______|  \______/     |_______/ /__/     \__\ 
                                                                      
 _______   ______   .______        ______     ___      
|   ____| /  __  \  |   _  \      /      |   /   \     
|  |__   |  |  |  | |  |_)  |    |  ,----'  /  ^  \    
|   __|  |  |  |  | |      /     |  |      /  /_\  \   
|  |     |  `--'  | |  |\  \----.|  `----./  _____  \  
|__|      \______/  | _| `._____| \______/__/     \__\ 


      ________       ___________________ 
     |/      |    /                   |
     |      (_) <  by Satoshi v.0.01  |
     |      \|/   \ __________________|
     |       |
     |      / \ 
     |
    _|___
                                                                
Regras:

* O primeiro jogador deve escolher uma palavra
* O segundo jogador deve adivinhar a palavra em até 6 tentativas                                                                
                                                                
''')

vidas = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',"""
     _\|/^
      (_oo 
       |     
      /|\ 
       |
       LL"""]

import getpass

while True:

    tentativas = 0
    digitadas = []
    buffer_palavra = ''

    palavra_secreta = getpass.getpass(prompt = 'Digite a palavra secreta: ')
    checagem = any(caractere.isdigit() for caractere in palavra_secreta)

    if checagem == True:
        print(f'A palavra não pode conter numeros!!!'
              f'Tente de novo')
        continue

    for letra_secreta in palavra_secreta:
        buffer_palavra += '_'

    while True:

        if tentativas == 6:
            print(vidas[6])
            print(f'Você morreu!!!\n'
                  f'A apalvra secreta era {palavra_secreta.upper()}, Jogador 2 ganhou')
            break

        else:

            print(vidas[tentativas], buffer_palavra)
            print(f'Chances restantes: {6 - tentativas}')
            letra = input('Digite uma letra: ')

            if len(letra) > 1 or letra.isdigit() == True:
                print('Digite corretamente, apenas uma letra e sem numeros!!! ;< ')
                continue

            digitadas.append(letra)

        if letra not in palavra_secreta:
            tentativas += 1
            digitadas.pop()

        buffer_palavra =''
        for letra_secreta in palavra_secreta:
            if letra_secreta in digitadas:
                buffer_palavra += letra_secreta
            else:
                buffer_palavra += '_'

        if buffer_palavra == palavra_secreta:
            print(f'{ vidas[7]}\n\n'
                  f'Você acertou a palavra secreta "{palavra_secreta.upper()}" com {tentativas} erros (s)!\n'
                  f'O Jogador 1 ganhou')
            break

    opcao = input(f'Deseja continuar jogando?\n'
                  f'Pressione s para continuar,ou qualquer outra tecla para sair: ')

    if opcao == 's':
        continue

    else:
        print('Fim de jogo')
        break