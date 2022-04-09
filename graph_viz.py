import networkx as nx
import matplotlib.pyplot as plt
import edge


def graph_viz(graph):
    G = nx.DiGraph()
    for 


G.add_edge(1,2, weight=1)
G.add_edge(1,3, weight=2)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()