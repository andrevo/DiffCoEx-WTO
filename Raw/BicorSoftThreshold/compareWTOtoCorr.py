import networkx as nx
import scipy.stats
import operator
import numpy

def jaccardFromRank(a, b, n):
    count = 0
    for i in range(len(a)):
        if (a[i] <= n) & (b[i] <= n):
            count += 1
    return float(count)/float(n)
        



f = open("SampleWTOandRhoFull.txt")

network = nx.Graph()
for line in f:
    splitLine = line.rstrip().split('\t')
    network.add_edge(splitLine[0], splitLine[1])
    network[splitLine[0]][splitLine[1]]['wtoFull'] = abs(float(splitLine[3]))#*numpy.sign(float(splitLine[3]))
    network[splitLine[0]][splitLine[1]]['rhoFull'] = abs(float(splitLine[2]))



f = open("SampleWTOandRhoSmall.txt")


for line in f:
    splitLine = line.rstrip().split('\t')
    network[splitLine[0]][splitLine[1]]['wtoSmall'] = abs(float(splitLine[3]))#*numpy.sign(float(splitLine[3]))
    network[splitLine[0]][splitLine[1]]['rhoSmall'] = abs(float(splitLine[2]))


f = open("SampleWTOandRho20.txt")


for line in f:
    splitLine = line.rstrip().split('\t')
    network[splitLine[0]][splitLine[1]]['wto20'] = abs(float(splitLine[3]))#*numpy.sign(float(splitLine[3]))
    network[splitLine[0]][splitLine[1]]['rho20'] = abs(float(splitLine[2]))

f = open("SampleWTOandRho50.txt")


for line in f:
    splitLine = line.rstrip().split('\t')
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

network.remove_edges_from(network.selfloop_edges())
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



wtoFR = {}
wtoSR = {}
rhoFR = {}
rhoSR = {}
wto20R = {}
wto50R = {}
rho20R = {}
rho50R = {}


for i in range(len(wtoFS)):
    wtoFR[wtoFS[i][0]] = i

for i in range(len(wtoSS)):
    wtoSR[wtoSS[i][0]] = i

for i in range(len(rhoFS)):
    rhoFR[rhoFS[i][0]] = i

for i in range(len(rhoSS)):
    rhoSR[rhoSS[i][0]] = i

for i in range(len(wto20S)):
    wto20R[wto20S[i][0]] = i

for i in range(len(wto50S)):
    wto50R[wto50S[i][0]] = i

for i in range(len(rho20S)):
    rho20R[rho20S[i][0]] = i

for i in range(len(rho50S)):
    rho50R[rho50S[i][0]] = i


wfrList = []
wsrList = []
rfrList = []
rsrList = []
w20rList = []
w50rList = []
r20rList = []
r50rList = []


for edge in edgeList:
    wfrList.append(wtoFR[edge])
    wsrList.append(wtoSR[edge])
    rfrList.append(rhoFR[edge])
    rsrList.append(rhoSR[edge])
    w20rList.append(wto20R[edge])
    w50rList.append(wto50R[edge])
    r20rList.append(rho20R[edge])
    r50rList.append(rho50R[edge])


#print "RhoS vs RhoF", scipy.stats.spearmanr(rsrList, rfrList)
#print "WTOS vs WTOF", scipy.stats.spearmanr(wsrList, wfrList)
#print "WTOS vs RhoF", scipy.stats.spearmanr(wsrList, rfrList)

n = 10000

print str(scipy.stats.spearmanr(rsrList, rfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(r20rList, rfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(r50rList, rfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(wsrList, wfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(w20rList, wfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(w50rList, wfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(wsrList, rfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(w20rList, rfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(w50rList, rfrList).correlation)+'\t'+ str(scipy.stats.spearmanr(wfrList, rfrList).correlation), 



print str(jaccardFromRank(rsrList, rfrList, n))+'\t'+ str(jaccardFromRank(r20rList, rfrList, n))+'\t'+ str(jaccardFromRank(r50rList, rfrList, n))+'\t'+ str(jaccardFromRank(wsrList, wfrList, n))+'\t'+ str(jaccardFromRank(w20rList, wfrList, n))+'\t'+ str(jaccardFromRank(w50rList, wfrList, n))+'\t'+ str(jaccardFromRank(wsrList, rfrList, n))+'\t'+ str(jaccardFromRank(w20rList, rfrList, n))+'\t'+ str(jaccardFromRank(w50rList, rfrList, n))+'\t'+str(jaccardFromRank(wfrList, rfrList, n))


