classe = []
classe2 = (1)
fa = []
fr = []
Fa = []
Fa2 = (0)
Fr = []
Fr2 = (0)

xi = int(input("\nQuantas categorias existem? "))

while xi > 0 :
    classe.append(input("Digite a {}° categoria : ".format(classe2)))
    classe2 = classe2 + 1
    xi = xi - 1
       
print("\n")

for indice in range(0, len(classe)):
    fa.append(float(input(("Diga a frequência absouta na ordem das categorias : "))))

nfa = sum(fa)

print("\n")

for indice in range(0, len(classe)):
    fr.append(fa[indice] / nfa * 100)
    (indice + 1)

nfr = sum(fr)

print("\n")

for indice in range(0, len(classe)):
    Fa.append(fa[indice] + Fa2)
    Fa2 = Fa2 + fa[indice]
    (indice + 1)

print("\n")

for indice in range(0, len(classe)):
    Fr.append(fr[indice] + Fr2)
    Fr2 = Fr2 + fr[indice]
    (indice + 1)

print ("\n  xi |  fa   | fr%  |  Fa  |  Fr%")
print(40*"-")

for indice in range(0, len(classe)):
       print("  {}  | {:.1f}  | {:.1f} | {:.1f} | {:.1f}".format(classe[indice],fa[indice],fr[indice],Fa[indice],Fr[indice]))
       indice + 1
       
print("  n |  {:.1f} | {:.0f}% | _____ | _____".format(nfa, nfr))

























