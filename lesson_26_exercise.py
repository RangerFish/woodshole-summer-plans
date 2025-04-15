#---SE370 Lesson 26 Lecture/Exercise---#
#-By: Ian Kloo
#-March 2025

import os
os.getcwd()

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import ipysigma

#---things to do:
#1. Build networks from scratch --> edge lists and adjacency matrices
#2. Basic network analysis --> centrality, clustering, shortest paths
#3. Visualize networks with ipysigma
#4. Load networks from files

#---building networks in networkx
#-adjacency matrix

adj_matrix = pd.DataFrame([[0,1,1,1,0,0,0,0,0],
                            [1,0,1,1,0,0,1,1,1],
                            [1,1,0,1,1,1,0,0,0],
                            [1,1,1,0,0,0,0,0,0],
                            [0,0,1,0,0,1,0,0,0],
                            [0,0,1,0,1,0,0,0,0],
                            [0,1,0,0,0,0,0,0,0],
                            [0,1,0,0,0,0,0,0,0],
                            [0,1,0,0,0,0,0,0,0],], 
                            columns = ['cadet_1','cadet_2','cadet_3','cadet_4','cadet_5','cadet_6','cadet_7','cadet_8','cadet_9'],
                            index = ['cadet_1','cadet_2','cadet_3','cadet_4','cadet_5','cadet_6', 'cadet_7','cadet_8','cadet_9'])

adj_matrix
#convert to a networkx graph
G = nx.from_pandas_adjacency(adj_matrix)
G
nx.draw(G, with_labels = True)
#draw with the built-in tools



#-edge list
edge_list = [('cadet_1','cadet_2'), ('cadet_1','cadet_3'), 
             ('cadet_1','cadet_4'), ('cadet_2','cadet_4'), 
             ('cadet_3','cadet_4'), ('cadet_3','cadet_5'),
             ('cadet_3','cadet_2'), ('cadet_6','cadet_5'),
             ('cadet_6','cadet_3'), ('cadet_2','cadet_7'),
             ('cadet_2','cadet_8'), ('cadet_2','cadet_9'),]

#convert to a networkx graph - first we instatiate an empty graph object
G = nx.Graph()
#now we add the edges
G.add_edges_from(edge_list)
#and finally draw



#-directed graphs


#-weighted graphs

#adding edge weights
edge_list = [('cadet_1','cadet_2',1), ('cadet_1','cadet_3',2), 
             ('cadet_1','cadet_4',1), ('cadet_2','cadet_4',1), 
             ('cadet_3','cadet_4',4), ('cadet_3','cadet_5',3),
             ('cadet_3','cadet_2',3), ('cadet_6','cadet_5',2),
             ('cadet_6','cadet_3',1), ('cadet_2','cadet_7', 1),
             ('cadet_2','cadet_8', 1), ('cadet_2','cadet_9', 1),]
G = nx.DiGraph()
G.add_weighted_edges_from(edge_list)

#get edge weights
edge_weights = nx.get_edge_attributes(G, 'weight')
edge_weights = list(edge_weights.values())

#draw the graph with edges sized proportionally to weight
nx.draw(G, with_labels = True, arrows = True, arrowsize = 14, arrowstyle = '-|>', width = edge_weights, connectionstyle = 'arc3,rad=0.5')

#curved edges can be useful sometimes...but can also be distracting - use with caution!
# end at edge_weights if you don't want the curved edges

#-layouts

#spring layout --> usually pretty good, avoids overlaps

#circular layout --> often loses the structure

#random layout --> not very useful

#fruchterman-reingold layout --> best for avoiding edge overlap


#---basic network analysis

#-most important nodes
#degree centrality --> total number of connections (scaled)
nx.degree_centrality(G)
#betweenness centrality --> number of times a node is on the shortest path between two other nodes (scaled)

#pagerank --> a measure of importance, used by search engines to determine best pages to return in a search (scaled)

#-community detection
#find louvain communities

#label propagation


#---visualizing with ipysigma
#simplest version

#size nodes by degree

#color by partition

#set edge widths


#---special topic: bipartite graphs
edge_list = [('cadet_1','se370'), ('cadet_1','se387'), ('cadet_1','se489'), 
             ('cadet_2','se370'), ('cadet_2','se489'), 
             ('cadet_3','se387')]

#color cadets and courses differently


#---loading networks from files
#load edges and nodes from 911 data
edges = pd.read_csv('911_edges.csv')
nodes = pd.read_csv('911_node_list.csv')
#replace edges with names
edge_names = edges.merge(nodes, left_on = 'from', right_on = 'id', how = 'left')[['name', 'to']]
edge_names.columns = ['from', 'to']

edge_names = edges.merge(nodes, left_on = 'from', right_on = 'id', how = 'left')[['from', 'name']]
edge_names.columns = ['from', 'to']

edge_names

#build graph from edges
G = nx.Graph()
G.add_edges_from(edge_names.values)
#size by betweenness centrality
degree = nx.betweenness_centrality(G)

#color by community
partition = nx.community.louvain_communities(G, weight = 'weight')
partition

node_colors = []
for node in G.nodes():
    if node in partition[0]:
        node_colors.append(1)
    if node in partition[1]:
        node_colors.append(2)
    if node in partition[2]:
        node_colors.append(3)

node_colors
        

