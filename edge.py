class Edge:
    # initialize an edge with an outgoing vertex and an incoming vertex
    def __init__(self, outgoing_vertex, incoming_vertex, capacity):
        self.outgoing_vertex = outgoing_vertex
        self.incoming_vertex = incoming_vertex
        self.capacity: float = capacity