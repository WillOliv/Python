busca = input("\nDigite o nome do aluno que deseja buscar : ")

for indice in range(0, len(nome)):
    if busca == nome[indice]:
        print('Nome : {}'.format(nome[indice]))
        print('Idade :{}'.format(idade[indice]))
        print('Nota : {}'.format(float(nota[indice])))
