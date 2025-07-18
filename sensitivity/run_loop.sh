#!/bin/bash
# Iterate runs from XX to XX
for run in {1..3}
do
    for i in {0..10}
    do
        stage=$(echo "scale=3; $i / 10" | bc) 
        # beginning of each epoch (40 total)
        # scale keeps 3 d.p.
        echo "Starting run ${run}, stage ${stage}"
        python compute_sensitivity.py --stage $stage --save-name "ckpt_n1${run}" --res-name "res_n1${run}" 
    done
done

echo "Running res_concat.py to merge results..."
python3 ./res/res_concat.py  
echo "Starting composition calculation on res_concat.csv..."
python3 renyi_per_instance_sum_compo.py "./res/res_concat.csv"
echo "Composition calculation completed."
echo "Running rank.py to rank results..."
python3 ./compo_res/rank.py

# to make the script executable: chmod +x run_loop.sh
# to run: ./run_loop.sh
# to run in background: nohup ./run_loop.sh > output.log 2>&1 &
# to kill: kill -9 [PID]