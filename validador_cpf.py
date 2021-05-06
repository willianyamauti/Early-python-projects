"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

while True:
    cpf = input('Digite o cpf: ')
    cpf = cpf.replace('.', '').replace('-', '')

    print(cpf)
    if not cpf.isnumeric() or len(cpf) != 11:
        print(f'CPF invalido digite novamente! '
              f'(o cpf deve não deve possuir letras e deve ter 11 numeros)')
        continue

    novo_cpf = []
    for n in cpf:
        novo_cpf.append(int(n))

    digito_1 = 0
    digito_2 = 0
    x = 0

    # p = 3 (p += 1)  r = 11 (r -= 1)
    for p, r in enumerate (range(11, 2, -1), 3):
        digito_1 += novo_cpf[p-3] * (r-1)
        digito_2 += novo_cpf[p-3] * r
        x += 1
        print(f'p = {p}')
        print(f'r = {r}')
        print(f'{novo_cpf[p-3]} x {r-1} = {digito_1}/{novo_cpf[p-3]} x {r} = {digito_2}')

    digito_1 = 11 - (digito_1 % 11)
    print(digito_1)
    digito_1_verificao = (digito_1 > 9)
    print(digito_1_verificao)
    digito_1 = 0 if digito_1_verificao else digito_1
    print(digito_1)
    digito_2 = 11 - ((digito_2 + (digito_1 * 2)) % 11)
    print(digito_2)


    *digitos, n1_, n2_ = novo_cpf
    digitos.append(digito_1)
    digitos.append(digito_2)

    novo_cpf = ''.join([str(numero) for numero in digitos])

    print(novo_cpf)

    msg = 'Esse CPF é valido' if novo_cpf == cpf else 'Esse cpf é invalido'
    print(msg)
