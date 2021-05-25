resposta = 'S'
info = []

while resposta == 'S':
    aluno = [input('Nome : '),
            input('Idade : '),
            float(input('Nota : '))]
    info.append(aluno)
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in info:
    print(20 * '-')
    print('Nome : {}'.format(indice[0]))
    print('Idade : {}'.format(indice[1]))
    print('Nota : {}'.format(indice[2]))
