from argparse import ArgumentError
import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from edge import Edge

def graph_viz(graph: Graph, config: str) -> None:
    """
    this function uses networkx to visualize Graph objects
    params:
        graph: a Graph object
        config: how this graph should be printed. Use 'max_flow' to see the flow through the graph and the capacity of the edge.
        use 'min_cut' to see whether each edge is cut and the capcity of the edge. any other config will just show edge capacity.
    """
    # initializing a networkx graph
    G = nx.DiGraph()

    #creating edge weights based upon the config
    if config == "max_flow":
        for edge in graph.edges.values():
            G.add_edge(edge.outgoing_vertex.id, edge.incoming_vertex.id, weight = str(edge.flow) + "/" + str(edge.capacity))
    elif config == "min_cut":
        for edge in graph.edges.values():
            G.add_edge(edge.outgoing_vertex.id, edge.incoming_vertex.id, weight = str(edge.cut) + "," + str(edge.capacity))
    else:
        for edge in graph.edges.values():
            G.add_edge(edge.outgoing_vertex.id, edge.incoming_vertex.id, weight = str(edge.capacity))
    pos = nx.planar_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    # displaying the graph in the Python visualizer
    plt.show()