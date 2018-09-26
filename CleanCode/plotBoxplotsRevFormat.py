import matplotlib.pyplot as plt
import numpy as np

corrMat = {}
jaccMat = {}

sets = ["rho10", "rho20", "rho50", "rhoFull", "wto10", "wto20", "wto50", "wtoFull"]
for i in sets:
    for j in sets:
        corrMat[(i, j)] = []
        jaccMat[(i, j)] = []

f = open("RhoAndWTOSimilarity.txt")

#f.readline()
i = 0
for line in f:
    print i
    i+=1
    splitLine = line.rstrip().split('\t')
    corrMat[("rho10", "rhoFull")].append(float(splitLine[0]))
    corrMat[("rho20", "rhoFull")].append(float(splitLine[1]))
    corrMat[("rho50", "rhoFull")].append(float(splitLine[2]))
    corrMat[("wto10", "wtoFull")].append(float(splitLine[3]))
    corrMat[("wto20", "wtoFull")].append(float(splitLine[4]))
    corrMat[("wto50", "wtoFull")].append(float(splitLine[5]))
    corrMat[("wto10", "rhoFull")].append(float(splitLine[6]))
    corrMat[("wto20", "rhoFull")].append(float(splitLine[7]))
    corrMat[("wto50", "rhoFull")].append(float(splitLine[8]))
    corrMat[("wtoFull", "rhoFull")].append(float(splitLine[9]))    


boxCombs = []
boxCombs.append(corrMat[("rho10", "rhoFull")])
boxCombs.append(corrMat[("wto10", "wtoFull")])
boxCombs.append(corrMat[("wto10", "rhoFull")])
boxCombs.append(corrMat[("rho20", "rhoFull")])
boxCombs.append(corrMat[("wto20", "wtoFull")])
boxCombs.append(corrMat[("wto20", "rhoFull")])
boxCombs.append(corrMat[("rho50", "rhoFull")])
boxCombs.append(corrMat[("wto50", "wtoFull")])
boxCombs.append(corrMat[("wto50", "rhoFull")])
boxCombs.append(corrMat[("wtoFull", "rhoFull")])


                    
plt.boxplot(boxCombs)
plt.savefig("wtoComparisonSpearmanRevFormat.png", dpi=600)
plt.close()

f = open("RhoAndWTOSimilarity.txt")

f.readline()
for line in f:
    splitLine = line.rstrip().split('\t')
    jaccMat[("rho10", "rhoFull")].append(float(splitLine[10]))
    jaccMat[("rho20", "rhoFull")].append(float(splitLine[11]))
    jaccMat[("rho50", "rhoFull")].append(float(splitLine[12]))
    jaccMat[("wto10", "wtoFull")].append(float(splitLine[13]))
    jaccMat[("wto20", "wtoFull")].append(float(splitLine[14]))
    jaccMat[("wto50", "wtoFull")].append(float(splitLine[15]))
    jaccMat[("wto10", "rhoFull")].append(float(splitLine[16]))
    jaccMat[("wto20", "rhoFull")].append(float(splitLine[17]))
    jaccMat[("wto50", "rhoFull")].append(float(splitLine[18]))
    jaccMat[("wtoFull", "rhoFull")].append(float(splitLine[19]))    

boxCombs = []

boxCombs.append(jaccMat[("rho10", "rhoFull")])
boxCombs.append(jaccMat[("wto10", "wtoFull")])
boxCombs.append(jaccMat[("wto10", "rhoFull")])
boxCombs.append(jaccMat[("rho20", "rhoFull")])
boxCombs.append(jaccMat[("wto20", "wtoFull")])
boxCombs.append(jaccMat[("wto20", "rhoFull")])
boxCombs.append(jaccMat[("rho50", "rhoFull")])
boxCombs.append(jaccMat[("wto50", "wtoFull")])
boxCombs.append(jaccMat[("wto50", "rhoFull")])
boxCombs.append(jaccMat[("wtoFull", "rhoFull")])


                    
plt.boxplot(boxCombs)
plt.savefig("wtoComparisonJaccardRevFormat.png", dpi=600)
plt.close()


perfDiff = {}

perfDiff[("rho10", "wto10")] = []
perfDiff[("rho20", "wto20")] = []
perfDiff[("rho50", "wto50")] = []

for i in range(19):
    perfDiff[("rho10", "wto10")].append(corrMat[("wto10", "rhoFull")][i] - corrMat[("rho10", "rhoFull")][i])
    perfDiff[("rho20", "wto20")].append(corrMat[("wto20", "rhoFull")][i] - corrMat[("rho20", "rhoFull")][i])
    perfDiff[("rho50", "wto50")].append(corrMat[("wto50", "rhoFull")][i] - corrMat[("rho50", "rhoFull")][i])
                                        
                                        
             
boxCombs = [perfDiff[("rho10", "wto10")], perfDiff[("rho20", "wto20")], perfDiff[("rho50", "wto50")]]
plt.boxplot(boxCombs)
plt.savefig("wtoPerfImprovement.png", dpi=600)
plt.close()

