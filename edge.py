class Edge:
    def __init__(self, outgoing_vertex, incoming_vertex, capacity):
        """
        initializer for Edge object
        params: 
            outgoing_vertex: the Vertex object which this edge is directed from
            incoming_vertex: the Vertex object which this edge is directed towards
            capacity: the flow capacity of the edge
        """
        self.outgoing_vertex = outgoing_vertex
        self.incoming_vertex = incoming_vertex
        self.capacity: float = capacity
        # the current flow through the edge (this will be useful when calculating max flow)
        self.flow: float = 0
        # a bool indicating the the edge is cut (this will be useful when calculating min cut)
        self.cut: bool = False

    def set_flow(self, new_flow: float):
        self.flow = new_flow

    def set_cut(self, new_cut: bool):
        self.cut = new_cut
