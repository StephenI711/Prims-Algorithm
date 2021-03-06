# Stephen Irwin
# MATH 2305
# Final Project (Prims Algorithm)
# Solves minimum spanning tree problem

import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np

G = nx.read_weighted_edgelist('data/G1.txt')


def show_weighted_graph(G):
    
     """Prints a weighted graph from a text file.
    
    A weighted graph shows the cost or weight between between points on the
    graph.
    
    Parameters
    ----------
    G = A networkx graph.
    
    Returns
    -------
    A plotted graph with weights between its nodes.
    
    """
    
     pos = nx.planar_layout(G)
     nx.draw(G, pos)
     labels = nx.get_edge_attributes(G, 'weight')
     nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels)
     plt.show()


def draw_subtree(G, T):
    
     """Prints a subtree of graph 'G'.
    
    A subtree is tree graph inside of larger graph. 
    
    Parameters
    ----------
    G = A networkx graph.
    T = A networkx subgraph of 'G'
    Returns
    -------
    A subgraph of a plotted weighted graph.
    
    """
    
     pos = nx.planar_layout(G)
     nx.draw_networkx(G, pos)
     labels = nx.get_edge_attributes(G, 'weight')
     nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels,)
     nx.draw_networkx_edges(G, pos,
                            edgelist=T.edges(),
                            width=8, alpha=0.5,
                            edge_color='r',)
     nx.draw_networkx_nodes(G,
                           pos,
                           nodelist=T.nodes(),
                           node_color='r',
                           node_size=500,
                           alpha=0.8)
     plt.show()