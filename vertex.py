class Vertex:
    # initializing a vertex with a unique id and an array of outgoing edges
    def __init__(self, id):
        self.id = id
        self.outgoing_edges = set()
    
    # add an outgoing edge for a vertex
    def add_outgoing_edge(self, edge):
        self.outgoing_edges.add(edge)
    