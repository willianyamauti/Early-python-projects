"""

operacoes +,-,/,*,**,

"""

while True:

    print()
    num_1 = input('Digite o primeiro numero ')
    num_2 = input('Digite o segundo numero ')
    operacao = input('Digite + para adição, - para subtração, * para multiplicaçao'
                     '^ para potenciacão, / para divisão e qualquer outro caractere para sair ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print ('Você precisa digitar um numero')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operacao == '+':
        print(num_1+num_2)
    elif operacao == '-':
        print(num_1-num_2)
    elif operacao == '*':
        print(num_1*num_2)
    elif operacao == '/':
        print(num_1/num_2)
    elif operacao == '^':
        print(num_1**num_2)
    else:
        print ('caculadora encerrada')
        break