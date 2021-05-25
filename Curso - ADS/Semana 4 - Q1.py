''''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação
sendo o valor da casa a comprar dividido pelo número de meses a pagar.'''

casa = int(input('Digite o valor da casa : '))
salario = float(input('Digite seu salário : '))
tempo = int(input('Quantidade de anos a pagar : '))

ano = (tempo * 12)
mensalidade = (casa / ano)
salario_porcent = (salario * 30/100)

print(20*'-')

if mensalidade > salario_porcent:
    print('Você não pode pagar por esta casa, a mensalidade é maior que 30% do seu salário.')

elif mensalidade < salario_porcent:
    print('Você pode pagar por esta casa. \nMensalidade : R${}'.format(mensalidade))

else:
    print('Algo deu errado, reinicie o código e digite os dados corretamente.')
