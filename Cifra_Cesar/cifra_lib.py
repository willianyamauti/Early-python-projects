import cifra_buffer as buffer


def cesar(mensagem, rotacao, opcao):
    mensagem_final = ""
    if opcao == 'decodificar':
        rotacao *= -1
    for letra in mensagem:
        if letra in buffer.alfabeto:
            index = buffer.alfabeto.index(letra)
            mensagem_final += buffer.alfabeto[index + rotacao]
        else:
            mensagem_final += letra
    print(f'Após {opcao}, a mensagem ficou: {mensagem_final}\n')
