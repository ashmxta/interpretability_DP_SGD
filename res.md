Data on res files: 
| `distance (sum)`  | l2 norm of gradients summed across batch (used for sensitivity) |
| `step`            | Training step |
| `real batch size` | Effective batch size during the step |
| `p`               | |
| `point`           | Index of the data point |
| `sigma`           | Noise multiplier used in DP-SGD |
| `correct`         |  |
| `accuracy`        | Accuracy at this step |
| `type`            |  |
| `points`          | Total number of points evaluated |
| `batch_size`      | Configured batch size |
| `num_iters`       | Number of iterations (for Renyi accounting) |
| `alpha`           | Rényi divergence order |
| `num_batches`     | Number of batches in the dataset |
| `lr`              | Learning rate |
| `cn`              | Clip norm|
| `epochs`          | Total epochs |
| `dp`              | Whether DP-SGD was used (0/1) |
| `eps`             | Privacy budget ε (epsilon) |
| `optimizer`       | Optimizer used |
| `dataset`         | Dataset name (e.g. MNIST) |
| `model`           | Model architecture (e.g. lenet) |
| `norm_type`       | Type of norm used for gradient clipping (e.g. `gn`) |
| `save_freq`       | Frequency (in steps) of saving model checkpoints |
| `save_name`       | |
| `res_name`        | Results CSV file |
| `gamma`           |  |
| `dec_lr`          | |
| `id`              | |
| `seed`            | Random seed (default 24) |
| `overwrite`       | Whether to overwrite existing run (0/1) |
| `poisson_train`   |  |
| `stage`           | |
| `reduction`       | Aggregation method (e.g. `sum`) |
| `exp`             | |
| `less_point`      | |
