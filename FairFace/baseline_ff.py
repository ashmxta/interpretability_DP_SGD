from train_ff import train_fn

model = train_fn(
    lr=0.1,
    batch_size=256,
    dataset='FairFace',
    architecture='resnet56',
    exp_id='debug',
    epochs=40,
    dp=0,  # no DP for best performance sanity check
    norm_type='gn',
    optimizer='sgd',
    save_freq=None,
    seed=24,
    reduction='mean',
    save_name='baseline_test',
)

print(f"Trainset size: {len(model.trainset)}")
print(f"Total steps: {model.sequence.shape[0]}")

for step in range(model.sequence.shape[0]):
    print(f"Training step {step}")
    model.train(step) 

acc = model.validate()
print(f"Final accuracy: {acc * 100:.2f}%")


