from graph import Graph


def max_flow_ff(g: Graph, source: int, sink: int):
    so = g.get_vertex(source)
    si = g.get_vertex(sink)
    