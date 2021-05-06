"""
Algoritmo para medir o tempo vivido, atualmente o codigo computa sua idade
e retorna os dados para : sua idade atual e o restante de tempo disponivel até 80 anos

v 0.01

#adicionado calculo para ano bisexto


"""
while True:

    ano = input('Qual ano você nasceu?: ')

    if not ano.isdigit():
        print('ano invalido,  o valor precisa ser um numero')
        continue

    else :
        ano = int(ano)
        ano_flag = ano
        idade = 2021 - ano
        dias_vividos = 0

        for x in range(idade):
            if ano%4 != 0:
                dias_vividos += 365
                ano_flag += 1

            else :
                if ano % 100 != 0:
                    dias_vividos += 366
                    ano_flag += 1
                elif ano % 400 != 0:
                    dias_vividos += 365
                    ano_flag += 1
                else:
                    dias_vividos += 366
                    ano_flag += 1

        dias_vividos_idade = dias_vividos

        for x in range(80-idade):
            if ano%4 != 0:
                dias_vividos += 365
                ano_flag += 1

            else :
                if ano % 100 != 0:
                    dias_vividos += 366
                    ano_flag += 1
                elif ano % 400 != 0:
                    dias_vividos += 365
                    ano_flag += 1
                else:
                    dias_vividos += 366
                    ano_flag += 1

        dias_vividos_80 = dias_vividos

        print(f'você ja viveu {dias_vividos_idade} dias!\n')
        print(f'Isso equivale a:\n'
              f'{idade} anos\n'
              f'ou {idade * 12} meses\n'
              f'ou {dias_vividos_idade / 7}  semanas\n'
              f'ou {dias_vividos_idade * 24} horas\n'
              f'ou {dias_vividos_idade * 24 * 60} minutos\n'
              f'ou {dias_vividos_idade * 24 * 60 *60} segundos\n'
              f'ou {dias_vividos_idade * 24 * 60 * 60 * 1000} milesimos!!! \n')

        print(f'Se você viver ate os 80 anos ainda lhe restam {80 - idade} anos\n'
              f'ou {(80 - idade) * 12} meses\n'
              f'ou {(dias_vividos_80 - dias_vividos_idade) / 7}  semanas\n'
              f'ou {dias_vividos_80} dias\n'
              f'ou {dias_vividos_80 * 24} horas\n'
              f'ou {dias_vividos_80 * 24 * 60} minutos\n'
              f'ou {dias_vividos_80 * 24 * 60 * 60} segundos\n'
              f'ou {dias_vividos_80 * 24 * 60 * 60 * 1000} milesimos!!!\n')

        op_shutdown = input('Deseja continuar? Pressione (s) para sim ou qualuqer outra tecla para sair!')

        if op_shutdown == 's':
            continue

        else :
            break
