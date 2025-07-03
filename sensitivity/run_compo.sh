#!/bin/bash


echo "Starting composition calculation on res_concat.csv..."

python3 renyi_per_instance_sum_compo.py "./res/res_concat.csv"

echo "Composition calculation completed."


# chmod +x run_compo.sh       --> to make executable
# ./run_compo.sh              --> to run
# nohup ./run_compo.sh > output_compo.log 2>&1 &   --> to run in background
# tail -f output_compo.log    --> to watch logs
