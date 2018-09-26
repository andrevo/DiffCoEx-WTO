for i in {1..20}; do
    (cd $i; python ../EvaluateWTO.py; echo $i$ "done") & 
done
