# Stephen Irwin
# MATH 2305
# Final Project (Prims Algorithm)
# Solves minimum spanning tree problem


from algorithms.prims import prims_algorithm
import networkx as nx


# Import graph from Data folder to use algorithm
# 3 test graphs (G1.txt, G2.txt, G3.txt)

G = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
# Initialize T 

T = prims_algorithm(G,3, draw = True, detail = True)

