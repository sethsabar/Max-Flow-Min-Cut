from hashlib import new


class Edge:
    # initialize an edge with an outgoing vertex and an incoming vertex
    def __init__(self, outgoing_vertex, incoming_vertex, capacity):
        self.outgoing_vertex = outgoing_vertex
        self.incoming_vertex = incoming_vertex
        self.capacity: float = capacity
        self.flow: float = 0

    def get_outgoing_vertex(self):
        return self.outgoing_vertex

    def get_incoming_vertex(self):
        return self.incoming_vertex

    def get_capacity(self):
        return self.capacity
    
    def get_flow(self):
        return self.flow

    def set_flow(self, new_flow: float):
        self.flow = new_flow
