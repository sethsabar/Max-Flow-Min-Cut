import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from edge import Edge


def graph_viz(graph: Graph):
    G = nx.DiGraph()
    edge: Edge
    for edge in graph.edges:
        G.add_edge(edge.outgoing_vertex.id, edge.incoming_vertex.id, weight = edge.weight)
    pos = nx.planar_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()