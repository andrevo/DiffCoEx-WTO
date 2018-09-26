#!/bin/bash
for i in {0..19}; do
    cd MultiSets/$i
    python ../../compareWTOtoCorr.py >> ../../RhoAndWTOSimilarity.txt
    cd ../../
    done
