from numpy import double
from edge import Edge
from vertex import Vertex

class Graph:
	def __init__(self):
		self.vertices = {}
		self.edges = set()
	
	def add_vertex(self, vertex_id: int):
		v = Vertex(vertex_id)
		self.vertices[vertex_id] = v

	def add_edge(self, outgoing: int, incoming: int, weight: float):
		v1 = self.vertices[outgoing]
		v2 = self.vertices[incoming]
		e = Edge(v1,v2,weight)
		v1.add_outgoing_edge(e)
		self.edges.add(e)
