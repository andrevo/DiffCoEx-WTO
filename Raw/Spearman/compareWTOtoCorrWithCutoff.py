import networkx as nx
import scipy.stats
import operator
import numpy
import community


def jaccardFromRank(a, b, n):
    count = 0
    for i in range(len(a)):
        if (a[i] <= n) & (b[i] <= n):
            count += 1
    return float(count)/float(n)
        



f = open("SampleWTOandRhoFull.txt")

network = nx.Graph()
for line in f:
    splitLine = line.rstrip().split(' ')
    network.add_edge(splitLine[0], splitLine[1])
    network[splitLine[0]][splitLine[1]]['wtoFull'] = abs(float(splitLine[3]))#*numpy.sign(float(splitLine[3]))
    network[splitLine[0]][splitLine[1]]['rhoFull'] = abs(float(splitLine[2]))



f = open("SampleWTOandRhoSmall.txt")


for line in f:
    splitLine = line.rstrip().split(' ')
    network[splitLine[0]][splitLine[1]]['wtoSmall'] = abs(float(splitLine[3]))#*numpy.sign(float(splitLine[3]))
    network[splitLine[0]][splitLine[1]]['rhoSmall'] = abs(float(splitLine[2]))


f = open("SampleWTOandRho20.txt")


for line in f:
    splitLine = line.rstrip().split(' ')
    network[splitLine[0]][splitLine[1]]['wto20'] = abs(float(splitLine[3]))#*numpy.sign(float(splitLine[3]))
    network[splitLine[0]][splitLine[1]]['rho20'] = abs(float(splitLine[2]))

f = open("SampleWTOandRho50.txt")


for line in f:
    splitLine = line.rstrip().split(' ')
    network[splitLine[0]][splitLine[1]]['wto50'] = abs(float(splitLine[3]))#*numpy.sign(float(splitLine[3]))
    network[splitLine[0]][splitLine[1]]['rho50'] = abs(float(splitLine[2]))

wtoFull = {}
wtoSmall = {}
rhoFull = {}
rhoSmall = {}
wto20 = {}
wto50 = {}
rho20 = {}
rho50 = {}



for edge in network.edges():
    if edge[0] == edge[1]:
        network.remove_edge(edge[0], edge[1])

edgeList = network.edges()


for edge in edgeList:

    wtoFull[edge] = network[edge[0]][edge[1]]['wtoFull']
    wtoSmall[edge] = network[edge[0]][edge[1]]['wtoSmall']
    rhoFull[edge] = network[edge[0]][edge[1]]['rhoFull']
    rhoSmall[edge] = network[edge[0]][edge[1]]['rhoSmall']
    rho20[edge] = network[edge[0]][edge[1]]['rho20']
    rho50[edge] = network[edge[0]][edge[1]]['rho50']

    wto50[edge] = network[edge[0]][edge[1]]['wto50']
    wto20[edge] = network[edge[0]][edge[1]]['wto20']




wtoFS = sorted(wtoFull.items(), key=operator.itemgetter(1))
wtoSS = sorted(wtoSmall.items(), key=operator.itemgetter(1))
rhoFS = sorted(rhoFull.items(), key=operator.itemgetter(1))
rhoSS = sorted(rhoSmall.items(), key=operator.itemgetter(1))
wto50S = sorted(wto50.items(), key=operator.itemgetter(1))
wto20S = sorted(wto20.items(), key=operator.itemgetter(1))
rho50S = sorted(rho50.items(), key=operator.itemgetter(1))
rho20S = sorted(rho20.items(), key=operator.itemgetter(1))

