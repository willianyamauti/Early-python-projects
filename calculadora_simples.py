"""
operations suported +,-,/,*,**,
"""

while True:

    print()
    num_1 = input('Type the first number ')
    num_2 = input('Type the second number ')
    operacao = input('Type the desired operation(+,-,*,/,^ or any other key to exit:  ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print ('You need to typer numbers!')
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
        print ('EXITING CALCULATOR')
        break
