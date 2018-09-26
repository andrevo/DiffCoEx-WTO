import matplotlib.pyplot as plt
import numpy as np


sets = ["rho10", "rho20", "rho50", "rhoFull", "wto10", "wto20", "wto50", "wtoFull"]
mets = ['len', 'rhoOL', 'wtoOL', 'mod', 'noMod', 'clust', 'asst']
mats = {}

for met in mets:
    mats[met] = {}
    for i in sets:
        mats[met][i] = []

    
f = open("RhoAndWTOSimilarityCutoff.txt")

f.readline()
for line in f:
    splitLine = line.rstrip().split(' ')
    i = 0
    for met in mets:
        for j in range(len(sets)):
            mats[met][sets[j]].append(float(splitLine[i+j]))
        i+= len(sets)

    
for met in mets:

    boxCombs = []
    for i in sets:
        boxCombs.append(mats[met][i])
    


                    
    plt.boxplot(boxCombs)
    plt.savefig(met+".png", dpi=600)
    plt.close()

