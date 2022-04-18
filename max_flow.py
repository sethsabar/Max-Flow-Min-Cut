from queue import PriorityQueue
from turtle import back
from graph import Graph
from graph_viz import graph_viz
from vertex import Vertex
from math import inf

def bfs(g_alt: Graph, so):
    # enquing the source vertex for BFS, and initializing came_from and visited dictionaries
    to_check = []
    to_check.append(so)

    came_from = {value:None for (_, value) in g_alt.vertices.items()}
    visited = {value:False for (_, value) in g_alt.vertices.items()}
    visited[so] = True

    while not len(to_check) == 0:
        cur_vertex: Vertex = to_check.pop(0)
        for e in cur_vertex.get_outgoing_edges():
            if visited[e.get_incoming_vertex()] == False:
                if e.get_capacity() - e.get_flow() != 0:
                    visited[e.get_incoming_vertex()] = True
                    to_check.append(e.get_incoming_vertex())
                    came_from[e.incoming_vertex] = (cur_vertex, "forward")
        for e in cur_vertex.get_incoming_edges():
            if visited[e.get_outgoing_vertex()] == False:
                if e.get_flow() > 0:
                    visited[e.get_outgoing_vertex()] = True
                    to_check.append(e.get_outgoing_vertex())
                    came_from[e.outgoing_vertex] = (cur_vertex, "backward")
    
    return came_from


def max_flow_ff(g: Graph, source, sink):
    # creating a deep copy of our graph, we will use this graph for computation, 
    # and returning so that we don't alter the original graph
    g_alt = g.deep_copy()
    so = g_alt.get_vertex(source)
    si = g_alt.get_vertex(sink)

    came_from = bfs(g_alt, so)
    while came_from[si] != None:
        backtrack_vertex = si
        init_edge_list = []
        min_capacity = inf
        while backtrack_vertex != so:
            if came_from[backtrack_vertex][1] == "forward":
                edge_to_add = g_alt.get_edge(came_from[backtrack_vertex][0].id, backtrack_vertex.id)
                init_edge_list.append((edge_to_add, "forward"))
                if edge_to_add.get_capacity() - edge_to_add.get_flow() < min_capacity:
                    min_capacity = edge_to_add.get_capacity() - edge_to_add.get_flow()
            else:
                edge_to_add = g_alt.get_edge(backtrack_vertex.id, came_from[backtrack_vertex][0].id)
                init_edge_list.append((edge_to_add, "backward"))
                if edge_to_add.get_flow() < min_capacity:
                    min_capacity = edge_to_add.get_flow()
            
            backtrack_vertex = came_from[backtrack_vertex][0]
        for edge in init_edge_list:
            if edge[1] == "forward":
                edge[0].set_flow(edge[0].get_flow() + min_capacity)
            else:
                edge[0].set_flow(edge[0].get_flow() - min_capacity)
    
        came_from = bfs(g_alt, so)

    return g_alt
            

