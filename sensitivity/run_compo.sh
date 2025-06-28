#!/bin/bash

if [ -n "$wait_pid" ]; then
    echo "Waiting for run.sh to complete..."
    while kill -0 "$wait_pid" 2>/dev/null; do
        sleep 1
    done
fi

echo "run.sh has completed. Starting composition calculations..."

# Loop over res1.csv to res10.csv
for X in {1..10}
do
    echo "Running composition for res${X}.csv..."
    python3 renyi_per_instance_sum_compo.py "./res/res${X}.csv"
done

echo "Composition calculations completed."

# Instructions:
# chmod +x run_compo.sh       --> to make executable
# ./run_compo.sh              --> to run
# nohup ./run_compo.sh > output_compo.log 2>&1 &   --> to run in background
# tail -f output_compo.log    --> to watch logs
