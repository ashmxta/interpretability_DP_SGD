# Forged Distributions

The scripts in this repo evaluate various approximation techniques on per-instance per-step privacy cost curves, with the goal of reducing compute costs of experiments at scale. Model training and grad norm computation scripts are in the 'sensitivity' folder, the set-up is adapted from [Gradients Look Alike: Sensitivity is Often Overestimated in DP-SGD](https://arxiv.org/abs/2307.00310).

## Model training to obtain per-instance per-step privacy costs
1. To compute the sensitivity of certain data points before computing their per-instance guarantees of DP-SGD:
    - Use run.sh (or run_loop.sh to do multiple runs at once) compute sensitivity for 10 MNIST data points over 40 epochs (staged every epoch) in the background:
        - to make the script executable: chmod +x run.sh
        - to run in background: nohup ./run.sh > output.log 2>&1 &
        - checkpoints saved to models/ckptX (X = run)
        - results saved to res/resX.csv
2. 

 ## Plotting privacy cost curves
