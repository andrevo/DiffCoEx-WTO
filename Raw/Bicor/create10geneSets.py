import random

files = "RhoAndVar20.txt", "RhoAndVar50.txt", "RhoAndVarFull.txt", "RhoAndVarSmall.txt"
#files = "RhoAndVarFull.txt", "RhoAndVarSmall.txt"

geneList = []
f = open("geneList.txt")
for line in f:
    splitLine = line.rstrip().split('\t')
    geneList.append(splitLine[0])

geneSample = random.sample(geneList, 20000)



inSample = {}

for i in range(20):
    for gene in geneSample[i*1000:(i+1)*1000]:
        inSample[gene] = i



        
for fname in files:
    f = open(fname)
    outF = []
    for i in range(20):
        outF.append(open('MultiSets/'+str(i)+'/'+fname+".sample", 'w'))
    k = 0
    for line in f:
        if k % 1000000 == 0:
            print k
        k += 1
        splitLine = line.rstrip().split('\t')
        if ((splitLine[0] in inSample) & (splitLine[1] in inSample)):
            if (inSample[splitLine[0]] == inSample[splitLine[1]]):
                print >> outF[inSample[splitLine[0]]], line.rstrip()
                          
                          
    f.close()

                          
    for i in range(20):
        outF[i].close()
