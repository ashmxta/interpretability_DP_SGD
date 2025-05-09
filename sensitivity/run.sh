#!/bin/bash
# Iterate runs
run=1
for i in {0..40}
do
    stage=$(echo "scale=3; $i / 40" | bc) 
    # beginning of each epoch (40 total)
    # scale keeps 3 d.p.
    echo "Starting run ${run}, stage ${stage}"
    python compute_sensitivity.py --stage $stage --save-name "ckpt${run}" --res-name "res${run}"
done

# to make the script executable: chmod +x run.sh
# to run: ./run.sh
# to run in background: nohup ./run.sh > output.log 2>&1 &
