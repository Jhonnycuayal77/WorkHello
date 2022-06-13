import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt

dt= pd.read_csv("C:/Users\Jhonny\Downloads\Libro1Datos.csv", header=0)

DATOS= nx.from_pandas_edgelist(dt, source="Criatura1", target="Criatura2", edge_attr="Distancia")

nx.draw_circular(DATOS, node_size=10, width=0.5,with_labels=True)
plt.axis("equal")
plt.show()


# #Graficar ruta
# amigo1=input("Ingresar tu nombre: ")
# amigo2=input("Ingresa el nombre de tu amigo: ")

# ruta=nx.dijkstra_path(DATOS, source=str(amigo1), target=str(amigo2), weight=True)
# ruta1=DATOS.subgraph(ruta)
# nx.draw_circular(ruta1, with_labels=True)
# plt.axis("equal")
# plt.show()


for x in DATOS.nodes():
    if DATOS.degree(x) >2:
        print(x)










# import networkx as nx
# from matplotlib import pyplot as plt

# G=nx.complete_graph(20) #Función Generadora de un grafo completo
# nx.draw_circular(G, node_size=10, width=0.5,with_labels=False)
# plt.axis("equal")
# plt.show()

# G=nx.complete_graph(20) #Función Generadora de un grafo completo
# nx.draw_circular(G, node_size=10, width=0.5,with_labels=False)
# plt.axis("equal")
# plt.show()
