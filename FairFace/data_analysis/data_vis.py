import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Paths
DATA_DIR = "/h/321/ashmita/forged_distributions/FairFace/data"
TRAIN_CSV = os.path.join(DATA_DIR, "fairface_label_train.csv")
OUT_DIR = "/h/321/ashmita/forged_distributions/FairFace/data_analysis/outputs"
os.makedirs(OUT_DIR, exist_ok=True)

df = pd.read_csv(TRAIN_CSV)

# Count plots with percentages
def plot_distribution(column):
    plt.figure(figsize=(8, 5))
    order = df[column].value_counts().index
    ax = sns.countplot(data=df, x=column, order=order)

    total = len(df)
    for p in ax.patches:
        count = int(p.get_height())
        percentage = f'{100 * count / total:.1f}%'
        ax.annotate(percentage, (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10)

    plt.title(f"{column.title()} Distribution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/{column}_distribution.png")
    plt.close()

for col in ["race", "gender", "age"]:
    plot_distribution(col)

# Cross-tab heatmaps with percent of total dataset
def plot_crosstab_heatmap(col1, col2):
    ct = pd.crosstab(df[col1], df[col2])
    total = ct.values.sum()

    # Create annotations: count + percent of total
    annot = np.empty_like(ct.values, dtype=object)
    for i in range(ct.shape[0]):
        for j in range(ct.shape[1]):
            count = ct.values[i, j]
            pct = 100 * count / total
            annot[i, j] = f"{count}\n({pct:.1f}%)"

    plt.figure(figsize=(10, 6))
    sns.heatmap(ct, annot=annot, fmt='', cmap="Blues", cbar_kws={'label': 'Raw Count'},
                xticklabels=ct.columns, yticklabels=ct.index)
    plt.title(f"{col1.title()} vs {col2.title()} (% of Total Dataset)")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/{col1}_vs_{col2}_heatmap.png")
    plt.close()

plot_crosstab_heatmap("race", "gender")
plot_crosstab_heatmap("race", "age")
