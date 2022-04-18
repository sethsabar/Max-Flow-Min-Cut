from numpy import double
from edge import Edge
from vertex import Vertex

class Graph:
	# initializes the Graph with an dictionary of vertex id to vertices and a set for edges 
	def __init__(self):
		self.vertices: dict[int, Vertex] = {}
		self.edges: set[Edge] = set()
	
	# adds a vertex to the Graph given the vertex id
	def add_vertex(self, vertex_id: int):
		v = Vertex(vertex_id)
		self.vertices[vertex_id] = v

	# adds an edge to the Graph given the ids of the outgoing and incoming vertices and an edge weight
	def add_edge(self, outgoing: int, incoming: int, weight: float):
		v1 = self.vertices[outgoing]
		v2 = self.vertices[incoming]
		e = Edge(v1,v2,weight)
		v1.add_outgoing_edge(e)
		v2.add_incoming_edge(e)
		self.edges.add(e)
	
	# gets a vertex object given a vertex id
	def get_vertex(self, vertex_id: int) -> Vertex:
		return self.vertices[vertex_id]
	
	def get_edge(self, outgoing: int, incoming: int) -> Edge:
		outgoing_vertex: Vertex = self.vertices[outgoing]
		incoming_vertex: Vertex = self.vertices[incoming]
		for edge in outgoing_vertex.get_outgoing_edges():
			if edge.get_incoming_vertex() == incoming_vertex:
				return edge

	def deep_copy(self):
		g = Graph()
		for e in self.edges:
			v1 = e.outgoing_vertex.id
			v2 = e.incoming_vertex.id
			cap = e.capacity
			if v1 not in g.vertices.keys():
				g.add_vertex(v1)
			if v2 not in g.vertices.keys():
				g.add_vertex(v2)
			g.add_edge(v1, v2, cap)
		return g
