from queue import PriorityQueue
from turtle import back
from graph import Graph
from graph_viz import graph_viz
from vertex import Vertex
from edge import Edge
from math import inf

def bfs(g: Graph, so) -> dict[Vertex, (Vertex, str)]:
    """
    a method which implements breadth first search starting from a source vertex
    params:
        g: a graph object
        so: a source vertex object
    returns:
        a dictionary from Vertex to (Vertex, str) tuple. this returned dictionary essentially notes where each Vertex came from
        in the path starting from the source Vertex. the str in the tuple informs us whether or not the path through the edge
        was forwards or backwards. In the implementation of the Ford-Fulkerson algorithm, we allow for backtracking through
        edges in the wrong direction if the flow is non-zero
    """

    # initializing a list of vertices, which will act as a queue of vertices to check
    to_check = []
    to_check.append(so)

    # initializing a dictionary from Vertex to the Vertex it came from as well as the direction in which the edge from 
    # the vertex is
    came_from: dict[Vertex, (Vertex, str)] = {value:None for (_, value) in g.vertices.items()}

    # initializing a set of already visited vertices. we do not want to travle to the same vertex twice
    visited = set()
    visited.add(so)

    while not len(to_check) == 0:

        # popping the Vertex which has been in the queue the longest
        cur_vertex: Vertex = to_check.pop(0)

        # if a vertex connected via a directed edge from the current vertex has not been visited and there is spare 
        # flow available we queue up the incoming vertex of that edge to be checked, and add the current vertex as the 
        # incoming vertex's came from
        for e in cur_vertex.outgoing_edges:
            if e.incoming_vertex not in visited:
                if (e.capacity - e.flow) != 0:
                    visited.add(e.incoming_vertex)
                    to_check.append(e.incoming_vertex)
                    came_from[e.incoming_vertex] = (cur_vertex, "forward")
        
        # if a vertex connected via a directed edge to the current vertex has not been visited and there is non-zero flow in
        # through edge we queue up the outgoing vertex of that edge to be checked, and add the current vertex as the 
        # outgoing vertex's came from
        for e in cur_vertex.incoming_edges:
            if e.outgoing_vertex not in visited:
                if e.flow > 0:
                    visited.add(e.outgoing_vertex)
                    to_check.append(e.outgoing_vertex)
                    came_from[e.outgoing_vertex] = (cur_vertex, "backward")

    return came_from


def max_flow_ff(g: Graph, source: int, sink: int) -> float:
    """
    a method which populates a graph with it's maximum flow through edges
    params:
        g: a graph
        source: the id of the source vertex
        sink: the id of the sink vertex
        returns: the value of the maximum flow through the graph
    """

    # getting the Vertex objects from the graph
    so = g.get_vertex(source)
    si = g.get_vertex(sink)

    flow_val = 0

    # applying BFS to the graph to see if we can increment the flow
    came_from: dict[Vertex, tuple[Vertex, str]] = bfs(g, so)

    # as long as we have found a non-zero path from the source to the sink via BFS we can improve our flow
    while came_from[si] != None:
        backtrack_vertex: Vertex = si

        # initialzing a list of edges for which we'll need to update the flow, we have the tuple with a string
        # to note whether or not to increase or decrease flow (based on if we followed the edge forwards or backwards)
        init_edge_list: list[tuple[Edge, str]] = []
        min_capacity = inf

        # as we follow came_from from the sink back the source we update add the edges to the list of edges to update
        # and keep track of the minimum change we can make
        while backtrack_vertex != so:
            if came_from[backtrack_vertex][1] == "forward":
                edge_to_add = g.get_edge(came_from[backtrack_vertex][0].id, backtrack_vertex.id)
                init_edge_list.append((edge_to_add, "forward"))
                if edge_to_add.capacity - edge_to_add.flow < min_capacity:
                    min_capacity = edge_to_add.capacity - edge_to_add.flow
            else:
                edge_to_add = g.get_edge(backtrack_vertex.id, came_from[backtrack_vertex][0].id)
                init_edge_list.append((edge_to_add, "backward"))
                if edge_to_add.flow < min_capacity:
                    min_capacity = edge_to_add.flow
            
            backtrack_vertex = came_from[backtrack_vertex][0]

        # updating the total flow based upon the incremental improvement we just made
        flow_val += min_capacity

        # for each edge to update we increase or decrease the flow by min_capacity based on if we followed 
        # it forwards or backwards
        for edge in init_edge_list:
            if edge[1] == "forward":
                edge[0].set_flow(edge[0].flow + min_capacity)
            else:
                edge[0].set_flow(edge[0].flow - min_capacity)
    
        # repeating the BFS search
        came_from = bfs(g, so)

    return flow_val
            

