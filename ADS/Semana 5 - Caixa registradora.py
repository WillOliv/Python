'''Faça um algoritmo para uma caixa registradora. A máquina recebe os produtos comprados e a quantidade
de cada um deles e retorna o valor total da compra. A funcionária deverá entrar com o código do produto
e a quantidade. A tabela abaixo mostra os produtos existentes. Quando a funcionária terminar de entrar
os produtos ela deverá digitar código do produto = 0 (zero). Neste instante, a caixa registradora deverá
retornar o valor total da compra. Lembre-se de fazer a verificação de erros checando se a funcionária digitou
os códigos corretamente.
(Produtos em uma tabela na atividade)'''

c = ['501', '502', '503', '504', '505', '506']
n = ['Arroz Tio João 1kg ', 'Feijão Kicaldo 1kg', 'Aguardente Velho Barreiro 910 ml', 'Fio Dental Reach Essencial Menta 100m', 'Fralda Huggies G Turma da Mônica Tripla Proteção Mega - 48 Unidades', 'Bebida à Base de Soja Sabor Maçã Ades 1 Litro']
p = [7.95, 4.65, 2.98, 9.85, 29.90, 5.95]

resposta = 1
caixa = 0
codigo = (input('Digite o código produto : '))

while resposta == 1:
    for indice in range(0, len(c)):
        if codigo == c[indice]:
            quantidade = int(input('Quantidade : '))
            soma = (p[indice] * quantidade)
            caixa = (caixa + soma)
            print('Total : R${:.2f} \n'.format(caixa))

            resposta = int(input('Digite 1 para continuar e 0 para finalizar : '))            
            while resposta != 0 and resposta != 1:
                print('Error')
                resposta = int(input('Digite 1 para continuar e 0 para finalizar : '))
                     
            if resposta == 0:
                print('\nCompra efetuada \nTotal : R${:.2f}'.format(caixa))
                break

            codigo = (input('Digite o código produto : '))

    if codigo != c[indice]:
        print('Produto não encontrado, reinicie o programa.')
        break
