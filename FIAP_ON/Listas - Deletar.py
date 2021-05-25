nome = ['a', 'b', 'c']
idade = [1, 2, 3]
nota = [10, 20, 30]

busca = input("Digite o nome do aluno que será excluido no sistema : ")

for indice1 in range(0, len(nome)):
    if busca == indice1:
        del nome[indice1]
        del idade[indice1]
        del nota[indice1]
        break

for indice2 in range(0, len(nome)):
    print('Nome : '.format(nome[indice2]))
    print('Idade : '.format(idade[indice2]))
    print('Nota : '.format(nota[indice2]))
