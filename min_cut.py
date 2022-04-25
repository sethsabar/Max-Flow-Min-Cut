from graph import Graph
from vertex import Vertex

def dfs(g: Graph, source: int) -> set[Vertex]:
    """
    a function which implements depth first search, we are considered able to travel via an edge if the flow is less than
    the capacity (there is spare flow in the edge to travel through)
    params:
        g: a graph
        source: the id of the source vertex
    returns:
        a set of accessible edges from the source
    """
    to_check = [g.get_vertex(source)]
    visited = set()

    # while we still have vertices to check we pop the most recently add vertex to the queue and check the vertices
    # directly available via an outgoin edge. we only enqueue the vertex if it hasn't already been visited and the edge
    # has non-zero flow available
    while len(to_check) != 0:
        cur_vertex = to_check.pop()
        visited.add(cur_vertex)
        for e in cur_vertex.outgoing_edges:
            if e.incoming_vertex not in visited and e.capacity - e.flow != 0:
                to_check.append(e.incoming_vertex)
    
    return visited

def min_cut(g: Graph, source: int) -> float:
    """
    a method which gets the min cut for a graph. this method may only be called after max_flow_ff has been called on the graph
    as this information is required to implement this algorithm
    params:
        g: a graph
        source: the id of the source vertex 
    returns:
        the value of the minimum cut
    """

    # getting the edges 
    visited: set[Vertex] = dfs(g, source)

    # we cut exactly the edges which connect a vertex which can be reached from the source to a vertex which cannot be reached
    # from the source vertex
    cut_val = 0
    for v in visited:
        for e in v.outgoing_edges:
            if e.incoming_vertex not in visited:
                e.set_cut(True)
                cut_val += e.capacity
    
    return cut_val
