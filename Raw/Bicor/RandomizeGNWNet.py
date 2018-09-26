import networkx as nx
import random

regNet = nx.DiGraph()


f = open("Ecoli.tsv")



def flip(a):
    if a == '+':
        return '-'
    elif a == '-':
        return '+'
    else:
        return a
    
    
edgelist = []

for line in f:
    splitLine = line.rstrip().split('\t')
    regNet.add_edge(splitLine[0], splitLine[1])
    regNet[splitLine[0]][splitLine[1]]['type'] = splitLine[2]

modNet = regNet.copy()


netLen = len(regNet)/10
sample = random.sample(modNet.edges(), netLen)
deletions = sample[0:(netLen/2)]
switches = sample[((netLen/2)+1):netLen]

f = open("switches.txt", 'w')
for edge in switches:
    print >> f, edge[0], edge[1]

f.close()

f = open("deletions.txt", 'w')
for edge in deletions:
    print >> f, edge[0], edge[1]

f.close()



for edge in deletions:
    modNet.remove_edge(edge[0], edge[1])

for edge in switches:
    modNet[edge[0]][edge[1]]['type'] = flip(modNet[edge[0]][edge[1]]['type'])



f = open("Randomized.tsv", 'w')

for edge in modNet.edges():
    print >> f, edge[0]+'\t'+edge[1]+'\t'+modNet[edge[0]][edge[1]]['type']

f.close()

           



