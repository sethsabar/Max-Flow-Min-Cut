from graph import Graph
from load_graph import load_graph
from graph_viz import graph_viz
from max_flow import max_flow_ff

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

def test_deep_copy():
    g = load_graph("testfiles/edge1.txt")
    g_alt = g.deep_copy()
    assert len(g_alt.vertices) == 6
    assert len(g_alt.edges) == 6
    assert g.vertices[0] != g_alt.vertices[0]
    assert g.edges.pop() not in g_alt.edges
    assert g_alt.vertices[1].incoming_edges.pop() in g_alt.vertices[0].outgoing_edges

def test_max_flow():
    g1 = load_graph("testfiles/edge1.txt")
    g1_alt_1 = max_flow_ff(g1, 0, 3)
    assert g1_alt_1.get_edge(0, 1).get_flow() == 1
    assert g1_alt_1.get_edge(1, 2).get_flow() == 1
    assert g1_alt_1.get_edge(2, 3).get_flow() == 1
    g1_alt_2 = max_flow_ff(g1, 1, 4)
    assert g1_alt_2.get_edge(1, 2).get_flow() == 2
    assert g1_alt_2.get_edge(2, 3).get_flow() == 2
    assert g1_alt_2.get_edge(3, 4).get_flow() == 2

    g2 = load_graph("testfiles/edge3.txt")
    g2_alt = max_flow_ff(g2, 0, 3)
    assert g2_alt.get_edge(0, 1).get_flow() == 14
    assert g2_alt.get_edge(0, 2).get_flow() == 13
    assert g2_alt.get_edge(1, 3).get_flow() == 12
    assert g2_alt.get_edge(2, 3).get_flow() == 15
    assert g2_alt.get_edge(1, 2).get_flow() == 2

    g3 = load_graph("testfiles/edge5.txt")
    g3_alt = max_flow_ff(g3,0,3)
    assert g3_alt.get_edge(0,1).get_flow() == 0
