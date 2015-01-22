import networkx as nx
import timeit


"""From the input file , take the edge info line by line and
store it in a list called lines"""

start=timeit.default_timer()

G=nx.Graph()

lines = [line.rstrip() for line in open('sample.txt')]
dict={}



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


#Removing nodes which are not having more than 3 nodes connected to them.


#Finding how many nodes have degree greater than equal to 2
node_degrees=[]

for each_value in deg.values():
    if int(each_value) >=2:
        node_degrees.append(each_value)

nodes_with_deg_more_than2=len(node_degrees)

stop = timeit.default_timer()

print "Total program run time is",stop-start








