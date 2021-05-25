login = 'SIM'
while login == 'SIM':
    tipo = input('Você é ADM, USR, GUEST ou outro?').upper()
    if tipo == 'ADM' or tipo == 'USR':
        gen = input('Qual seu gênero?').upper()

        if tipo == 'USR' and gen == 'FEMININO':
            print('Olá usuária')
        elif tipo == 'USR' and gen == 'MASCULINO':
            print('Olá usuário')
        elif tipo == 'ADM' and gen == 'FEMININO':
            print('Olá administradora')
        elif tipo == 'ADM' and gen == 'MASCULINO':
            print('Olá administrador')
        else:
            print('Gênero não encontrado')

    elif tipo == 'GUEST':
        print('Olá visitante')

    else:
        print('Olá desconhecido(a)')
    login = input('Você quer logar? ').upper()
