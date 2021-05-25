nome = input('Nome : ')
idade = int(input('idade : '))
doenca_infecciosa = input('Doença infecciosa?').upper()

if idade >= 65:
    print('Com prioridade')

    if doenca_infecciosa == 'SIM':
        print('Sala amarela')
    elif doenca_infecciosa == 'NAO':
        print('Sala branca')
    else:
        print('Responda com sim ou nao')

elif idade < 65:
    print('Sem prioridade')

    if doenca_infecciosa == 'SIM':
        print('Sala amarela')
    elif doenca_infecciosa == 'NAO':
        print('Sala branca')
    else:
        print('Responda com sim ou nao')

else:
    print('Sem prioridade nenhuma')
