from edge import Edge
from vertex import Vertex

class Graph:
	def __init__(self):
		"""
		initializer for Graph
		"""

		# a dictionary from vertex id to vertex
		self.vertices: dict[int, Vertex] = {}

		# a dictionary from 
		self.edges: dict[tuple[int, int], Edge] = {}
	
	def add_vertex(self, vertex_id: int):
		"""
		method for adding a vertex to the graph
		params:
			vertex_id: the integer id of the vertex we'd like to add
		"""
		v = Vertex(vertex_id)
		self.vertices[vertex_id] = v

	def add_edge(self, outgoing: int, incoming: int, capacity: float):
		"""
		method for adding an edge the to graph. if this method is called it is assumed that the edge vertices have already
		been added to the graph.
		params:
			outgoing: the id of the outgoing edge
			incoming: the id of the incoming edge
			capacity: the flow capacity of the edge
		"""

		v1 = self.vertices[outgoing]
		v2 = self.vertices[incoming]
		e = Edge(v1,v2,capacity)
		v1.add_outgoing_edge(e)
		v2.add_incoming_edge(e)
		self.edges[(outgoing, incoming)] = e
	
	def get_vertex(self, vertex_id: int) -> Vertex:
		return self.vertices[vertex_id]
	
	def get_edge(self, outgoing: int, incoming: int) -> Edge:
		"""
		a method which gets an edge from the graph
		params:
			outgoing: the id of the outgoing id
			incoming: the id of the incoming id
		"""
		return self.edges[(outgoing, incoming)]
	
	def clear(self) -> None:
		"""
		a method for resetting every edge's flow and cut status to 0 and false respectively
		"""
		for edge in self.edges.values():
			edge.flow = 0
			edge.cut = False