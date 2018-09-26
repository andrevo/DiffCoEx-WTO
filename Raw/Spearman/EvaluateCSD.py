import operator


cVals = {}
sVals = {}
dVals = {}


f = open("commonGenes.txt")
for line in f:
    cVals[line.rstrip()] = {}
    sVals[line.rstrip()] = {}
    dVals[line.rstrip()] = {}

f = open("AllValues.txt")

f.readline()
for line in f:
    splitLine = line.rstrip().split('\t')
    cVals[splitLine[0]][splitLine[1]] = float(splitLine[6])
    sVals[splitLine[0]][splitLine[1]] = float(splitLine[7])
    dVals[splitLine[0]][splitLine[1]] = float(splitLine[8])

switch = {}
deletion = {}
conserved = {}

for gene in cVals.keys():
    conserved[gene] = {}
    switch[gene] = {}
    deletion[gene] = {}
    for gene2 in cVals.keys():
        conserved[gene][gene2] = False
        switch[gene][gene2] = False
        deletion[gene][gene2] = False

f = open("conserved.txt")


for line in f:

    splitLine = line.rstrip().split('\t')
    if (splitLine[0] in cVals.keys()) & (splitLine[1] in cVals.keys()):
        conserved[splitLine[0]][splitLine[1]] = True
        conserved[splitLine[1]][splitLine[0]] = True

nCons = 0
for i in conserved.keys():
    for j in conserved[i].keys():
        if conserved[i][j]:
            nCons += 1


f = open("switches.txt")

for line in f:
    splitLine = line.rstrip().split(' ')

    if (splitLine[0] in cVals.keys()) & (splitLine[1] in cVals.keys()):
        switch[splitLine[0]][splitLine[1]] = True
        switch[splitLine[1]][splitLine[0]] = True


nSwitch = 0
for i in switch.keys():
    for j in switch[i].keys():
        if switch[i][j]:
            nSwitch += 1

f = open("deletions.txt")
for line in f:

    splitLine = line.rstrip().split(' ')
    if (splitLine[0] in cVals.keys()) & (splitLine[1] in cVals.keys()):
        deletion[splitLine[0]][splitLine[1]] = True
        deletion[splitLine[1]][splitLine[0]] = True

nDels = 0
for i in deletion.keys():
    for j in deletion[i]:
        if deletion[i][j]:
            nDels += 1

orderedC = []

f = open("CValuesSorted.txt")
for line in f:
    orderedC.append(line.rstrip().split("\t"))

f.close()
# for k1, subdict in cVals.items():
#     for k2, value in sorted(subdict.items(), key=lambda (k, v): v, reverse=True):
#         orderedC.append((k1, k2, value))

# orderedC.sort(key=lambda x: x[2], reverse=True)

orderedS = []

f = open("SValuesSorted.txt")
for line in f:
    orderedS.append(line.rstrip().split("\t"))

f.close()
# for k1, subdict in sVals.items():
#     for k2, value in sorted(subdict.items(), key=lambda (k, v): v, reverse=True):
#         orderedS.append((k1, k2, value))

# orderedS.sort(key=lambda x: x[2], reverse=True)

orderedD = []
f = open("DValuesSorted.txt")
for line in f:
    orderedD.append(line.rstrip().split("\t"))

f.close()

# for k1, subdict in dVals.items():
#     for k2, value in sorted(subdict.items(), key=lambda (k, v): v, reverse=True):
#         orderedD.append((k1, k2, value))
        
# orderedD.sort(key=lambda x: x[2], reverse=True)




cSpec = []
cSens = []
cFPR = []
TP = 0
FP = 0
i = 0

for element in orderedC:
    i += 1
    if conserved[element[0]][element[1]] == True:
        TP += 1
        #print "TPC", element, i
    else:
        FP += 1
    
    TN = len(orderedS)-nCons-FP
    cSens.append(float(TP)/float(nCons))
    cFPR.append(float(FP)/float(len(orderedC)-nCons))
    cSpec.append(float(TN)/float(len(orderedC)-nCons))


sSpec = []
sSens = []
sFPR = []
TP = 0
FP = 0
i = 0

for element in orderedS:
    i += 1
    if deletion[element[0]][element[1]] == True:
        TP += 1
        #print "TPS", i
    else:
        FP += 1
    TN = len(orderedS)-nSwitch-FP
    sSens.append(float(TP)/float(nDels))
    sFPR.append(float(FP)/float(len(orderedS)-nDels))
    sSpec.append(float(TN)/float(len(orderedS)-nDels))



            
dSpec = []
dSens = []
dFPR = []
TP = 0
FP = 0
i = 0

for element in orderedD:
    i += 1
    if switch[element[0]][element[1]] == True:
        TP += 1
        #print "TPD", i
    else:
        FP += 1
    TN = len(orderedS)-nDels-FP
    dSens.append(float(TP)/float(nSwitch))
    dFPR.append(float(FP)/float(len(orderedD)-nSwitch))
    dSpec.append(float(TN)/float(len(orderedD)-nSwitch))




f = open("cROCCSD.txt", 'w')

for i in range(len(cSens)):
        print >> f, cSens[i], cFPR[i], cSpec[i]

f.close()    

f = open("sROCCSD.txt", 'w')

for i in range(len(sSens)):
    print >> f, sSens[i], sFPR[i], sSpec[i]

f.close()

f = open("dROCCSD.txt", 'w')

for i in range(len(dSens)):
    print >> f, dSens[i], dFPR[i], dSpec[i]

f.close()
