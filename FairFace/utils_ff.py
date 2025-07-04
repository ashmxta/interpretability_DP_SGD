import os
import numpy as np
import torch.optim as optim

'''
summary of main changes; MNIST / CIFAR -> FairFace
- torchvision imports removed (N/A here)
- load dataset (MNIST / CIFAR specific removed)
- get_optimizer if conditions (dataset based) removed
- should be good to go - yet to test
'''
# no changes
def create_sequences(batch_size, dataset_size, epochs, sample_data, poisson=False, remove_points=None):
    # create a sequence of data indices used for training
    num_batch = (epochs * dataset_size) // batch_size
    dataset = np.arange(dataset_size)
    if remove_points is not None:
        if not isinstance(remove_points, list):
            remove_points = [remove_points]
        for remove_point in remove_points:
            dataset = dataset[dataset != remove_point]
        dataset_size = dataset.shape[0]
    if sample_data < 1:
        sample_vector = np.random.default_rng().choice([False, True], size=dataset_size, replace=True,
                                                       p=[1 - sample_data, sample_data])
        dataset = dataset[sample_vector]
        dataset_size = dataset.shape[0]
    if poisson:
        p = batch_size / dataset_size
        sequence = []
        for _ in range(num_batch):
            sampling = np.random.binomial(1, p, dataset_size)
            indices = dataset[sampling.astype(np.bool_)]
            sequence.append(indices)
        sequence = np.array(sequence, dtype=object)
    else:
        sequence = np.concatenate([np.random.default_rng().choice(dataset, size=dataset_size, replace=False)
                                   for i in range(epochs)])
        sequence = np.reshape(sequence[:num_batch * batch_size], [num_batch, batch_size])
    return sequence


def get_optimizer(net, lr, num_batch, dec_lr=None, privacy_engine=None, gamma=0.1, optimizer_type="sgd"):
    if optimizer_type == "sgd":
        optimizer = optim.SGD(net.parameters(), lr=lr, momentum=0.9, weight_decay=5e-4)
        # Optional LR schedule
        if dec_lr is not None:
            scheduler = optim.lr_scheduler.MultiStepLR(
                optimizer,
                milestones=[round(i * num_batch) for i in dec_lr],
                gamma=gamma
            )
        else:
            scheduler = None
    elif optimizer_type == "adam":
        print("Using Adam optimizer")
        optimizer = optim.Adam(net.parameters(), lr=lr)
        scheduler = None
    else:
        raise ValueError(f"Unsupported optimizer: {optimizer_type}")

    if privacy_engine is not None:
        privacy_engine.attach(optimizer)

    return optimizer, scheduler

def get_save_dir(save_name):
    if not os.path.exists("models"):
        os.mkdir("models")
    return os.path.join("models", save_name)


def find_ckpt(ckpt_step, trainset_size, batch_size, save_freq, epochs):
    if isinstance(ckpt_step, str):
        if ckpt_step == "final":
            ckpt_step = 1
        elif ckpt_step == "middle":
            ckpt_step = 0.5
        elif ckpt_step == "initial":
            ckpt_step = 0
        else:
            ckpt_step = float(ckpt_step)

    total_ckpts = trainset_size * epochs // batch_size // save_freq
    return round(total_ckpts * ckpt_step) * save_freq


def get_last_ckpt(save_dir, keyword):
    saved_points = [int(model_path[len(keyword):]) for model_path in os.listdir(save_dir)
                    if keyword in model_path]
    return max(saved_points)
