for i in {1..20}; do
    (cp FindCorrAndVarFull.cpp $i; cp FindCorrAndVarSmall.cpp $i; cp FindCorrAndVar50.cpp $i; cp FindCorrAndVar20.cpp $i; cd $i; bash ../convertExpData.sh; g++ -o a.out -O3 FindCorrAndVarFull.cpp; g++ -o b.out -O3 FindCorrAndVarSmall.cpp; g++ -o c.out -O3 FindCorrAndVar50.cpp; g++ -o d.out -O3 FindCorrAndVar20.cpp;  ulimit -s unlimited; ./a.out & ./b.out & ./c.out & ./d.out; wait; python ../RhoToWTOFull.py & python ../RhoToWTOSmall.py & python ../RhoToWTO20.py & python ../RhoToWTO50.py; echo $i$ "done") &
    #(cp FindCorrAndVar.cpp $i; cp FindCorrAndVarRand.cpp $i; cd $i; bash ../convertExpData.sh; common="$(wc -l commonGenes.txt | cut -f1 -d' ')"; echo $common; sed -i "s/numberOfGenes = [0-9]*/numberOfGenes = $common/" FindCorrAndVar*; g++ -o a.out -O3 FindCorrAndVar.cpp; g++ -O3 -o b.out FindCorrAndVarRand.cpp; ulimit -s unlimited; ./a.out & ./b.out; wait; python ../FindCSD.py; sed -i 's/ //g' AllValues.txt; sed -i '/\tnan\t/d' AllValues.txt; sed '1d' AllValues.txt | sort -k7 -g -r | cut -f1,2,7 > CValuesSorted.txt; sed '1d' AllValues.txt | sort -k8 -g -r | cut -f1,2,8 > SValuesSorted.txt; sed '1d' AllValues.txt | sort -k9 -g -r | cut -f1,2,9 > DValuesSorted.txt; python ../EvaluateCSD.py; echo $i$ "done") & 
done
