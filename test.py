import pytest
from edge import Edge
from graph_viz import graph_viz
from min_cut import min_cut
from vertex import Vertex
from graph import Graph
from load_graph import load_graph
from max_flow import max_flow_ff

def test_vertex_and_edge_init():
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_edge(0,1,2.5)
    g.add_edge(0,2,3)
    g.add_edge(2,3,4)

    assert [0,1,2,3] == [v for v in g.vertices.keys()]
    assert [(0,1), (0,2), (2,3)] == [e for e in g.edges.keys()]
    assert [2.5,3,4] == [e.capacity for e in g.edges.values()]

def test_load_graph():
    g = load_graph("testfiles/test1.txt")
    assert [0,1] == [v for v in g.vertices.keys()]
    assert [(0,1)] == [e for e in g.edges.keys()]
    assert [1] == [e.capacity for e in g.edges.values()]

    g = load_graph("testfiles/test2.txt")
    assert [0,1,2,3] == [v for v in g.vertices.keys()]
    assert [(0,1), (1,2), (2,3), (3,0)] == [e for e in g.edges.keys()]
    assert [3.2, 4, 0.4, 1] == [e.capacity for e in g.edges.values()]

def test_max_flow():
    g = load_graph("testfiles/test1.txt")
    assert 1 == max_flow_ff(g,0,1)
    g.clear()
    assert 0 == max_flow_ff(g,1,0)

    g = load_graph("testfiles/test2.txt")
    assert 3.2 == max_flow_ff(g,0,2)
    g.clear()
    assert 0.4 == max_flow_ff(g,0,3)
    g.clear()
    assert 1 == max_flow_ff(g,3,0)

    g = load_graph("testfiles/test3.txt")
    assert 8 == max_flow_ff(g,0,5)

def test_min_cut():
    g = load_graph("testfiles/test1.txt")
    max_flow_ff(g,0,1)
    assert 1 == min_cut(g,0)
    g.clear()
    assert 0 == min_cut(g,1)

    g = load_graph("testfiles/test2.txt")
    max_flow_ff(g,0,2)
    assert 3.2 == min_cut(g,0)
    g.clear()
    max_flow_ff(g,0,3)
    assert 0.4 == min_cut(g,0)
    g.clear()
    max_flow_ff(g,3,0)
    assert 1 == min_cut(g,3)

    g = load_graph("testfiles/test3.txt")
    max_flow_ff(g,0,5)
    assert 8 == min_cut(g,0)