# Forged Distributions

The scripts in this repo evaluate various approximation techniques on per-instance per-step privacy cost curves, with the goal of reducing compute costs of experiments at scale. Model training and grad norm computation scripts are in the 'sensitivity' folder, the set-up is adapted from [Gradients Look Alike: Sensitivity is Often Overestimated in DP-SGD](https://arxiv.org/abs/2307.00310).

## 1. Model training to obtain gradient norms and per-point privacy guarantees:
a) To compute the gradeint norms of certain data points before computing their per-point guarantees of DP-SGD:
    - Use run.sh (or run_loop.sh to do multiple runs at once) to compute grad norms for 10 MNIST data points over 40 epochs (staged every epoch) in the background:
        - to make the script executable: chmod +x run.sh
        - to run in background: nohup ./run.sh > output.log 2>&1 &
        - checkpoints saved to models/ckptX (X = run)
        - results saved to res/resX.csv; 10 runs completed for this experiment (note these files are saved according to training run)
        - res_per_point contains CSV files per point per run and average of grad norms across trials per point (naming convention: res_runX_pointX / res_runA_pointX)
b) To obtain the total privacy loss (per data point, composition over steps), run renyi_per_instance_sum_compo.py (using bash script run_compo.sh if preferred)

## 2. Obtain indicies of points of lowest impact:
a) compo_res.CSV files contain privacy costs per step, to obtain the total privacy cost they must first be summed, and then they can be ranked using compo_res/rank.py.
b) [in-progress] all data in SQL 
c) [in-progress] data visualization with seaborn

 ## Plotting privacy cost curves (approximation techniques)
** Summer 2024 codebase
