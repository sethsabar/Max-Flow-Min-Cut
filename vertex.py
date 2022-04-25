import edge

class Vertex:
    # initializing a vertex with a unique id and an array of outgoing edges
    def __init__(self, id):
        self.id: int = id
        self.outgoing_edges: set[edge.Edge] = set()
        self.incoming_edges: set[edge.Edge] = set()
    
    # add an outgoing edge for a vertex
    def add_outgoing_edge(self, edge: edge.Edge):
        self.outgoing_edges.add(edge)

    # add an incoming edge for a vertex
    def add_incoming_edge(self, edge: edge.Edge):
        self.incoming_edges.add(edge)