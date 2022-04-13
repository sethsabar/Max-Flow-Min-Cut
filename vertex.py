class Vertex:
    # initializing a vertex with a unique id and an array of outgoing edges
    def __init__(self, id):
        self.id: int = id
        self.outgoing_edges = set()
    
    # add an outgoing edge for a vertex
    def add_outgoing_edge(self, edge):
        self.outgoing_edges.add(edge)
    
    # gets the outgoing edges for a vertex
    def get_outgoing_edges(self):
        return self.outgoing_edges