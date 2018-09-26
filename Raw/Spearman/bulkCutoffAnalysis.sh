#!/bin/bash
for i in {0..19}; do
    cd MultiSets/$i
    python ../../compareWTOtoCorrWithCutoff.py >> ../../RhoAndWTOSimilarityCutoff.txt
    cd ../../
    done