cutoffIndex = 489500
cutoff = {}
nLabels = ['wtoSmall', 'wto20', 'wto50', 'rhoSmall', 'rho20', 'rho50', 'wtoFull', 'rhoFull']
cutoff['wtoFull'] = wtoFS[cutoffIndex][1]
cutoff['wtoSmall'] = wtoSS[cutoffIndex][1]
cutoff['wto20'] = wto20S[cutoffIndex][1]
cutoff['wto50'] = wto50S[cutoffIndex][1]
cutoff['rhoFull'] = rhoFS[cutoffIndex][1]
cutoff['rhoSmall'] = rhoSS[cutoffIndex][1]
cutoff['rho20'] = rho20S[cutoffIndex][1]
cutoff['rho50'] = rho50S[cutoffIndex][1]


nets = {}

edgeList = network.edges()

for label in nLabels:
    nets[label] = nx.Graph()
    for edge in edgeList:
        if network[edge[0]][edge[1]][label] >= cutoff[label]:
            nets[label].add_edge(edge[0], edge[1])
    comps = list(nx.connected_component_subgraphs(nets[label]))
    maxSize = 0

    for i in range(len(comps)):
        if len(comps[i]) > maxSize:
            maxIndex = i
            maxSize = len(comps[i])
    nets[label] = comps[maxIndex]

overlapNodes = {}

for label in nLabels:
    for label2 in nLabels:
        overlapNodes[(label, label2)] = {}
        deg1 = []
        deg2 = []

        
        for node in nets[label]:
            if node in nets[label2]:
                overlapNodes[(label, label2)][node] = True
                deg1.append(nx.degree(nets[label], node))
                deg2.append(nx.degree(nets[label2], node))
        
        #print label, label2, len(overlapNodes[(label, label2)]), scipy.stats.spearmanr(deg1, deg2)
        

for label2 in ['wtoFull', 'rhoFull']:
    for label in nLabels:
        overlapDeg = []
        nonOverlapDeg = []
        for node in nets[label]:
            if node in nets[label2]:
                overlapDeg.append(nx.degree(nets[label], node))
            else:
                nonOverlapDeg.append(nx.degree(nets[label], node))
#        print label, label2, scipy.stats.mannwhitneyu(overlapDeg, nonOverlapDeg)

top100Nodes = {}


sDegs = {}
top100 = {}

for label in ['wtoFull', 'rhoFull']:
    degrees = []
    for node in nets[label]:
        degrees.append((node, nets[label].degree(node)))
    sDegs[label] = sorted(degrees, key=lambda x: x[1], reverse=True)
    count = 0
    top100[label] = {}
    for node in sDegs[label][0:100]:
        top100[label][node[0]] = True


top100overlapWTO = {}
top100overlapRho = {}
modularity = {}
noModules = {}

for label in nLabels:
    degrees = []
    for node in nets[label]:
        degrees.append((node, nets[label].degree(node)))
    sDegs[label] = sorted(degrees, key=lambda x: x[1], reverse=True)
    top100overlapWTO[label] = 0
    top100overlapRho[label] = 0
    
    for node in sDegs[label][0:100]:
        if node[0] in top100['rhoFull']:

            top100overlapRho[label] += 1
    for node in sDegs[label][0:100]:
        if node[0] in top100['wtoFull']:

            top100overlapWTO[label] += 1
    modularity[label] = community.modularity(community.best_partition(nets[label]), nets[label])
    noModules[label] = max(community.best_partition(nets[label]).values())
    #print label, count, community.modularity(community.best_partition(nets[label]), nets[label]), max(community.best_partition(nets[label]).values())

    #nx.write_edgelist(nets[label], label+'net.txt')
    
nLabels = ['rhoSmall', 'wtoSmall', 'rho20', 'wto20', 'rho50', 'wto50', 'rhoFull', 'wtoFull']
    
    
for label in nLabels:
    print len(nets[label]),

for label in nLabels:
    print float(top100overlapRho[label])/100,

for label in nLabels:
    print float(top100overlapWTO[label])/100,
    
for label in nLabels:
    print modularity[label],

for label in nLabels:
    print noModules[label],

for label in nLabels:
    print nx.average_clustering(nets[label]),

for label in nLabels:
    print numpy.mean(nx.degree_assortativity_coefficient(nets[label])),
print ''
    
n = 10000




