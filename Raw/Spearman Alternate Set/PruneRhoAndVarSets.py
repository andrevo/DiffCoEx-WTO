import random

files = "../RhoAndVar20.txt", "../RhoAndVar50.txt", "../RhoAndVarFull.txt", "../RhoAndVarSmall.txt"
#files = "RhoAndVarFull.txt", "RhoAndVarSmall.txt"

geneList = []
f = open("geneList.txt")
for line in f:
    splitLine = line.rstrip().split('\t')
    geneList.append(splitLine[0])

geneSample = random.sample(geneList, 1000)

inSample = {}
for gene in geneSample:
    inSample[gene] = True


for fname in files:
    f = open(fname)
    outF = open(fname+".sample", 'w')
    for line in f:
        splitLine = line.rstrip().split('\t')
        if (splitLine[0] in inSample) & (splitLine[1] in inSample):
            print >> outF, line
    f.close()
    outF.close()
