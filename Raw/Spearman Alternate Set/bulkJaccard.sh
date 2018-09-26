#!/bin/bash
for i in {0..19}; do
    cd MultiSets/$i
    bash ../../transformSampleData.sh
    python ../../compareWTOtoCorr.py >> ../../RhoAndWTOSimilarity.txt
    cd ../../
    done
