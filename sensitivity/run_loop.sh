#!/bin/bash
# Iterate runs from XX to XX
for run in {2..10}
do
    for i in {0..40}
    do
        stage=$(echo "scale=3; $i / 40" | bc) 
        # beginning of each epoch (40 total)
        # scale keeps 3 d.p.
        echo "Starting run ${run}, stage ${stage}"
        python compute_sensitivity.py --stage $stage --save-name "ckpt${run}" --res-name "res${run}" --less-point "1" --removedpoints 293
    done
done

# to make the script executable: chmod +x run_loop.sh
# to run: ./run_loop.sh
# to run in background: nohup ./run_loop.sh > output.log 2>&1 &
