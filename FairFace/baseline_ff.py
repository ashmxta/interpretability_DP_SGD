# run_ff_train.py
from train_ff import train_fn
import datetime

# Initialize the training object
model = train_fn(
    lr=0.1,
    batch_size=256,
    dataset='FairFace',
    architecture='resnet56',
    epochs=40,
    dp=0,  # No DP — baseline sanity check
    norm_type='gn',
    optimizer='sgd',
    save_freq=None,
    seed=24,
    reduction='mean',
    save_name='baseline_test',
)

print(f"Trainset size: {len(model.trainset)}")
print(f"Total steps: {model.sequence.shape[0]}")

steps_per_epoch = model.sequence.shape[0] // model.epochs

# Train and log per epoch
for step in range(model.sequence.shape[0]):
    if step % steps_per_epoch == 0:
        current_epoch = step // steps_per_epoch + 1
        print(f"\n========== Epoch {current_epoch}/{model.epochs} ==========")
        print(f"[{datetime.datetime.now()}] Starting epoch {current_epoch}")

    model.train(step)

# Final validation
final_acc = model.validate()
print(f"\nFinal accuracy: {final_acc * 100:.2f}%")


# nohup python baseline_ff.py > output.log 2>&1 &
