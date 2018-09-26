import networkx as nx

network = nx.Graph()

f = open("RhoAndVarSmall.txt")
for line in f:
    splitLine = line.rstrip().split('\t')
    network.add_edge(splitLine[0], splitLine[1], weight=abs(float(splitLine[2])))


for node in network:
    strength = 0
    for node2 in network:
        if node2 != node:
            strength += abs(network[node][node2]['weight'])
    network.node[node]['strength'] = strength

for node1 in network:
    print node1
    for node2 in network:
        weightProdSum = 0
        for neighbor in network:
            if (neighbor != node1) & (neighbor != node2):
                weightProdSum += abs(network[node1][neighbor]['weight']*network[node2][neighbor]['weight'])


        network[node1][node2]['overlap'] = (weightProdSum+network[node1][node2]['weight'])/(min(network.node[node1]['strength'], network.node[node2]['strength'])+1-abs(network[node1][node2]['weight']))

f = open("WTOSmall.txt", 'w')

for node1 in network:
    for node2 in network:
        print >> f, node1, node2, network[node1][node2]['overlap'], network[node1][node2]['weight']

f.close()



