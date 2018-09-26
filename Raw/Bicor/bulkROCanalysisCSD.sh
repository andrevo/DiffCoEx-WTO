for i in {1..20}; do
    (cp FindCorrAndVar.cpp $i; cp FindCorrAndVarRand.cpp $i; cd $i; bash ../convertExpData.sh; common="$(wc -l commonGenes.txt | cut -f1 -d' ')"; echo $common; sed -i "s/numberOfGenes = [0-9]*/numberOfGenes = $common/" FindCorrAndVar*; g++ -o a.out -O3 FindCorrAndVar.cpp; g++ -O3 -o b.out FindCorrAndVarRand.cpp; ulimit -s unlimited; ./a.out & ./b.out; wait; python ../FindCSD.py; sed -i 's/ //g' AllValues.txt; sed -i '/\tnan\t/d' AllValues.txt; sed '1d' AllValues.txt | sort -k7 -g -r | cut -f1,2,7 > CValuesSorted.txt; sed '1d' AllValues.txt | sort -k8 -g -r | cut -f1,2,8 > SValuesSorted.txt; sed '1d' AllValues.txt | sort -k9 -g -r | cut -f1,2,9 > DValuesSorted.txt; python ../EvaluateCSD.py; echo $i$ "done") & 
done
