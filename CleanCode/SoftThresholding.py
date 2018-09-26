files = ['RhoAndVarSmall.txt', 'RhoAndVar20.txt', 'RhoAndVar50.txt', 'RhoAndVarFull.txt']
import re


for fname in files:
    print fname
    f = open(fname)
    of = open(re.sub('Var', 'VarExp', fname), 'w')
    for line in f:
        splitLine = line.rstrip().split('\t')
        print >> of, splitLine[0]+'\t'+splitLine[1]+'\t'+str(pow(float(splitLine[2]), 6))



