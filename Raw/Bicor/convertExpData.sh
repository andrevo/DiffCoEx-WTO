#!/bin/bash


grep -P '^"|^1000' Ecoli_dream4_timeseries.tsv > OrigEColiExpData.tsv
awk '
{ 
    for (i=1; i<=NF; i++)  {
        a[NR,i] = $i
    }
}
NF>p { p = NF }
END {    
    for(j=1; j<=p; j++) {
        str=a[1,j]
        for(i=2; i<=NR; i++){
            str=str" "a[i,j];
        }
        print str
    }
}' OrigEColiExpData.tsv > temp
mv temp OrigEColiExpData.tsv
#sed -i '1d' OrigEColiExpData.tsv
sed -i 's/ /\t/g' OrigEColiExpData.tsv
sort OrigEColiExpData.tsv > temp
mv temp OrigEColiExpData.tsv


# grep -P '^"|^1000' Randomized_dream4_timeseries.tsv > RandEColiExpData.tsv
# awk '                                                                                                                                                                                                                                  
# {                                                                                                                                                                                                                                      
#     for (i=1; i<=NF; i++)  {                                                                                                                                                                                                           
#         a[NR,i] = $i                                                                                                                                                                                                                   
#     }                                                                                                                                                                                                                                  
# }                                                                                                                                                                                                                                      
# NF>p { p = NF }                                                                                                                                                                                                                        
# END {                                                                                                                                                                                                                                  
#     for(j=1; j<=p; j++) {                                                                                                                                                                                                              
#         str=a[1,j]                                                                                                                                                                                                                     
#         for(i=2; i<=NR; i++){                                                                                                                                                                                                          
#             str=str" "a[i,j];                                                                                                                                                                                                          
#         }                                                                                                                                                                                                                              
#         print str                                                                                                                                                                                                                      
#     }                                                                                                                                                                                                                                  
# }' RandEColiExpData.tsv > temp
#mv temp RandEColiExpData.tsv
#sed -i '1d' RandEColiExpData.tsv
#sed -i 's/ /\t/g' RandEColiExpData.tsv
#sort RandEColiExpData.tsv > temp
#mv temp RandEColiExpData.tsv
#sed -i '1s/^/\n/' RandEColiExpData.tsv

#cut -f1 RandEColiExpData.tsv | sort | uniq > commonGenes.txt
#grep -w -f commonGenes.txt OrigEColiExpData.tsv > OrigEColiExpDataFiltered.tsv
#sed -i '1s/^/\n/' OrigEColiExpDataFiltered.tsv
