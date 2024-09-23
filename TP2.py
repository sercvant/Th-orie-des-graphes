#Exercice 1

#1. C'est un graphe

#2.

def enfile(F,v):
    F.append(v)
    return F

def defile(F):
    del F[0]
    return F

def estFileVide(F):
    return F == []

def tete(F):
    return F[0]

tab = [1,2,3,4]

print(tete(tab))

#3.

def empile(P, v):
    P.append(v)
    return P

def depile(P):
    del P[-1]

def estPileVide(P):
    return P == []

def sommet(P):
    return P[-1]

#Exercice 2

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph([(0,1),(0,2),(1,3),(2,4),(2,1),(3,5),(5,1)])

#1 
def parcours_en_profondeur(G, s):
    pere = ["0" for x in range(len(G.nodes))]
    p = []
    p.append(s)
    marc = []
    while len(p) > 1:
        u = sommet(p)
        depile(p)
        if u not in marc:
            marc.append(u)
            print(u)
            for v in list(G.neighbors(u)):
                if v not in marc:
                    pere[v] = u
                    empile(p,v)
    print(pere)
    print(p)

parcours_en_profondeur(g, 2)
nx.draw(g, with_labels=True)
plt.show()


