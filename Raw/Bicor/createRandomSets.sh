for i in {1..20}; do
    rm -r $i
    mkdir $i
    (cp Ecoli.tsv $i; cp RandomizeGNWNet.py $i; cd $i; python RandomizeGNWNet.py; grep -x -f Randomized.tsv Ecoli.tsv | cut -f1-2 > conserved.txt) &
done
