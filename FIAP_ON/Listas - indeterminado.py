resposta = 'SIM'

nome = []
idade = []
nota = []

while resposta == 'SIM':
    nome.append(input('Qual o nome do aluno? : '))
    idade.append(input('Qual a idade? : '))
    nota.append(float(input('Qual a nota? : ')))
    resposta = input('Adicionar outro aluno no sistema? : ').upper

for indice in range(0, len(nome)):
    print('\n')
    print(20 * '-')
    print('Nome :  {}'.format(nome[indice]))
    print('Idade : {}'.format(idade[indice]))
    print('Nota : {}'.format(nota[indice]))
    print(20 * '-')
