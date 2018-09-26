import numpy
import bisect

startSample = 1
endSample = 21
sets = range(startSample, endSample)


cROCraw = []
sROCraw = []
dROCraw = []

cROCshort = []
sROCshort = []
dROCshort = []



for num in sets:
    fname = str(num)+"/cROCCSD.txt"
    cROC = []
    f = open(fname)
    for line in f:
        splitLine = line.rstrip().split(" ")
        cROC.append((float(splitLine[1]), float(splitLine[0])))
    cROCraw.append(cROC)

    fname = str(num)+"/sROCCSD.txt"
    sROC = []
    f = open(fname)
    for line in f:
        splitLine = line.rstrip().split(" ")
        sROC.append((float(splitLine[1]), float(splitLine[0])))
    sROCraw.append(sROC)
        
    fname = str(num)+"/dROCCSD.txt"
    dROC = [] 
    f = open(fname)
    for line in f:
        splitLine = line.rstrip().split(" ")
        
        dROC.append((float(splitLine[1]), float(splitLine[0])))
    dROCraw.append(dROC)

    cROCshort.append([])
    sROCshort.append([])
    dROCshort.append([])

    cROClist = []
    sROClist = []
    dROClist = []


    for i in range(1001):
        cROClist.append([])
        sROClist.append([])
        dROClist.append([])
    
    for pair in cROCraw[num-startSample]:
        cROClist[int(pair[0]*1000)].append(pair[1])
    for pair in sROCraw[num-startSample]:
        sROClist[int(pair[0]*1000)].append(pair[1])
    for pair in dROCraw[num-startSample]:
        dROClist[int(pair[0]*1000)].append(pair[1])


        
    for i in range(1001):
        
        cROCshort[num-startSample].append(numpy.mean(cROClist[i]))
        sROCshort[num-startSample].append(numpy.mean(sROClist[i]))
        dROCshort[num-startSample].append(numpy.mean(dROClist[i]))

    
cROCavg = []
sROCavg = []
dROCavg = []

for i in range(1001):
    c = []
    s = []
    d = []
    for j in range(len(cROCshort)):
        c.append(cROCshort[j][i])
        s.append(sROCshort[j][i])
        d.append(dROCshort[j][i])
    cROCavg.append(numpy.mean(c))
    sROCavg.append(numpy.mean(s))
    dROCavg.append(numpy.mean(d))


f = open("cROCavgCSD.txt", 'w')
for i in range(1000):
    print >> f, float(i)/1000, cROCavg[i]
f.close()

f = open("sROCavgCSD.txt", 'w')
for i in range(1000):
    print >> f, float(i)/1000, sROCavg[i]
f.close()

f = open("dROCavgCSD.txt", 'w')
for i in range(1000):
    print >> f, float(i)/1000, dROCavg[i]
f.close()
