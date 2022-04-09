import pytest
from graph import Graph

def test_graph():
    g = Graph()
    assert len(g.vertices) == 0
    assert len(g.edges) == 0
    g.add_vertex(0)
    assert len(g.vertices) == 1
    g.add_vertex(1)
    assert len(g.vertices) == 2
    g.add_edge(0,1,2)
    assert len(g.edges) == 1
    for e in g.edges:
        assert e.outgoing_vertex == g.vertices[0]
        assert e.incoming_vertex == g.vertices[1]
