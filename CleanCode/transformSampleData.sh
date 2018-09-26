sort SampleWTOFull.txt > temp
mv temp SampleWTOFull.txt
sort SampleWTOSmall.txt > temp
mv temp SampleWTOSmall.txt
sort SampleWTO20.txt > temp
mv temp SampleWTO20.txt
sort SampleWTO50.txt > temp
mv temp SampleWTO50.txt

sort RhoAndVar50.txt.sample > temp
mv temp RhoAndVar50.txt.sample
sort RhoAndVar20.txt.sample > temp
mv temp RhoAndVar20.txt.sample
sort RhoAndVarSmall.txt.sample > temp
mv temp RhoAndVarSmall.txt.sample
sort RhoAndVarFull.txt.sample > temp
mv temp RhoAndVarFull.txt.sample



paste RhoAndVar50.txt.sample SampleWTO50.txt | sed 's/\t/ /g' | cut -f1,2,3,6 -d' ' | sed 's/\t/ /g' > SampleWTOandRho50.txt
paste RhoAndVar20.txt.sample SampleWTO20.txt | sed 's/\t/ /g' | cut -f1,2,3,6 -d' '| sed 's/\t/ /g' > SampleWTOandRho20.txt
paste RhoAndVarFull.txt.sample SampleWTOFull.txt | sed 's/\t/ /g' | cut -f1,2,3,6 -d' '| sed 's/\t/ /g' > SampleWTOandRhoFull.txt
paste RhoAndVarSmall.txt.sample SampleWTOSmall.txt | sed 's/\t/ /g' | cut -f1,2,3,6 -d' '| sed 's/\t/ /g' > SampleWTOandRhoSmall.txt
