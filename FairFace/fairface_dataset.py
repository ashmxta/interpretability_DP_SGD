import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset
import torchvision.transforms as transforms

class FairFaceDataset(Dataset):
    def __init__(self, csv_path, img_dir, transform=None):
        self.data = pd.read_csv(csv_path)
        self.img_dir = img_dir
        self.transform = transform
        assert 'file' in self.data.columns
        assert 'race' in self.data.columns
        self.label_map = {label: idx for idx, label in enumerate(sorted(self.data['race'].unique()))}
        self.data['label'] = self.data['race'].map(self.label_map)

    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        img_name = row['file'].replace("train/", "").replace("val/", "")
        img_path = os.path.join(self.img_dir, img_name)
        image = Image.open(img_path).convert('RGB')
        label = row['label']
        if self.transform:
            image = self.transform(image)
        return image, label
