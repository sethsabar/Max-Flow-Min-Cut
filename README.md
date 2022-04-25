# Max-Flow-Min-Cut
For MATH1230: Graph Theory

This program implements the max flow and min cut algorithms on graphs using the Ford-Fulkerson algorithm. Within this project,
there are Graph, Edge, and Vertex classes to represent directed graphs with flow capacity, flow, and cuts. There is a graph_viz
class which allows us to visualize what the graphs look like, with different configurations for visualizing a graph normally,
visualizing the max flow through a graph, or visualizing the min cut of a graph. There is a load_graph class which allows us to
cleanly load a graph with a txt file. For such a file, each line represents an edge, where the first element is the id of the
outgoing edge, the second element is the id of the incoming edge, and the third element is the capacity of the edge, seperated by
commas. Refer to the testfiles directory for some examples. There is also a test class which I have done some testing of my
program to make sure it is performing correctly. This file can be run by calling pytest test.py.

In order to actually use this program, a user should first create a graph file. Then they should run main.py, which will 
initialize a repl. They must first call load_graph 'file' which will load the 'file' into a Graph object in the repl. Then,
the user may call max_flow_min_cut 'source' 'sink'. This will first print the value of the max flow through the loaded graph, 
then it will visualize the max flow through the graph. Once the user closes the visualizer window, the value of the min flow 
will be printed (this will always equal max cut). Then it will visualize the min cut of the graph. Once the user closes the 
visualizer window, the repl will be ready to take in another command. The user may continue to load new graphs and/or get the
max flow and min cut for different sources and sinks as much as they'd like.

At the moment, the only bug I'm aware of is that graph visualization does not support multiple edges between the same vertex. 
Internally, the max flow and min cut calculations will be correct, however, they will not be visualized correctly. 

For my runtime analysis, please see runtime_analysis.txt