# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 02:41:46 2019

@author: gaurav
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()  # nx.Graph()

G.add_edge('a', 'b', weight=0.6)
G.add_edge('a', 'c', weight=0.2)
G.add_edge('c', 'd', weight=0.1)
G.add_edge('c', 'e', weight=0.7)
G.add_edge('c', 'f', weight=0.9)
G.add_edge('a', 'd', weight=0.3)

G.edges()

pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, arrowsize=25)

# labels
nx.draw_networkx_labels(G, pos, font_size=20)
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.xticks([])
plt.yticks([])
plt.show()
