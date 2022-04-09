from posixpath import split
from graph import Graph
def load_graph(file: str):
    g = Graph()
    file  = open(file, 'r')
    lines = file.readlines()
    lines = [line for line in lines if line != "\n"]
    file.close()
    for line in lines:
        split_line = line.split(",")
        if not split_line[0] in g.vertices.keys():
            g.add_vertex(int(split_line[0]))
        if not split_line[1] in g.vertices.keys():
            g.add_vertex(int(split_line[1]))
        g.add_edge(int(split_line[0]), int(split_line[1]), float(split_line[2]))
    return g