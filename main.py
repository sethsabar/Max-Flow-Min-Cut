from graph_viz import graph_viz
from load_graph import load_graph
from max_flow import max_flow_ff


g = load_graph("testfiles/edge4.txt")
g_alt = max_flow_ff(g, 1, 6)
graph_viz(g_alt)