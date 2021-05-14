"""
Cifra de cesar

to-do:
colocar outros modos de encripitacao
encriptar numeros e simbolos

"""
import cifra_lib as cifra
import cifra_buffer as buffer

print(buffer.logo)
fim = False
while not fim:
    opcao = input("Digite 'codificar' para encriptar, 'decodificar' para decifrar: \n")
    if not opcao == 'codificar' and not opcao == 'decodificar':
        print("Digite uma das duas opções!")
        continue
    mensagem = input("Digite a mensagem:\n").lower()
    rotacao = int(input("Digite o numero de deslocamentos:\n"))
    if rotacao > 26:
        rotacao = rotacao % 26
    cifra.cesar(mensagem, rotacao, opcao)
    continuar = input("Digite y para continuar, ou qualquer outra tecla para sair.\n")
    if continuar == 'n':
        fim = True
print("O programa será encerrado")