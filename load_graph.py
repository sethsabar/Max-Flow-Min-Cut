from io import BufferedReader
from graph import Graph

def load_graph(file: str):
    """
    a method for loading a graph from a txt file. These files must be formatted such that each line represents an edge,
    where there is the outgoing vertex id, the incoming vertex id, and the flow capacity of the edge seperated by commas
    params:
        file: the pathname of the graph file
    """

    # converting the file into a list of lines
    file: BufferedReader = open(file, 'r')
    lines = file.readlines()
    lines = [line for line in lines if line != "\n"]
    file.close()

    g = Graph()
    for line in lines:
        split_line = line.split(",")
        # if either of the vertices isn't already in the graph we must add them to the graph
        if not int(split_line[0]) in g.vertices.keys():
            g.add_vertex(int(split_line[0]))
        if not int(split_line[1]) in g.vertices.keys():
            g.add_vertex(int(split_line[1]))
        # adding the edge to the graph
        g.add_edge(int(split_line[0]), int(split_line[1]), float(split_line[2]))
        
    return g