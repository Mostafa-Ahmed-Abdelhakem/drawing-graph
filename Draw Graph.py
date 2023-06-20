#### Implementing a graph as a shape ####

# import needed libraries
import networkx as nx
import matplotlib.pyplot as plt

# creating the graph
G = nx.DiGraph()

# crating the connections
G.add_edges_from(    
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])


# put in some nodes a specific values
val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

# put default in the rest of our nodes(using comprehension method)
values = [val_map.get(node, 0.25) for node in G.nodes()]

# specify the edges you want by a specific color(red)
red_edges = [('A', 'C'), ('E', 'C')]

# make other edges with color(black)
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# useless line
# edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

# Need to create layout when doing separate calls to draw nods and edges
# to determine the layout of the shape
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, cmap = plt.get_cmap('jet'), node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist = red_edges, edge_color = 'r', arrows = True)
nx.draw_networkx_edges(G, pos, edgelist = black_edges, edge_color = 'k', arrows = False)

plt.show()