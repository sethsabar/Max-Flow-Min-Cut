from graph import Graph

# given a csv file of graph edges where each line contains the outgoing vertex id, the incoming vertex id, the edge weight
def load_graph(file: str):
    g = Graph()
    file = open(file, 'r')
    # get an array of non-emtpy lines in the csv
    lines = file.readlines()
    lines = [line for line in lines if line != "\n"]
    file.close()
    for line in lines:
        split_line = line.split(",")
        # if either of the vertices isn't already in the graph add them
        if not split_line[0] in g.vertices.keys():
            g.add_vertex(int(split_line[0]))
        if not split_line[1] in g.vertices.keys():
            g.add_vertex(int(split_line[1]))
        # add the edge to the graph
        g.add_edge(int(split_line[0]), int(split_line[1]), float(split_line[2]))
    return g