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



paste SampleWTO50.txt RhoAndVar50.txt.sample | cut -f1,4 | sed 's/\t/ /g' > SampleWTOandRho50.txt
paste SampleWTO20.txt RhoAndVar20.txt.sample | cut -f1,4 | sed 's/\t/ /g' > SampleWTOandRho20.txt
paste SampleWTOFull.txt RhoAndVarFull.txt.sample | cut -f1,4 | sed 's/\t/ /g' > SampleWTOandRhoFull.txt
paste SampleWTOSmall.txt RhoAndVarSmall.txt.sample | cut -f1,4 | sed 's/\t/ /g' > SampleWTOandRhoSmall.txt