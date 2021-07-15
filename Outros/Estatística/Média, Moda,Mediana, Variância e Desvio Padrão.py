import math

classe = int(input("\nQuantas categorias existem? "))
par_ou_impar = int(input("A quantidade de classes é par ou impar (0 para par e 1 para impar)? "))

#Frequência absoluta / frequência absoluta total / quantas classes existem
fa = []
xi = []
n = classe

print("\n")
while classe > 0 :
    fa.append(float(input("Diga a frequência absouta das classes em ordem crescente : ")))
    classe = classe - 1

#Frequência absoluta total
faTotal = sum(fa)
media = (faTotal/n)

#Posição dos 2 números do meio caso a mediana seja par
posicao1 = int((n/2))
posicao2 = int((n / 2) +1)

mediana = (0)

if par_ou_impar == 0:
    mediana1 = (fa[posicao1 - 1])
    mediana2 = (fa[posicao2 - 1])
    mediana = ((mediana1 + mediana2) / 2)

elif par_ou_impar == 1:
    mediana1 = (fa[posicao1])
    mediana2 = (fa[posicao2])
    mediana = (mediana1)

else :
    print("\n")
    print(30*"-")
    print("\nErro, alguns dados podem não estar certos\n")
    print(30*"-")

#Primeiro e Segundo processo da variância
box1 = []
box2 = []

for indice in range(0, len(fa)):
    box1.append(float("{:.3f}".format(fa[indice] - media)))

for indice in range(0, len(fa)):
    box2.append(float("{:.3f}".format(box1[indice] ** 2)))

#Terceiro processo da variância / Variância final / Desvio padrão
box3 = sum(box2)
box4 = (box3 / (n-1))
S = math.sqrt(box4)

#Quartis 1, 2 e 3 sem float
Q1 = int(1*(n+1)/4)
Q2 = int(2*(n+1)/4)
Q3 = int(3*(n+1)/4)

#Quartis 1, 2 e 3 com float
q1 = (1*(n+1)/4)
q2 = (2*(n+1)/4)
q3 = (3*(n+1)/4)

print("\n")
print(30*"-")
print("A média é : {:.2f} ".format(media))
print("A moda é a classe que mais se repete")
print("A mediana é : {:.2f} \n".format(mediana))

print(30*"-")
print("Variância(S²) \n")
print(box1)
print(box2)
print(box3)
print(box4,"\n")
print(30*"-")
print("O desvio padrão(S) é : {} \n".format(S))
print(30*"-")

print("Quartis(Q)")
print("\nNúmeros estipulados")
print("Q1 = {}".format(fa[Q1]))
print("Q2 = {}".format(fa[Q2]))
print("Q3 = {}".format(fa[Q3]))
print("\nNúmeros exatos")
print("Q1 = {}".format(q1))
print("Q2 = {}".format(q2))
print("Q3 = {}".format(q3))
