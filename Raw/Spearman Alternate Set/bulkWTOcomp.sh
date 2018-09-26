#!/bin/bash
for i in {0..19}; do
    (cp SampleRhoToWTOSmallLowMem.py MultiSets/$i; cp SampleRhoToWTO20LowMem.py MultiSets/$i; cp SampleRhoToWTO50LowMem.py MultiSets/$i; cp SampleRhoToWTOFullLowMem.py MultiSets/$i; cd MultiSets/$i; python SampleRhoToWTOSmallLowMem.py & python SampleRhoToWTO20LowMem.py & python SampleRhoToWTO50LowMem.py & python SampleRhoToWTOFullLowMem.py) &
    done
