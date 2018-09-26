import networkx as nx

#network = nx.Graph()

f = open("RhoAndVarExp50.txt.sample")
i = 0
weightMat = {}
nodeStrength = {}
for line in f:
    if ((i%1000000) == 0):
        print i
    i += 1
    splitLine = line.rstrip().split('\t')
    nodeStrength[splitLine[0]] = 1
    if (splitLine[1], splitLine[0]) not in weightMat:
        weightMat[(splitLine[0], splitLine[1])] = abs(float(splitLine[2]))
    
    #network.add_edge(splitLine[0], splitLine[1], weight=abs(float(splitLine[2])))

def getWeight(node1, node2):
    if (node1, node2) in weightMat:
        return weightMat[(node1, node2)]
    elif (node2, node1) in weightMat:
        return weightMat[(node2, node1)]

for node in nodeStrength:
    strength = 0
    for node2 in nodeStrength:
        if node2 != node:
            if (node, node2) in weightMat:
                strength += abs(weightMat[(node, node2)])
            else:
                strength += abs(weightMat[(node2, node)])                
    nodeStrength[node] = strength

f = open("SampleWTO50.txt", 'w')

for node1 in nodeStrength:
#    print node1
    for node2 in nodeStrength:
        weightProdSum = 0
        for neighbor in nodeStrength:
            if (neighbor != node1) & (neighbor != node2):
                weightProdSum += getWeight(node1, neighbor)*getWeight(neighbor, node2)
                 
        overlap = (weightProdSum+getWeight(node1, node2))/(min(nodeStrength[node1], nodeStrength[node2])+1-getWeight(node1, node2))
        print >> f, node1, node2, overlap
#        network[node1][node2]['overlap'] = (weightProdSum+network[node1][node2]['weight'])/(min(network.node[node1]['strength'], network.node[node2]['strength'])+1-network[node1][node2]['weight'])

f.close()

# for node1 in network:
#     for node2 in network:
#         print >> f, node1, node2, network[node1][node2]['overlap'], network[node1][node2]['weight']

#f.close()



