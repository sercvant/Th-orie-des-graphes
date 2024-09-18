import networkx as nx           #pour la manipulation des graphes
import matplotlib.pyplot as plt #pour l’affichage
"""G1 = nx.Graph()                 #crée un graphe non-orienté vide
G1.add_edge(0,1)                #ajoute une arête entre les sommets 0 et 1
G1.add_edges_from([(3,0),(3,4)]) #ajoute les arêtes d’une liste donnée
nx.add_path(G1,[1,2,3])         #ajoute les arêtes du chemin 1-2-3
G1.add_node(6)                  #ajoute un sommet
G1.add_node("toto")
G1.add_edge("toto",6)

G1.remove_node(2) #Supprimez un sommet s de votre choix
print(G1.nodes) #Réaffichez le graphe
print(G1.edges)

nx.draw(G1,with_labels=True)    #on prépare le dessin du graphe
plt.show() #on affiche le dessin"""

#1.3
"""
G1 = nx.Graph()                 #crée un graphe non-orienté vide
G1.add_edge(0,1)                #ajoute une arête entre les sommets 0 et 1
G1.add_edges_from([(3,0),(3,4)]) #ajoute les arêtes d’une liste donnée
nx.add_path(G1,[1,2,3])         #ajoute les arêtes du chemin 1-2-3
G1.add_node(6)                  #ajoute un sommet
G1.add_node("toto")
G1.add_edge("toto",6)

G1.remove_node(6) #Supprimez un sommet s de votre choix
print(G1.nodes) #Réaffichez le graphe
print(G1.edges)
nx.draw(G1, with_labels=True, pos=nx.circular_layout(G1), node_color='r',
edge_color='b')

plt.show() #on affiche le dessin
"""
"""
G1 = nx.Graph()                 #crée un graphe non-orienté vide
G1.add_edge(0,1)                #ajoute une arête entre les sommets 0 et 1
G1.add_edges_from([(3,0),(3,4)]) #ajoute les arêtes d’une liste donnée
nx.add_path(G1,[1,2,3])         #ajoute les arêtes du chemin 1-2-3
G1.add_node(6)                  #ajoute un sommet
G1.add_node("toto")
G1.add_edge("toto",6)

G1.remove_node(6) #Supprimez un sommet s de votre choix
print(G1.nodes) #Réaffichez le graphe
print(G1.edges)
dico_positions = {0:(0,0),1:(1,0),2:(0,1),3:(1,1),4:(0,-1),6:(-1,-1),"toto":(1,-1)}
nx.draw(G1, with_labels=True, pos=dico_positions)
plt.show() #on
"""


#2.1
"""
G1 = nx.Graph()                 #crée un graphe non-orienté vide
G1.add_edge(1,5)                #ajoute une arête entre les sommets 0 et 1
G1.add_edges_from([(5,4),(5,2)]) #ajoute les arêtes d’une liste donnée
nx.add_path(G1,[1,2,3])         #ajoute les arêtes du chemin 1-2-3
G1.add_node(6)                  #ajoute un sommet
G1.add_edge(4,6)
G1.add_edge(4,3)
G1.add_edge(5,3)


#G1.remove_node(6) #Supprimez un sommet s de votre choix
#print(G1.nodes) #Réaffichez le graphe
#print(G1.edges)

tab = []
for couple in G1.edges:
    if 5 in couple:
        if couple[0] == 5:
            tab.append(couple[1])
        else:
            tab.append(couple[0])

print(tab)
dico_positions = {0:(0,0),1:(1,0),2:(0.9,-0.5),3:(0.7,-0.55),4:(0.6,0.2),6:(0.4,0.6),5:(0.8,0.3)}
nx.draw(G1, with_labels=True, pos=dico_positions)
plt.show() #on
"""

#2.2
"""
G1 = nx.Graph()                 #crée un graphe non-orienté vide
G1.add_edge(1,5)                #ajoute une arête entre les sommets 0 et 1
G1.add_edges_from([(5,4),(5,2)]) #ajoute les arêtes d’une liste donnée
nx.add_path(G1,[1,2,3])         #ajoute les arêtes du chemin 1-2-3
G1.add_node(6)                  #ajoute un sommet
G1.add_edge(4,6)
G1.add_edge(4,3)
G1.add_edge(5,3)
"""
def nombre_sommets(graph):
    return len(graph.nodes)

def nombre_aretes(graph):
    return len(graph.edges)

def existe_arete(graph, s1, s2):
    return (s1, s2) in graph.edges or (s2,s1) in graph.edges

def voisins(G, s):
    tab = []
    for i in range(nombre_sommets(G)+1):
        if(existe_arete(G, s, i)):
            tab.append(i)
    return tab

def degre(G,s):
    return len(voisins(G, s))

"""
print(nombre_sommets(G1)) 
print(nombre_aretes(G1)) 
print(existe_arete(G1, 3,0))
print(voisins(G1, 4))
print(degre(G1, 4))
"""
#print(G1.edges)

"""for couple in G1.edges:
    if 5 in couple:
        print(couple)

dico_positions = {0:(0,0),1:(1,0),2:(0.9,-0.5),3:(0.7,-0.55),4:(0.6,0.2),6:(0.4,0.6),5:(0.8,0.3)}
nx.draw(G1, with_labels=True, pos=dico_positions)
plt.show() #on"""


GO = nx.DiGraph() #on crée un graphe orienté
GO.add_edge(0,1)
GO.add_edge(1,0)
GO.add_edge(1,2)
GO.add_edge(3,2)
GO.add_edge(3,1)


def existe_arc(G, s1, s2):
    return (s1, s2) in G.edges

def voisins_entrants(G, s):
    tab = []
    for i in range(len(G.nodes)+1):
        if(existe_arc(G, i, s)):
            tab.append(i)
    return tab

def degre_entrant(G, s):
    return len(voisins_entrants(G, s))

def est_source(G, s):
    return degre_entrant(G, s) == 0

print(existe_arc(GO,1,0))
print(voisins_entrants(GO, 1))
print(degre_entrant(GO, 1))
print(est_source(GO, 3))

nx.draw(GO,with_labels=True) #on prépare le dessin du graphe
plt.show() #on affiche le dessin

