from graph import Graph
def load_vertex_file(g, vertex_file):
    file = open(vertex_file, 'r')
    lines = file.readlines
    file.close
    for line in lines:
        g.add_vertex(line)

def load_edge_file(g, edge_file):
    file  = open(edge_file, 'r')
    lines = file.readlines
    file.close
    for line in lines:
        split_line = line.split(",")
        g.add_edge(split_line[0], split_line[1], split_line[2])

def load_graph(vertex_file, edge_file):
    g = Graph()
    load_vertex_file(g, vertex_file)
    load_edge_file(g, edge_file)