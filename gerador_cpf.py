from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero
print(novo_cpf)
fator = 11
soma_digito_1 = 0
soma_digito_2 = 0

for index in range(0, 9, 1):
    soma_digito_1 += int(novo_cpf[index]) * (fator - 1)
    soma_digito_2 += int(novo_cpf[index]) * fator
    fator -= 1

digito_ver_1 = 11 - (soma_digito_1 % 11)
digito_ver_1 = 0 if digito_ver_1 > 9 else digito_ver_1  # se digito_ver > 9 -> 0
digito_ver_2 = 11 - ((soma_digito_2 + (digito_ver_1 * 2)) % 11)
digito_ver_2 = 0 if digito_ver_2 > 9 else digito_ver_2

novo_cpf += str(digito_ver_1) + str(digito_ver_2)

print(f'CPF: {novo_cpf}')
