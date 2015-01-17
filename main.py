import networkx as nx
import timeit
import csv

"""From the input file , take the edge info line by line and
store it in a list called lines"""

start=timeit.default_timer()

G=nx.Graph()

lines = [line.rstrip() for line in open('dataset')]
dict={}

"""Store the edge information in form of a dictionary
The starting node is the key, the nodes connected to it by edges are
stored in a list"""

for i in range(0,len(lines)-1):
    u,v=lines[i].split('\t')
    G.add_edge(u,v)


"""Finding the node with highest degree
Inbuilt function degree returns a dictionary with
dgrees for each node in the list"""

deg=G.degree()

#Finding the biggest degree value
largest=max(deg.values())

#Reverse dictionary lookup to find the key(node)
for key in deg.keys():
    if deg[key]==largest:
        print "nodes with highest degree are",key


stop = timeit.default_timer()

print "Total program run time is",stop-start








