#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 16:39:58 2019

@author: cengqiqi
"""

import networkx as nx
import matplotlib.pyplot as plt
import pylab

G = nx.DiGraph()
G = nx.read_edgelist('wiki.txt')

#print(nx.info(G))

#print(nx.number_of_nodes(G)) 
#print(nx.number_of_edges(G)) 

#print(nx.is_directed(G))

#Rich club
rc = nx.rich_club_coefficient(G, normalized=False)
plt.scatter(rc.keys(),rc.values(),marker='x', c='g',s = 0.5)
plt.title('Rich-Club coefficient vs node degree')
plt.xlabel('k')
plt.ylabel('Rich-club coefficient of k')
pylab.savefig('rc_coefficient.png')

#Compute degree assortativity of graph.
dac=nx.degree_assortativity_coefficient(G)
print(dac)

#Nearest neighbrt drgree
#knn = nx.k_nearest_neighbors(G)
#plt.scatter(knn.keys(),knn.values(),marker='x', c='r',s = 0.5)
#plt.title('Nearest neghbours average degree vs node degree')
#plt.xlabel('k')
#plt.ylabel('Knn(K)')
#pylab.savefig('knn.png')

#Assortative coefficient
#ac = nx.degree_mixing_dict(G)
#plt.scatter(ac.keys(),ac.values(),marker='x', c='r',s = 0.5)

#Centrality
#cen = nx.degree_centrality(G)
#top_cen = sorted(cen.values())[0,50]
#plt.plot(top_cen)

#plt.title('Centrality of top 50')
#plt.xlabel('Centrality rank')
#plt.ylabel('Centrality')




