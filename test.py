import pytest
from graph import Graph
from load_graph import load_graph
from graph_viz import graph_viz

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

def test_load_graph():
    g = load_graph("testfiles/edge1.txt")
    assert len(g.vertices) == 6
    assert len(g.edges) == 6

def test_graph_viz():
    graph_viz(load_graph("testfiles/edge2.txt"))