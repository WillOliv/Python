'''Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro
número superior ao número lido. Exemplo: se o usuário informou o número 30, a sequência a ser
impressa será 1 1 2 3 5 8 13 21 34 (1 ponto).'''

numero = int(input('Digite um número : '))

a = 0
b = 1
c = (a + b)

while c <= numero:
    print(b)
    print(c)
    a = c
    b = (b + c)
    c = (a + b)
