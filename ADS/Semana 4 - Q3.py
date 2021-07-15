'''Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com
menor salário terá um aumento proporcionalmente maior do que os funcionários com um salário maior, e
conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário.
Faça um programa que leia:
o valor do salário atual do funcionário;
o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Salário atual     - Reajuste     - Tempo de serviço  - Bônus

Até 500,00        - 25%          - Abaixo de 1 ano   - Sem bônus
Até 1000,00       - 20%          - De 1 a 3 anos     - 100,00
Até 1500,00       - 15%          - De 4 a 6 anos     - 200,00
Até 2000,00       - 10%          - De 7 a 10 anos    - 300,00
Acima de 2000,00  - Sem reajuste - Mais de 10 anos   - 500,00'''

valor = int(input('Qual o valor do seu salário atual?'))
tempo = int(input('Quantos anos você vai completar dentro da empresa no final desse ano?'))

salario1 = 500
salario2 = 1000
salario3 = 1500
salario4 = 2000

reajuste1 = 25/100
reajuste2 = 20/100
reajuste3 = 15/100
reajuste4 = 10/100
reajuste5 = 'Sem reajuste'

bonus1 = 'Sem bônus'
bonus2 = 100
bonus3 = 200
bonus4 = 300
bonus5 = 500

if (valor <= salario1) and (tempo == 1):
    print('Seu reajuste é de:', valor * reajuste1)
    print('Seu bônus é de :', bonus1)
    print('Salário total após reajuste :', valor + (valor * reajuste1))

elif valor > salario1 and valor <= salario2 and tempo > 1 and tempo <= 3:
    print('Seu reajuste é de:', valor * reajuste2)
    print('Seu bônus é de :', bonus2)
    print('Salário total após reajuste :', valor + (valor * reajuste2) + bonus2)

elif valor > salario2 and valor <= salario3 and tempo > 3 and tempo <= 6:
    print('Seu reajuste é de:', valor * reajuste3)
    print('Seu bônus é de :', bonus3)
    print('Salário total após reajuste :', valor + (valor * reajuste3) + bonus3)

elif valor > salario3 and valor <= salario4 and tempo > 6 and tempo <= 10:
    print('Seu reajuste é de:', valor * reajuste4)
    print('Seu bônus é de :', bonus4)
    print('Salário total após reajuste :', valor + (valor * reajuste4) + bonus4)

elif (valor > salario4) and (tempo > 10):
    print('Seu reajuste é de:', reajuste5)
    print('Seu bônus é de :', bonus5)
    print('Salário total após reajuste :', (valor + bonus5))

else:
    print('Você não tem direito à reajuste ou bônus')
