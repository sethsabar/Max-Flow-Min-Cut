from tomli import load
from graph_viz import graph_viz
from load_graph import load_graph
from max_flow import max_flow_ff
from min_cut import min_cut
from graph import Graph

# the currently loaded graph
cur_graph: Graph = None

if __name__ == '__main__':

    print("> ", end='')
    args = input()

    # the user can type quit to exit the repl
    while (args != "quit"):
        args = args.split(" ")

        # if load_graph is called we attempt to load the graph to our repl
        if (args[0] == "load_graph"):
            try:
                cur_graph = load_graph(args[1])
                print("Graph loaded!")
            except :
                print("Error: Unable to load graph")
        
        # if max_flow_min_cut is called we first print the value of the max flow, then visualize the graph of max flow, 
        # then we print out the value of the min cut, then visualize the graph of min cut
        elif (args[0] == "max_flow_min_cut"):
            try:
                flow = max_flow_ff(cur_graph, int(args[1]), int(args[2]))
                print("Max flow: " + str(flow))
                graph_viz(cur_graph, "max_flow")
                cut = min_cut(cur_graph, int(args[1]))
                print("Min cut: " + str(cut))
                graph_viz(cur_graph, "min_cut")
                cur_graph.clear()
            except:
                print("Error: Please make sure vertex id names are valid and/or you have loaded a graph")
        
        # if an invalid command is called we inform the user of available commands
        else:
            print("Invalid command: Please try:\n" +
            "load_graph <file name>\n" +
            "max_flow_min_cut <source> <sink> \n" + 
            "quit")

        print("> ", end='')
        args = input()