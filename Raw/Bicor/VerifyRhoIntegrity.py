import numpy
genes = {}
corrMat = {}

f = open("RhoAndVarFull.txt")
i = 0
errCount = 0
tests = 0
nanCount = 0
nanGenes = {}
for line in f:
    if i%100000 == 0:
        print i
    splitLine = line.rstrip().split('\t')
    if (splitLine[2] == '-nan'):
        nanCount += 1
        nanGenes[splitLine[0]] = True
    if (splitLine[1], splitLine[0]) in corrMat:
        tests += 1
        if (float(splitLine[2]) != corrMat[(splitLine[1], splitLine[0])]):
            errCount += 1
        if ((splitLine[2] == '-nan') ^ (numpy.isnan(corrMat[(splitLine[1], splitLine[0])]))):
            errCount += 1
    else:
        corrMat[(splitLine[0], splitLine[1])] = float(splitLine[2])

    i+=1
f.close()


errCount = 0


